from rest_framework.permissions import BasePermission
from rest_framework.exceptions import PermissionDenied


class IsClient(BasePermission):
    def has_permission(self, request, view):
        try:
            request.user.is_client
        except:
            raise PermissionDenied
        return bool(request.user and request.user.is_client)


class IsConsultant(BasePermission):
    def has_permission(self, request, view):
        try:
            request.user.is_consultant
        except:
            raise PermissionDenied
        return bool(request.user and request.user.is_consultant and request.user.is_active)
