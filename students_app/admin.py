from django.contrib import admin

from django.contrib import admin
from .models import Post
from .models import Student, Group


admin.site.register(Post)


class StudentInline(admin.TabularInline):
    model = Student
    extra = 3


class GroupAdmin(admin.ModelAdmin):
    inlines = [StudentInline,]


class GroupInline(admin.TabularInline):
    model = Group
    extra = 3


class StudentAdmin(admin.ModelAdmin):
    inlines = [GroupInline,]


admin.site.register(Group, GroupAdmin)
admin.site.register(Student, StudentAdmin)


