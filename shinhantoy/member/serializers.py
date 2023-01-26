from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import Member

class MemberSerializer(serializers.ModelSerializer):

    def validate_password(self,value):
        #유효성 검사가 끝난 값을 반환.
        if len(value) <8:
            raise serializers.ValidationError('Too short password')


        return make_password(value)

    class Meta: #생성, 반환 결과값 설정 ('fields')
        model = Member
        fields = ('id','username','tel','password')
        extra_kwargs = {
            'id' :{
                'read_only':True,   
            },
            'password': {
                'write_only': True
            }
        }