from django.urls import path, include
from . import views


urlpatterns = [
    path(r'', views.index, name='index'),
    # path(r'', views.post_list, name='post_list'),
    path(r'',views.mail_send,name='mail_send'),
    path(r'post/(?P<pk>\d+)/$',views.post_detail,name='post_detail'),
    # path('',views.post_detail,name='post_detail'),
    path(r'post/new/$', views.post_new, name='post_new'),
    path(r'post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    path(r'drafts/$', views.post_draft_list, name='post_draft_list'),
    path(r'post/(?P<pk>\d+)/publish/$', views.post_publish, name='post_publish'),
    path(r'post/(?P<pk>\d+)/remove/$', views.post_remove, name='post_remove'),
    path(r'post/(?P<pk>\d+)/comment/$', views.add_comment_to_post, name='add_comment_to_post'),
    path(r'comment/(?P<pk>\d+)/approve/$', views.comment_approve, name='comment_approve'),
    path(r'comment/(?P<pk>\d+)/remove/$', views.comment_remove, name='comment_remove'),

]
