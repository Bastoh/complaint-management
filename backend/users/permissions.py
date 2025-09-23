from rest_framework.permissions import BasePermission
from .models import User


class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        return bool(
            user and user.is_authenticated and (
                user.role == User.Roles.ADMIN or user.is_superuser or user.is_staff
            )
        )


class IsHandler(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        return bool(
            user and user.is_authenticated and (
                user.role in [User.Roles.HANDLER, User.Roles.ADMIN]
                or user.is_superuser or user.is_staff
            )
        )


class IsComplainant(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        return bool(
            user and user.is_authenticated and (
                user.role in [User.Roles.COMPLAINANT, User.Roles.ADMIN]
                or user.is_superuser or user.is_staff
            )
        )


class CanViewAndEditComplaint(BasePermission):
	def has_object_permission(self, request, view, obj):
			user = request.user

			if not user or not user.is_authenticated:
				return False

			if user.role == user.Roles.ADMIN or user.is_superuser or user.is_staff:
				return True

			if user.role == user.Roles.HANDLER:
				return obj.handler == user

			if user.role == user.Roles.COMPLAINANT:
				return obj.complainant == user

			return False

class CanViewAndEditHandler(BasePermission):
	def has_object_permission(self, request, view, obj):
		user = request.user

		if not user or not user.is_authenticated:
			return False

		if user.role == user.Roles.ADMIN or user.is_superuser or user.is_staff:
			return True
