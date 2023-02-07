from rest_framework import serializers
from shoppinglistapi.shoppinglist.domain.shoppinglist import  ShoppingList

class ShoppingListSerializer(serializers.Serializer):
    _user = serializers.CharField(required=True,allow_blank= False)
    _dict = serializers.DictField() 

    def create(self, validated_data):
        return ShoppingList(**validated_data)
