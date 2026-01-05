from django.urls import path

from .views import StudentsView, StudentDetailView


urlpatterns = [
    path("students/", StudentsView.as_view()),
    path("students/<int:pk>/", StudentDetailView.as_view()),
]
