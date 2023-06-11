from django.urls import path, include

from . import views


app_name = 'quiz'

urlpatterns = [
    path('',
        views.QuizListView.as_view(),
        name='list'
    ),
    path('<int:quiz_id>/',
        views.QuizDetailView.as_view(),
        name='detail'
    ),
    path('create/',
        views.QuizCreateView.as_view(),
        name='create'
    ),
    path('<int:quiz_id>/delete/',
        views.QuizDeleteView.as_view(),
        name='delete'
    ),
    path('<int:quiz_id>/submit/',
        views.QuizSubmitView.as_view(),
        name='submit'
    ),
    path('<int:quiz_id>/question/',
        include('quiz.question.urls'))
]
