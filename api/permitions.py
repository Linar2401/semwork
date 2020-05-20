from rest_framework import permissions


class MyCommentPermissions(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        # Allow get requests for all
        if request.method == 'GET':
            return True
        return bool(request.user and request.user.is_authenticated and request.user == obj.user)
