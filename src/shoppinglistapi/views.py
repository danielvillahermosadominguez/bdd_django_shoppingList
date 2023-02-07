import pinject
from rest_framework import status
from http import HTTPStatus
from rest_framework.response import Response
from rest_framework.views import APIView

from shoppinglistapi.di_configuration import BindingSpec
from shoppinglistapi.shoppinglist.application.shoppinglist_appserv import \
    ShoppingListAppServ

from .serializers import ShoppingListSerializer

OBJ_GRAPH = pinject.new_object_graph(
    modules=None, binding_specs=[BindingSpec()])
OK_MESSAGE = "OK"

class HealthCheck(APIView):
    def get(self, request, format=None):
        return Response(OK_MESSAGE, status.HTTP_200_OK)


class Info(APIView):
    def get(self, request, format=None):
        return Response("Welcome to the shoppig list api", status.HTTP_200_OK)


class ShoppingListView(APIView):
    OPTION_TAG = "option"
    OPTION_VALUE_RESET = "reset"
    NO_VALID_OPTION_MSG = "option parameter '%s' not valid."

    def get(self, request, format=None):
        serv = OBJ_GRAPH.provide(ShoppingListAppServ)
        user = request.user.get_username()
        sl = serv.get(user)
        serializer = ShoppingListSerializer(sl)
        return Response(serializer.data, status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        item = args[0]
        user = request.user.get_username()
        serv = OBJ_GRAPH.provide(ShoppingListAppServ)
        serv.add(item, user)
        return Response(OK_MESSAGE, status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        message = OK_MESSAGE
        serv = OBJ_GRAPH.provide(ShoppingListAppServ)
        user = request.user.get_username()
        if(len(args) == 0):
            serv.delete_all(user)
            return Response(message, status.HTTP_200_OK)

        result = status.HTTP_200_OK
        item = args[0]
        quantity = int(args[1])
        try:
            serv.delete(item, quantity, user)
        except Exception as error:
            result = status.HTTP_406_NOT_ACCEPTABLE
            message = error.message

        return Response(message, result)

    def put(self, request, *args, **kwargs):
        
        if(self.OPTION_TAG in request.POST):
            return self._updateItem_options(request)
            
        olditem = args[0]
        newitem = args[1]
        result = self._updateItem(request, olditem, newitem)
        return result

    def _updateItem_options(self, request):
        option = request.POST[self.OPTION_TAG]
        if(option == self.OPTION_VALUE_RESET):
            return self._resetItems(request)
        else:
            return Response(self.NO_VALID_OPTION_MSG % option, status.HTTP_404_NOT_FOUND)

    def _resetItems(self, request):
        user = request.user.get_username()
        serv = OBJ_GRAPH.provide(ShoppingListAppServ)
        message = OK_MESSAGE
        result = status.HTTP_200_OK
        serv.reset(user)
        return Response(message, result)

    def _updateItem(self, request, olditem, newitem):
        message = OK_MESSAGE
        result = status.HTTP_200_OK
        user = request.user.get_username()
        serv = OBJ_GRAPH.provide(ShoppingListAppServ)
        try:
            serv.change(olditem, newitem, user)
        except Exception as error:
            result = status.HTTP_204_NO_CONTENT
            message = error.message
        return Response(message, result)
