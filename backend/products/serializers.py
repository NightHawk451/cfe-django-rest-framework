from pickletools import read_floatnl
from rest_framework import serializers
from rest_framework.reverse import reverse

from api.serializers import UserPublicSerializer
from .models import Product
from .validators import validate_title_no_hello, unique_product_title



class ProductInlineSerializer(serializers.Serializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='product-detail',
        lookup_field='pk',
        read_only=True
        )
    title = serializers.CharField(read_only=True)


class ProductSerializer(serializers.ModelSerializer):
    owner = UserPublicSerializer(source='user', read_only=True)
    edit_url = serializers.SerializerMethodField(read_only=True)
    url = serializers.HyperlinkedIdentityField(
        view_name='product-detail',
        lookup_field='pk',
        )
    title = serializers.CharField(validators=[validate_title_no_hello, unique_product_title]) 
    body = serializers.CharField(source='content')
    class Meta:
        model = Product
        fields = [
            'owner',
            'url',
            'edit_url',
            'pk',
            'title',
            'body',
            'price',
            'sale_price',
            'public',
            'path',
        ]

    def create(self, validated_data):
        # return Product.objects.create(**validated_data)
        # email = validated_data.pop('email')
        obj = super().create(validated_data)
        # print(email, obj)
        return obj

    def update(self, instance, validated_data):
        # email = validated_data.pop('email')
        return super().update(instance, validated_data)

    def get_edit_url(self, obj):
        request = self.context.get('request')
        if request is None:
            return None
        return reverse("product-edit", kwargs={"pk": obj.pk}, request=request)
