from rest_framework import pagination
from rest_framework.exceptions import PermissionDenied
from rest_framework.response import Response


class LimitOffsetPagination(pagination.LimitOffsetPagination):
    def get_paginated_response(self, data):
        return Response({
            'state' : {
                'next_offset': self.get_next_offset(),
                'prev_offset': self.get_prev_offset(),
                'limit': self.limit,
                'total': self.count
            },
            'results': data,
        })

    def get_next_offset(self):
        return self.offset + self.limit

    def get_prev_offset(self):
        prev_offset = self.offset - self.limit
        if self.offset == 0:
            return None
        elif prev_offset < 0:
            return 0
        else:
            return prev_offset


class CheckIfSuperUser:

    def check_if_superuser(self, request, raise_error=True):
        if request.user.is_superuser or request.user.is_admin:
            return True

        if raise_error:
            raise PermissionDenied
        else:
            return False
