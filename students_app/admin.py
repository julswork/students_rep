from django.contrib import admin

from django.contrib import admin
from .models import Post
from .models import Student, Group


admin.site.register(Post)

admin.site.register(Student)
admin.site.register(Group)
