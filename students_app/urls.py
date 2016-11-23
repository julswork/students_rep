from django.conf.urls import url
from . import views

urlpatterns = [
    # url(r'^$', views.post_list, name='post_list'),
    # url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    # url(r'^post/new/$', views.post_new, name='post_new'),
    # url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),



    url(r'^$', views.group_list, name='group_list'),
    url(r'^group/(?P<pk>[0-9]+)/$', views.group_detail, name='group_detail'),
    url(r'^group/new/$', views.group_new, name='group_new'),
    url(r'^group/(?P<pk>[0-9]+)/edit/$', views.group_edit, name='group_edit'),


    url(r'^student/(?P<pk>[0-9]+)/$', views.student_detail, name='student_detail'),
    url(r'^student/new/$', views.student_new, name='student_new'),
    url(r'^student/(?P<pk>[0-9]+)/edit/$', views.student_edit, name='student_edit'),

    url(r'^student/delete/(?P<pk>[0-9]+)/(?P<id>[0-9]+)/$', views.group_student_delete),




    # url(r'^post/new/$', views.post_new, name='post_new'),
    # url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),

]