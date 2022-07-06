import json
from django.forms.models import model_to_dict
from django.http import JsonResponse, HttpResponse

from rest_framework.response import Response
from rest_framework.decorators import api_view

from products.models import Product
from products.serializers import ProductSerializer

@api_view(["POST"])
# Create your views here.
def api_home(request, *args, **kwargs):

    """
    DRF API VIEW
    """
    data = request.data
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        # instance = serializer.save()
        # instance = form.save()
        print(serializer.data)
        return Response(serializer.data)
    return Response({"invalid": "not good data"}, status=400)











    # if model_data:
    #     data['id'] = model_data.id
    #     data['title'] = model_data.title
    #     data['content'] = model_data.content
    #     data['price'] = model_data.price
    #     # model instance (model_data)
    #     # turn python to dict
    #     # return JSON to my client

    # request -> Http request -> Django
    # request.body
    print(request.GET) # url query param
    print(request.POST) # url query param

    body = request.body # byte string 
    try:
        data = json.loads(body) # string of JSON dara -> Python Dict
    except:
        pass
    print(data)
    # data['params'] = dict(request.GET)
    # data['headers'] = dict(request.headers) # request.META -> 
    # data['content_type'] = request.content_type
    # data['params'] = dict(request.POST)
    # return JsonResponse({"message": "Hi there this is your Django API Response!!"})
    # return JsonResponse(data)