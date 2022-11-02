from rest_framework.views import APIView
from rest_framework.response import Response
#from rest_framework.decorators import api_view, authentication_classes, permission_classes Para permissões e autenticação

from order.models import Order
from order.api.serializers import MyOrderSerializer

class OrdersList(APIView):
    #authentication_classes = [authentication.TokenAuthentication]
    #permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        orders = Order.objects.filter(user=request.user)
        serializer = MyOrderSerializer(orders, many=True)

        return Response(serializer.data)
