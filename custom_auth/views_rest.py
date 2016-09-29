import json

from rest_framework import viewsets
from rest_framework.decorators import list_route
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAuthenticated

from custom_auth.models import User
from custom_auth.serializers import UserSerializer
from rest_framework.response import Response


class UserViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated, )

    def list(self, request, *args, **kwargs):
        if request.user.is_superuser or request.user.is_admin:
            return super(UserViewSet, self).list(request, *args, **kwargs)
        else:
            raise PermissionDenied

    def retrieve(self, request, *args, **kwargs):
        if request.user.is_superuser or request.user.is_admin:
            return super(UserViewSet, self).retrieve(request, *args, **kwargs)
        else:
            raise PermissionDenied

    def update(self, request, *args, **kwargs):
        if request.user.is_superuser or request.user.is_admin:
            return super(UserViewSet, self).update(request, *args, **kwargs)
        else:
            raise PermissionDenied

    def destroy(self, request, *args, **kwargs):
        if request.user.is_superuser or request.user.is_admin:
            return super(UserViewSet, self).destroy(request, *args, **kwargs)
        else:
            raise PermissionDenied

    def create(self, request, *args, **kwargs):
        if request.user.is_superuser or request.user.is_admin:
            return super(UserViewSet, self).create(request, *args, **kwargs)
        else:
            raise PermissionDenied

    @list_route(methods=['get'])
    def current_user(self, request, *args, **kwargs):
        pk = request.user.id
        instance = self.queryset.get(pk=pk)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

