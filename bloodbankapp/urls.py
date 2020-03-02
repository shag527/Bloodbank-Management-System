from django.urls import path,re_path
from .import views
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns=[
path('home/',views.home,name='home'),
path('admin_login/',views.adminlogin,name='admin_login'),
path('about_us/',views.aboutus,name='about_us'),
path('eligibility/',views.eligibility,name='eligibility'),
path('donor/',views.donor,name='donor'),
path('sign_in/',views.signin,name='sign_in'),
path('t_c/',views.tandc,name='t_c'),
re_path(r'^login/$',LoginView.as_view(template_name='login.html',redirect_field_name='next'),name='login'),
re_path(r'^logout/$',LogoutView.as_view(next_page="home"),name='logout'),
path('profile/',views.profile,name='profile'),
path('profile/favourite/',views.favourite,name='favourite'),
path('seek/',views.requests,name='seek'),
re_path(r'^update/$',views.update,name="update"),
re_path(r'^delete/$',views.delete,name="delete"),
path('profile/edit',views.profile_edit,name='profile_edit'),
path('password/',views.change_password,name='change_password'),
re_path(r'^contact/$',views.contact_us,name='contact'),
re_path(r'^profile/(?P<pk>[0-9]+)$',views.detail,name='detail'),
re_path(r'^donor/(?P<pk>[0-9]+)$',views.detail,name='detail'),
]