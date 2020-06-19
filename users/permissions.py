from rest_framework.permissions import BasePermission


class IsClient(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_client)


class IsConsultant(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_consultant and request.user.is_active)
