from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required

app_name = 'profile'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('add_post/', views.add_post, name='add_post'),
    path('add_post/<int:year>/<int:month>/<int:day>/<slug:post>/', views.PostEditView.as_view(), name='post_edit'),
    path('', include('django.contrib.auth.urls')),
]