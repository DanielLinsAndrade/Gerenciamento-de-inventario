from rest_framework import permissions

class IsGerente(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name="Gerentes").exists()
