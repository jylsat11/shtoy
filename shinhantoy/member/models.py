from django.db import models
from django.contrib.auth.models import AbstractUser

class Member(AbstractUser):
    tel = models.CharField(max_length=32, null=True, blank=True, verbose_name = "연락처")
    status = models.CharField(max_length=16, default = "일반",
        choices = (
        ('일반','일반'),
        ('탈퇴','탈퇴'),
        ('휴면','휴면'),
        )
    )

    REQUIRED_FIELDS = ["tel"]

    class Meta:
        db_table = 'shinhan_member'
        verbose_name = '회원'
        verbose_name_plural = '회원'
        
# Create your models here.

#댓글 모델 만들기
#댓글에는 사용자 외래키, 상품 외래키, 댓글 내용, tstamp
#관리자 페이지에 등록해서
#관리자 페이지 통해서 댓글 3개 작성.