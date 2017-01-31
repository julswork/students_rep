# from django.conf.urls import url
# from . import views
#
# urlpatterns = [
#     # url(r'^$', views.post_list, name='post_list'),
#     # url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
#     # url(r'^post/new/$', views.post_new, name='post_new'),
#     # url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
#
#
# ]


from django.conf.urls import include, url
from django.contrib import admin


from .views import (
    login_user, create_mail_reminder, self_mail_reminder_by_id, delete_mail_reminder
)


urlpatterns = [
    url(r'^$', include(admin.site.urls)),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^login$', login_user, name='login'),

    url(r'^reminder/$', create_mail_reminder), # add employeemailreminder or return all employeemailreminders for current employee
    url(r'^reminder/employee/(?P<employee_id>\d+)/$', create_mail_reminder), # add employeemailreminder or return all employeemailreminder for current employee
    url(r'^reminder/(?P<employeemailreminder_id>\d+)/$', self_mail_reminder_by_id), # update employeemailreminder or get by id
    url(r'^reminder/(?P<employeemailreminder_id>\d+)/delete/$', delete_mail_reminder) # delete employeemailreminder or get by id
]

