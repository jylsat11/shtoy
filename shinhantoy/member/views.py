from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

#serializer 사용위해 쓰는 것.
from rest_framework import mixins
from rest_framework import generics
from .serializers import MemberSerializer

# 회원 가입
class MemberRegisterView(
    mixins.CreateModelMixin,
    generics.GenericAPIView
):
    #JSON 생성을 위해 serlializer 불러옴
    serializer_class = MemberSerializer

    def post(self, request, *args, **kwargs):
        
        return self.create(request,args,kwargs)
