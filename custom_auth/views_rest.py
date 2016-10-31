import json

from django.utils.translation import ugettext_lazy as _

from rest_framework import viewsets
from rest_framework.decorators import list_route
from rest_framework.exceptions import PermissionDenied, NotAcceptable, MethodNotAllowed, ValidationError
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView


from custom_auth.models import User
from custom_auth.serializers import UserSerializer, UserRegistrationSerializer,PasswordChangeSerializer , PasswordResetConfirmSerializer, PasswordResetSerializer




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
    def current_user(self, request):
        pk = request.user.id
        instance = self.queryset.get(pk=pk)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)



class UserRegisterViewSet(viewsets.ViewSet):

    permission_classes = (AllowAny, )
    serializer_class = UserSerializer

    def create(self, request):
        if request.method.lower() == 'post':
            if request.user.is_anonymous():
                request.data['groups'] = []
                serializer = UserRegistrationSerializer(data=request.data)

                if serializer.is_valid(raise_exception=True):
                    if len(User.objects.filter(email=serializer.data['email'])):
                        raise ValidationError({"email": "This email has been used already."})
                    user = serializer.create(serializer.validated_data)
                    user.groups = []
                    user.set_password(serializer.data['password'])
                    user.is_active = True
                    user.save()
                    serializer = UserSerializer(user)

                    return Response(serializer.data)
                else:
                    raise NotAcceptable()
            else:
                raise PermissionDenied('You are already registered.')
        else:
            raise MethodNotAllowed(request.method)

class PasswordResetViewSet(GenericAPIView):

    """
    Calls Django Auth PasswordResetForm save method.

    Accepts the following POST parameters: email
    Returns the success/fail message.
    """

    serializer_class = PasswordResetSerializer
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            if len(User.objects.filter(email =  serializer.data['email'])):
                serializer.save()
                return Response({"success": _("Password reset e-mail has been sent.")})
            else:
                return Response({"Failed": _("The email is not in our system.")})
        else:
            raise NotAcceptable()


class PasswordResetConfirmViewSet(GenericAPIView):
    """
    Password reset e-mail link is confirmed, therefore this resets the user's password.

    Accepts the following POST parameters: new_password1, new_password2
    Accepts the following Django URL arguments: token, uid
    Returns the success/fail message.
    """

    serializer_class = PasswordResetConfirmSerializer
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"success": _("Password has been reset with the new password.")})


class PasswordChangeViewSet(GenericAPIView):
    """
    Calls Django Auth SetPasswordForm save method.

    Accepts the following POST parameters: new_password1, new_password2
    Returns the success/fail message.
    """

    serializer_class = PasswordChangeSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"success": _("New password has been saved.")})



