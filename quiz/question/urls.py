from django.urls import path

from . import views


app_name = 'question'

urlpatterns = [
    path('create/<str:question_type>/',
        views.QuestionCreateView.as_view(),
        name='create'
    ),
    path('<int:question_id>/update/',
        views.QuestionUpdateView.as_view(),
        name='update'
    ),
    path('<int:question_id>/delete/',
        views.QuestionDeleteView.as_view(),
        name='delete'
    ),
]
