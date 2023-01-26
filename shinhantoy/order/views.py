from rest_framework import generics, mixins
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .serializers import (
    OrderSerializer, 
    CommentSerializer,
    CommentCreateSerializer
)
from .models import Order, Comment

# Create your views here.

class OrderListView(
    mixins.ListModelMixin,
    generics.GenericAPIView
):

    serializer_class = OrderSerializer

    def get_queryset(self):
        return Order.objects.all().order_by('-id')

    def get(self, request, *args, **kwargs):
        return self.list(request, args, kwargs)

class OrderDetailView(
    mixins.RetrieveModelMixin,
    generics.GenericAPIView
):
    serializer_class = OrderSerializer

    def get_queryset(self):
        return Order.objects.all().order_by('id')

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, args, kwargs)

class CommentListView(
    mixins.ListModelMixin, 
    generics.GenericAPIView
):
    #:generics.GenericAPIview: 내가 사용할 기능들에 대한 기본적인 뼈대를 만들어주는 것.
    serializer_class = CommentSerializer

    def get_queryset(self):
        order_id = self.kwargs.get('order_id')
        if order_id:
            return Comment.objects.filter(order_id = order_id)\
                .select_related('member','order') \
                .order_by('-id')

        return Comment.objects.none()

  
    def get(self, request, *args, **kwargs):
        # Queryset : 가져오고
        # Serialize : 처리해서
        # return Response : JSON 만들어서 전달
        return self.list(request,args,kwargs) #mixins.ListModelMixin에 있는 list함수 사용

class CommentCreateView(
    mixins.CreateModelMixin,
    generics.GenericAPIView
):
    permission_classes = [IsAuthenticated]
    serializer_class = CommentCreateSerializer

    def get_queryset(self):
        return Comment.objects.all()

    def post(self, request, *args, **kwargs):
        return self.create(request,args,kwargs)