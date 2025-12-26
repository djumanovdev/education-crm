from django.urls import path

from .views import StudentsView, StudentDeleteView, StudentListView


urlpatterns = [
    path("students/", StudentsView.as_view()),
    path("students/<int:student_id>/delete/", StudentDeleteView.as_view()),
    path("students/list/", StudentListView.as_view(), name="student-list"),
    
]
