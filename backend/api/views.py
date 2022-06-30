import json
from django.forms.models import model_to_dict

from rest_framework.decorators import api_view
from rest_framework.response import Response

from products.models import Product
from products.serializers import ProductSerializer

@api_view(["POST"])
def api_home(request, *args, **kwargs):
    data = request.data
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        # instance = serializer.save()
        print(data)
        return Response(serializer.data)
    # instance = Product.objects.all().order_by("?").first()
    # if instance:
    #     data = ProductSerializer(instance).data
    # print(data)
    # return Response(data)
    return Response({"invalid": "not good data"}, status=400)