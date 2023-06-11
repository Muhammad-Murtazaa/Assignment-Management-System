from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect


def index(request):
    return redirect('user:login')

urlpatterns = [
    path('', index, name='index'),
    path('admin/', admin.site.urls),
    path('auth/', include('user.urls')),
    path('course/', include('course.urls')),
    path('course/<course_id>/quiz/', include('quiz.urls')),
]
