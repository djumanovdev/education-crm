from rest_framework.permissions import BasePermission


class IsAdmin(BasePermission):
    message = 'siz amdin emassiz'

    def has_permission(self, request, view):
        return request.user and request.user.is_admin
    
class IsTeacher(BasePermission):
    message = 'siz Teacher emassiz'

    def has_permission(self, request, view):
        return request.user and request.user.is_manager
    
class IsStudent(BasePermission):
    message = 'siz user emassiz'

    def has_permission(self, request, view):
        return request.user and request.user.is_user

