from rest_framework.pagination import PageNumberPagination

class CustomPageNumberPagination(PageNumberPagination):
    page_size = 10  # Nombre d'objets par page
    page_size_query_param = 'page_size'  # Permet à l'utilisateur de spécifier ?page_size=...
    max_page_size = 100
