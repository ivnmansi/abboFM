from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        # permission to GET, HEAD or OPTIONS
        if request.method in SAFE_METHODS:
            return True
        
        # PATCH, PUT, DELETE just for owner
        return obj.user == request.user