from django import forms
from .models import Post
from .models import Student, Group



class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text',)


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('name', 'card_number', 'date_of_birth', 'student_group') #'date_of_birth', , 'student_group'


class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ('title', 'head')