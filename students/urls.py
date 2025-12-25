from django.urls import path

from .views import StudentsView, StudentsDetailView


urlpatterns = [
    path("students/", StudentsView.as_view()),
    path("students/<int:pk>/", StudentsDetailView.as_view()),
]
