from rest_framework import pagination


class AdmissionsPaginator(pagination.PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    page_query_param = 'p'
    
class AdmissionsDetailsPaginator(pagination.PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    page_query_param = 'p'