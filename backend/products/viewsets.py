from rest_framework import mixins, viewsets

from .models import Product
from .serializers import ProductSerializer

class ProductViewset(viewsets.ModelViewSet):
    '''
    get -> list -> Queryset
    get -> retrieve -> Product Instance Detail View
    post -> create -> New Instance
    put -> update
    patch -> Partial Update
    delete -> destrpy
    '''
    
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk' # default 

class ProductGenericViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet):
    '''
    get -> list -> Queryset
    get -> retrieve -> Product Instance Detail View
    '''
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk' # default 


# product_list_view = ProductGenericViewSet.as_view({"get":'list'})
# product_detail_view = ProductGenericViewSet.as_view({"get":'retrieve'})