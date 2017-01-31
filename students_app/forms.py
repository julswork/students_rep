# -*- encoding: utf-8 -*-
"""
Forms for NXT LVL
"""
from django import forms

from models import (
    Employee, UserNxtlvl, EmployeeMailReminder,
)


from datetime import datetime

class LoginForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True, min_length=1)

#
# # class PasswordResetForm(forms.Form):
# #     """
# #     Form to reset password and send the new password by mail
# #     """
# #
# #     email = forms.EmailField(label=_("Email"))
# #     logger.info(u"GET USER EMAIL FOR PASSWORD RESET....  EMAIL = {}".format(email))
# #
# #     def save(self):
# #         logger.info(u"LOOKING FOR EMPLOYEE WITH THIS EMAIL....")
# #         employee = Employee.objects.get(user__email__exact=self.cleaned_data['email'])
# #         logger.info(u"EMPLOYEE INFO....  EMPLOYEE = {}".format(employee))
# #         logger.info(u"GENERATING NEW PASSWORD....")
# #         password = generate_password(8)
# #         logger.info(u"SUCCESSFULY GENERATED. NEW PASSWORD = {}".format(password))
# #         logger.info(u"SETTING NEW PASSWORD FOR EMPLOYEE....")
# #         employee.user.set_password(password)
# #         logger.info(u"PASSWORD SET....")
# #         logger.info(u"SAVING....")
# #         employee.user.save()
# #         logger.info(u"SAVED!....")
#
# #COMMENTED 6.12.2016
#         # email_subject = 'NXT LVL'
#         # email_body = 'NXT LVL: ny password: {}'.format(password)
#         # sender = settings.DEFAULT_FROM_EMAIL
#         # recipients = ['{}'.format(employee.user.email)]
#         #
#         # send_single_mail.delay(email_subject, email_body, sender, recipients)
#
#         logger.info(u"ATTEMPTING TO SEND NEW PASSWORD TO USER....")
#
#         from_email = settings.DEFAULT_FROM_EMAIL
#         recipient_list = ['{}'.format(employee.user.email)]
#         logger.info(u"RECIPIENT EMAIL = {}, NEW PASSWORD = {}".format(employee.user.email, password))
#
#         subject = 'NXT LVL'
#         email_body = 'NXT LVL: ny password: {}'.format(password)
#         logger.info(u"SENDING EMAIL...")
#
#         send_single_mail.delay(
#             from_email, recipient_list, subject, email_body
#         )
#         logger.info(u"EMAIL SENT...")
#
#
#     def clean(self):
#         super(PasswordResetForm, self).clean()
#
#         if not 'email' in self.cleaned_data or not get_user_model().objects.filter(
#                 email__exact=self.cleaned_data['email']).exists():
#             raise forms.ValidationError(_('Unknown email'))
#         return self.cleaned_data
#
#
# class LoginForm(forms.Form):
#     email = forms.EmailField(required=True)
#     password = forms.CharField(required=True, min_length=1)


