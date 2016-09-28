from rest_framework import pagination
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

