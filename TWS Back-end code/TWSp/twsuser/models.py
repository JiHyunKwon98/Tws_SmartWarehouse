from django.db import models

class twsuser(models.Model):  # 장고에서 제공하는 models.Model를 상속받아야한다.
    username = models.CharField('사용자 이름', max_length=32, null=True)
    id = models.CharField('사용자 아이디', max_length=32, primary_key=True)
    pw = models.CharField('사용자 비밀번호', max_length=64, null=True)
    company = models.CharField('업체명', max_length=128, null=True)
    address = models.CharField('업체주소', max_length=256, null=True)
    call = models.CharField('업체번호', max_length=128, blank=True, null=True)
    email = models.CharField('사용자 이메일', max_length=128, blank=True, null=True)

    class Meta:  # 메타 클래스를 이용하여 테이블명 지정
        db_table = 'twsuser'