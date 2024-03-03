"""
URL configuration for digi_sailor project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from sailor import views
from users import views as user_views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # path("",views.home,name ='sailor-home'),
    path("about/",views.about,name ='sailor-about'),
    path("user/<str:username>",views.UserPostListView.as_view(),name ='sailor-post'),
    path("",views.PostListView.as_view(),name ='sailor-home'),
    path("post/<int:pk>/",views.PostDetailView.as_view(),name ='sailor-detail'),
    path("post/new/",views.PostCreateView.as_view(),name ='sailor-create'),
    path("post/<int:pk>/update/",views.PostUpdateView.as_view(),name ='sailor-update'),
    path("post/<int:pk>/delete/",views.PostDeleteView.as_view(),name ='sailor-delete'),

    path('register/', user_views.register, name='register'),
    path('login/',auth_views.LoginView.as_view(template_name='users/login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='users/logout.html'),name='logout'),
    path('profile/',user_views.profile,name='profile'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)