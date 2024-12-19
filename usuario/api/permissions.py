from rest_framework import permissions

class IsGerente(permissions.BasePermission):
    def has_permission(self, request, view):
<<<<<<< HEAD
        return request.user.groups.filter(name="Gerente").exists()
=======
        return request.user.groups.filter(name="Gerentes").exists()
>>>>>>> ce1a5a5 (test: Adicionando testes aos itens e usuários)
