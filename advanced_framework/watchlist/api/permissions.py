from rest_framework import permissions


# Custom Permissions
class AdminOrReadOnly(permissions.IsAdminUser):

    def has_permission(self, request, view):
        # Check permissions for read-only request
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            # Checks if user is staff/admin
            return bool(request.user and request.user.is_staff)


class ReviewUserOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        # SAFE_METHODS is a tuple of safe or data retrieving methods
        if request.method in permissions.SAFE_METHODS:
            # Check permissions for read-only request
            return True
        else:
            return obj.review_user == request.user
