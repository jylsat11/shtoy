from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.contrib.auth.hashers import check_password, make_password
#serializer 사용위해 쓰는 것.
from rest_framework import mixins
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .serializers import MemberSerializer
from .models import Member

# 회원 가입
class MemberRegisterView(
    mixins.CreateModelMixin,
    generics.GenericAPIView
):
    #JSON 생성을 위해 serlializer 불러옴
    serializer_class = MemberSerializer

    def post(self, request, *args, **kwargs):
        
        return self.create(request,args,kwargs)

class MemberChangePasswordView(APIView):

    permission_classes = [IsAuthenticated] #로그인한 사용자만 아래 동작을 할 수 있다.

    def put(self, request, *args, **kwargs):
        # username = request.data.get('username') : 이미 로그인한상태이므로 필요 없다.
        current = request.data.get('current')
        password1 = request.data.get('password1')
        password2 = request.data.get('password2')

        if password1 != password2:
            return Response({
                'detail': 'Wrong new passwords',
            }, status=status.HTTP_400_BAD_REQUEST)

        # if not Member.objects.filter(username=username).exists(): #이미 로그인한 상태라 필요 없음.
        #     return Response({
        #         'detail':'No account',
        #     }, status = status.HTTP_404_NOT_FOUND)

        # member = Member.objects.get(username=username)    #이미 로그인한 상태라 필요 없음.

        member = request.user
        if not check_password(current, member.password):
            return Response({
                'detail':'Wrong password',
            }, status = status.HTTP_400_BAD_REQUEST)

        member.password = make_password(password1)
        member.save()

        return Response(status=status.HTTP_200_OK)