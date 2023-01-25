from rest_framework import generics, mixins
from .models import Order
from .serializers import OrderSerializer

from .paginations import OrderLargePagination

class OrderListView(
    mixins.ListModelMixin, 
    generics.GenericAPIView
):
    #:generics.GenericAPIview: 내가 사용할 기능들에 대한 기본적인 뼈대를 만들어주는 것.
    serializer_class = OrderSerializer

    pagination_class = OrderLargePagination

    def get_queryset(self):
        orders = Order.objects.all()
        #인자값을 받아서 filter할 수 있게 하자!

        return orders.order_by('ord_id')

    def get(self, request, *args, **kwargs):
        # Queryset : 가져오고
        # Serialize : 처리해서
        # return Response : JSON 만들어서 전달
 
        return self.list(request,args,kwargs)