# class EmployeeForm(forms.Form):
#     """
#     Create employee form
#     """
#     company = forms.ModelChoiceField(queryset=Company.objects.all(), required=True, widget=forms.HiddenInput())
#     first_name = forms.CharField(label=_(u'First name'), max_length=100,
#                                  widget=forms.TextInput(attrs={'class': "form-control"}))
#     last_name = forms.CharField(label=_(u'Last name'), max_length=100,
#                                 widget=forms.TextInput(attrs={'class': "form-control"}))
#     email = forms.EmailField(label=_(u'Email'), widget=forms.TextInput(attrs={'class': "form-control"}))
#     language_code = forms.ChoiceField(label=_("Language"), choices=settings.LANGUAGES,
#                                       widget=forms.Select(attrs={'class': "form-control"}))
#     manager = forms.ModelChoiceField(label=_('Manager'), queryset=Employee.objects.filter(is_manager=True),
#                                      empty_label=_("choose manager"), required=False,
#                                      widget=forms.Select(attrs={'class': "form-control"}))
#     is_manager = forms.BooleanField(required=False, label=_('Create as manager'))
#     title = forms.CharField(label=_(u'Title'), max_length=4000,
#                             widget=forms.TextInput(attrs={'class': "form-control"}))
#
#     def __init__(self, request, *args, **kwargs):
#
#         self.request = request
#         self.user = self.request.user
#
#         super(EmployeeForm, self).__init__(*args, **kwargs)
#
#     def save(self):
#         """
#         Save form and send welcome mail (currently disabled)
#         """
#
#         employee = Employee.objects.get(user=self.user)
#         data = self.data
#         employee_manager = self.cleaned_data['manager']
#
#         employee.isHavePermissions(
#             employee_manager, allow_manager=True, allow_self=True,
#             allow_su=True, raise_exception=True,
#             exception_text="You don't have permissions to add employee to given manager"
#         )
#
#         password = generate_password(8)
#         user_model = get_user_model()
#         users = user_model.objects.filter(email=data.get('email')).all()
#
#         if users:
#             raise SuspiciousOperation("Denne emailadresse er allerede brugt anden bruger i systemet", 400)
#
#         user = user_model.objects.create_user(
#             username=data.get('email'),
#             email=data.get('email'),
#             password=password
#         )
#
#         user.first_name = data.get('first_name')
#         user.last_name = data.get('last_name')
#
#         user.save()
#
#         id = int(data.get('manager'))
#         manager = Employee.objects.get(id=id)
#
#         Employee.objects.create(
#             user=user,
#             manager=manager,
#             is_manager=data.get('is_manager'),
#             company=manager.company,
#             created_by=self.user,
#             updated_by=self.user,
#             language_code=data.get('language_code'),
#             title=data.get('title'),
#         )
#
#
# #COMMENTED 6.12.2016
#         # email_subject = 'NXT LVL'
#         # email_body = 'Du er blevet oprettet som bruger i NXT LVL SYS. Du er oprettet som ny bruger: {},' \
#         #              ' din email: {}, dit password: {} .' \
#         #              ' For at registrere gå til:{}'\
#         #     .format(user.first_name + " " + user.last_name, user.email, password,
#         #             self.request.build_absolute_uri('/#/login'))
#         # sender = settings.DEFAULT_FROM_EMAIL
#         # recipients = [self.data['email']]
#         #
#         # send_single_mail.delay(
#         #     email_subject, email_body, sender, recipients
#         # )
#
#         from_email = settings.DEFAULT_FROM_EMAIL
#         recipient_list = [self.data['email']]
#         subject = 'NXT LVL'
#         email_body = ' Du er blevet oprettet som bruger i NXT LVL SYS. Du er oprettet som ny bruger: {},' \
#                ' din email: {}, dit password: {} .' \
#                ' For at registrere gå til: {}'\
#             .format(user.first_name + " " + user.last_name, user.email, password,
#                      self.request.build_absolute_uri('/#/login'))
#
#         send_single_mail.delay(
#              from_email, recipient_list, subject, email_body
#         )
#
#
#     def _sendWelcomeMail(self, user, password):
#         """
#         Send welcome mail to user
#         """
#
#         template = loader.get_template('create_user_mail.tpl')
#         send_mail(
#             settings.WELCOME_MAIL_SUBJECT,
#             template.render(
#                 Context({
#                     'user': user,
#                     'password': password,
#                     'url': self.request.build_absolute_uri('/#/login/'),
#                     'sender': self.user
#                 })
#             ),
#             self.user.email,
#             [user.email]
#         )
#
#     def clean(self):
#         """
#         Do validation
#         """
#         super(EmployeeForm, self).clean()
#
#         username = self.cleaned_data.get('email')
#
#         if username:
#
#             if not Employee.isValidUsername(username):
#                 raise forms.ValidationError(_(
#                     'Invalid username format. Accepted characters are A-Z,a-z,0-9,_-,.'
#                 ))
#
#             if get_user_model().objects.filter(username__exact=username).exists():
#                 raise forms.ValidationError(_('Denne emailadresse er allerede brugt anden bruger i systemet'))
#
#         if UserNxtlvl.objects.filter(email__exact=self.cleaned_data.get('email')).exists():
#             raise forms.ValidationError(_('Denne emailadresse er allerede brugt anden bruger i systemet'))
#         return self.cleaned_data


#*************************************************************

class EmployeeMailReminderForm(forms.Form):
    title = forms.CharField(required=False)
    description = forms.CharField(required=False)
    reminder_date = forms.DateTimeField(required=False, input_formats=['%Y-%m-%d %H:%M:%S', '%Y-%m-%dT%H:%M:%S'])
    is_achieved = forms.BooleanField(required=False)

    def save(self, current_user, employeemailreminder=None, employee=None):
        if employeemailreminder:
            for f in ['is_achieved', 'title', 'description']:
                if f in self.data:
                    # if f == 'is_achieved_manager' and goal.employee.user == current_user:
                    #     continue
                    setattr(employeemailreminder, f, self.cleaned_data[f])

            employeemailreminder.updated_at = datetime.utcnow()
            employeemailreminder.updated_by = current_user
        else:
            employeemailreminder = EmployeeMailReminder(
                employee=employee if employee else current_user.employee_user,
                title=self.cleaned_data.get("title", ""),
                description=self.cleaned_data.get("description", ""),
                reminder_date=self.cleaned_data.get("reminder_date", ""),
                is_achieved=self.cleaned_data.get("is_achieved", False),
                created_by=current_user,
                updated_by=current_user
            )

        employeemailreminder.save()

        return employeemailreminder


