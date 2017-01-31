# -*- coding: utf-8 -*-
"""
Views for NXT LVL
"""
import pprint
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.cache import never_cache
from django.http import HttpResponseRedirect, JsonResponse
from models import (
    Employee, EmployeeMailReminder,
)
from django.template.response import TemplateResponse
from django.views.decorators.http import require_http_methods
import json
from forms import (
    EmployeeMailReminderForm,#, LoginForm
)

from django.contrib.auth import login, authenticate, logout
from django.core.exceptions import PermissionDenied
from django.forms.models import model_to_dict
from django.contrib.auth import get_user_model
from datetime import datetime
from functools import wraps



def login_required_403(view):
    """
    Decorator that returns 403 status if user isn't logged in
    instead of redirecting to the LOGIN_URL
    """
    @wraps(view)
    def dec_view(request, *args, **kwargs):
        if not request.user.is_authenticated():
            return JsonResponse({"detail": "You have to log in"}, status=403)

        return view(request, *args, **kwargs)

    return dec_view


class EmailAuthBackend(object):
    def authenticate(self, username=None, password=None, **kwargs):
        UserModel = get_user_model()
        try:
            user = UserModel.objects.get(email=username)
        except UserModel.DoesNotExist:
            return None
        else:
            if getattr(user, 'is_active', False) and user.check_password(password):
                return user
        return None

    def get_user(self, user_id):
        UserModel = get_user_model()
        try:
            return UserModel.objects.get(pk=user_id)
        except UserModel.DoesNotExist:
            return None


@csrf_exempt
@require_http_methods(['POST'])
def login_user(request):
    f = LoginForm(data=request.json_body)

    if not f.is_valid():
        return JsonResponse(status=400, data=json.loads(f.errors.as_json()))

    user = authenticate(username=f.cleaned_data["email"], password=f.cleaned_data["password"])

    if not user:
        return JsonResponse({}, status=401)
    else:
        employee = Employee.objects.filter(user=user).first()

        if not employee:
            raise PermissionDenied("You don't have any employee assigned to you", 401)
        login(request, user)

        return JsonResponse(status=200, data={"email": user.email, "employee_id": employee.id,
                                              "user_id": employee.user.pk})


@csrf_exempt
@require_http_methods(['POST'])
def logout_user(request, *args, **kwargs):
    logout(request)

    return JsonResponse({}, status=200)


def accesscode(request, code):
    """
    Login with an accesscode
    """
    employee = Employee.objects.get(access_code=code)
    user = employee.user
    user.backend = 'django.contrib.auth.backends.ModelBackend'
    login(request, user)
    return HttpResponseRedirect('/')


@csrf_exempt
@require_http_methods(['POST'])
def password_reset(request):
    """
    Password reset view
    """
    if request.method == "POST":
        form = PasswordResetForm(request.json_body)
        if form.is_valid():
            form.save()
            return JsonResponse(status=200, data={"password": "change"})
        return JsonResponse(status=400, data=json.loads(form.errors.as_json()))


def password_reset_done(request):
    """
    Password reset done
    """

    return TemplateResponse(
        request,
        'reset_done.html',

    )


@login_required_403
def employees_json(request):
    """
    Get all employees as json
    """
    # current_employee = Employee.objects.get(user__pk=request.user.pk)
    employee_list = Employee.objects.all()
    employees = list()

    for employee in employee_list:
        manager_dict = model_to_dict(employee)
        manager_dict['first_name'] = employee.user.first_name
        manager_dict['last_name'] = employee.user.last_name
        employees.append(manager_dict)

    data = {"employees": employees}

    return JsonResponse(status=200, data=data)





