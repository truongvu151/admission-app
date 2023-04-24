from rest_framework import pagination


class AdmissionPaginator(pagination.PageNumberPagination):
    page_size = 2