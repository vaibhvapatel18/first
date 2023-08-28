from rest_framework.pagination import PageNumberPagination

class Page(PageNumberPagination):
    page = 5
    page_query_param = 'p'
    page_size_query_param = 'records'
    max_page_size = 7
    last_page_strings = 'end'