@login_required_403
@never_cache
def employees_json_id(request, employee_id):
    """
    Show employee a level below
    """
    curent_employee = Employee.objects.get(pk=int(employee_id))
    if curent_employee.is_manager:
        employee_list = Employee.objects.all()
        employees = list()
        for employee in employee_list:
            employee_dict = model_to_dict(employee)
            employee_dict['first_name'] = employee.user.first_name
            employee_dict['last_name'] = employee.user.last_name

            employees.append(employee_dict)
        data = {"employees": employees}
    else:
        return JsonResponse(status=400, data={"error": "Employee with id={} not is_manager".format(int(employee_id))})
    return JsonResponse(data=data, content_type='application/json', safe=False)



#*****************************

@login_required_403
@csrf_exempt
def create_mail_reminder(request, employee_id=None):
    current_user = request.user
    current_employee = current_user.employee_user

    fields = ['title', 'id', 'is_achieved', 'description', 'reminder_date', 'created_at']

    employee = current_employee

    if employee_id:
        employee = Employee.objects.get(pk=int(employee_id))

    current_employee.isHavePermissions(
        employee, allow_manager=True, allow_su=True, allow_self=True, raise_exception=True,
        exception_text="You don't have permissions to see Mail Reminders of this employee."
    )

    if request.method == 'POST':
        f = EmployeeMailReminderForm(data=request.json_body)

        if not f.is_valid():
            return JsonResponse(data={"detail": json.loads(f.errors.as_json())}, status=400)

        employeemailreminder = f.save(current_user, None, employee)

        return JsonResponse(
            data={f: getattr(employeemailreminder, f) for f in fields}, status=201
        )
    elif request.method == 'GET':
        is_achieved_employeemailreminder = request.GET.get('is_achieved')

        if employee_id:
            employeemailreminder_list = EmployeeMailReminder.objects.filter(employee=employee)
        else:
            employeemailreminder_list = EmployeeMailReminder.objects.filter(employee=current_employee)

        if is_achieved_employeemailreminder is not None:
            employeemailreminder_list = employeemailreminder_list.filter(
                is_achieved=True if is_achieved_employeemailreminder == 'true' else False)

        employeemailreminders = [
            {f: getattr(emr, f) for f in fields} for emr in employeemailreminder_list
        ]

        return JsonResponse(data={"employeemailreminders": employeemailreminders}, status=200)


@login_required_403
@csrf_exempt
def self_mail_reminder_by_id(request, employeemailreminder_id):
    """
    Get or Update employeemailreminder by id

    Not in use
    """
    current_user = request.user
    current_employee = current_user.employee_user

    fields = ['title', 'id', 'is_achieved', 'description', 'reminder_date', 'created_at']

    employeemailreminder = EmployeeMailReminder.objects.get(pk=employeemailreminder_id)

    current_employee.isHavePermissions(
        employeemailreminder.employee, allow_self=True, allow_manager=True, allow_su=True, raise_exception=True,
        exception_text="You don't have access to mail reminders of this employee."
    )

    if request.method == 'POST':
        f = EmployeeMailReminderForm(data=request.json_body)

        if not f.is_valid():
            return JsonResponse(data={"detail": json.loads(f.errors.as_json())}, status=400)

        employeemailreminder = f.save(current_user, employeemailreminder)

    return JsonResponse(
        data={f: getattr(employeemailreminder, f) for f in fields}, status=200
    )


@login_required_403
@csrf_exempt
def delete_mail_reminder(request, employeemailreminder_id):
    current_user = request.user
    current_employee = current_user.employee_user

    fields = ['title', 'id', 'is_achieved', 'description', 'reminder_date', 'created_at']

    employeemailreminder = EmployeeMailReminder.objects.get(pk=employeemailreminder_id)

    current_employee.isHavePermissions(
        employeemailreminder.employee, allow_self=True, allow_manager=True, allow_su=True, raise_exception=True,
        exception_text="You don't have access to mail reminders of this employee."
    )

    if request.method == 'POST':
        employeemailreminder.delete()

        return JsonResponse(data={"detail": "Mail Reminder with id {} was deleted successfully."
                            .format(employeemailreminder_id)}, status=204)

    return JsonResponse(
        data={f: getattr(employeemailreminder, f) for f in fields}, status=200
    )