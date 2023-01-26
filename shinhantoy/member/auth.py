from django.contrib.auth.hashers import check_password
from .models import Member

class MemberAuth:

    def authenticate(self, request, username=None, password=None, *args, **kwargs):
        if not username or not password:
            if request.user.is_authenticated: # 혹시 이미 로그인이 되어있다면
                return request.user

            return None

        try:
            member = Member.objects.get(username = username) #회원이 있는지 확인
        except Member.DoesNotExist: #없으면 보내버림.
            return None
        
        if check_password(password, member.password): 
            if member.status == '일반':
                return member # 로그인 성공

        return None

    def get_user(self, pk):
        try:
            member = Member.objects.get(pk=pk)
        except Member.DoesNotExist:
            return None

        return member if member.is_active and member.status == '일반' else None        