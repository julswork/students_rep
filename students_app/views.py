from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from .models import Post
from .forms import PostForm
from django.shortcuts import redirect
from django.core.urlresolvers import reverse

from .models import Student, Group
from .forms import StudentForm, GroupForm




# def post_list(request):
#     posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
#     return render(request, 'students/post_list.html', {'posts': posts})
#
#
# def post_detail(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     return render(request, 'students/post_detail.html', {'post': post})
#
#
# def post_new(request):
#     if request.method == "POST":
#         form = PostForm(request.POST)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.author = request.user
#             post.published_date = timezone.now()
#             post.save()
#             return redirect('students_app.views.post_detail', pk=post.pk)
#     else:
#         form = PostForm()
#     return render(request, 'students/post_edit.html', {'form': form})
#
#
# def post_edit(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     if request.method == "POST":
#         form = PostForm(request.POST, instance=post)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.author = request.user
#             post.published_date = timezone.now()
#             post.save()
#             return redirect('students_app.views.post_detail', pk=post.pk)
#     else:
#         form = PostForm(instance=post)
#     return render(request, 'students/post_edit.html', {'form': form})





def group_list(request):
    groups = Group.objects.all()  #(published_date__lte=timezone.now()).order_by('title'))
    return render(request, 'students/group_list.html', {'groups': groups})


def group_detail(request, pk):
    group = get_object_or_404(Group, pk=pk)
    return render(request, 'students/group_detail.html', {'group': group})


def group_new(request):
    if request.method == "POST":
        form = GroupForm(request.POST)
        if form.is_valid():
            group = form.save(commit=False)
            # post.author = request.user
            # post.published_date = timezone.now()
            group.save()
            return redirect('students_app.views.group_detail', pk=group.pk)
    else:
        form = GroupForm()
    return render(request, 'students/group_new.html', {'form': form})


def group_edit(request, pk):
    group = get_object_or_404(Group, pk=pk)
    if request.method == "POST":
        form = GroupForm(request.POST, instance=group)
        if form.is_valid():
            group = form.save(commit=False)
            # group.author = request.user
            # group.published_date = timezone.now()
            group.save()
            return redirect('students_app.views.group_detail', pk=group.pk)
    else:
        form = GroupForm(instance=group)
    return render(request, 'students/group_edit.html', {'form': form, 'group': group})


def student_detail(request, pk):
    student = get_object_or_404(Student, pk=pk)
    return render(request, 'students/student_detail.html', {'student': student})


def student_new(request):
    # group = Group.objects.get(pk=group.pk)
    # print "form", group
    if request.method == "POST":
        form = StudentForm(request.POST)

        if form.is_valid():
            student = form.save(commit=False)
            # post.author = request.user
            # post.published_date = timezone.now()

            student.save()
            return redirect('students_app.views.student_detail', pk=student.pk)
    else:
        form = StudentForm()
    return render(request, 'students/student_new.html', {'form': form})


def student_edit(request, pk):
    student = get_object_or_404(Student, pk=pk)
    group = student.student_group

    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            group = form.save(commit=False)
            # group.author = request.user
            # group.published_date = timezone.now()
            student.save()
            return redirect('students_app.views.student_detail', pk=student.pk)
    else:
        form = StudentForm(instance=student)
    return render(request, 'students/student_edit.html', {'form': form, 'student': student, 'group': group})


def group_student_delete(request, id, pk):
    group = get_object_or_404(Group, pk=pk)
    student = get_object_or_404(Student, id=id)
    student.delete()
    return redirect('students_app.views.group_detail', group.pk)


from django.http import HttpResponse

def test(request):
    print "Test"
    import StringIO

    output = StringIO.StringIO()
    output.write('First line.\n')
    output.write('Second line.\n')

    f = output.getvalue()

    # ics_f = icsfile.IcsFile(output, 'w')
    # ics_f.write('test')

    response = HttpResponse(f, content_type='application/ics')
    response['Content-Disposition'] = 'attachment; filename=s.ics'
    return response

    #
    # print "YYY", contents
    #
    #
    #
    #
    # return render(request, 'students/test.html', {'contents': contents})




