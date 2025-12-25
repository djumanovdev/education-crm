from django.urls import path

from .views import StudentsView, StudentDeleteView, StudentsListView


urlpatterns = [
    path("students/", StudentsView.as_view()),
    path("students/list/", StudentsListView.as_view()),
    path("students/<int:student_id>/", StudentDeleteView.as_view()),
]
