from rest_framework import serializers

from .models import Order

class OrderSerializer(serializers.ModelSerializer):
    order_ord_ymd = serializers.SerializerMethodField()
    order_ord_no = serializers.SerializerMethodField()
    
    #method를 만들면 함수를 만들어야 한다.
    def get_order_ord_ymd(self,obj):
        return obj.order.ord_ymd

    def get_order_ord_no(self,obj):
        return obj.order.ord_no

   
    class Meta:
        model = Order
        fields = '__all__' # 가져올 데이터 종류 입력 ['id','price'] 이렇게 할 수도 있다.
