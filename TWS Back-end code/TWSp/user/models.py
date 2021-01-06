from django.db import models

class User(models.Model):
    username = models.CharField('사용자 이름', max_length=32)
    id = models.CharField('사용자 아이디', max_length=32, primary_key=True)
    pw = models.CharField('사용자 비밀번호', max_length=64)
    pwc = models.CharField('비밀번호 확인', max_length=64)
    company = models.CharField('업체명', max_length=128)
    address = models.CharField('업체주소', max_length=256)
    call = models.CharField('업체번호', max_length=128, blank=True)
    email = models.CharField('사용자 이메일', max_length=128, blank=True)

    class Meta:  # 메타 클래스를 이용하여 테이블명 지정
        db_table = 'user'

#def __str__(self):
#    return self.username
