from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from .models import Post
from .forms import PostForm
from django.shortcuts import redirect

from .models import Student, Group
from .forms import StudentForm




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


def student_detail(request, pk):
    student = get_object_or_404(Student, pk=pk)
    return render(request, 'students/student_detail.html', {'student': student})


def student_new(request):
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
    return render(request, 'students/student_edit.html', {'form': form})
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