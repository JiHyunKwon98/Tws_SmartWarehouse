from django.db import models
from django.urls import reverse

from photo.fields import ThumbnailImageField

class Category (models.Model):
    name = models.CharField('카테고리', max_length=50)
    description = models.CharField('설명', max_length=100, blank=True)

    class Meta:  # 정렬 객체리스트 정렬 기준 name
        ordering = ('name',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('photo:category_detail', args=(self.id,))


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    pname = models.CharField('제품명', max_length=32)
    pcost = models.CharField('가격', max_length=64)
    pcontent = models.TextField('상세설명', blank=True)
    pimage = models.ImageField('이미지', upload_to='Sorlphoto/%Y')
    psize = models.CharField('크기', max_length=64, blank=True)
    pweight = models.CharField('무게', max_length=64, blank=True)
    pship = models.CharField('배송방법', max_length=64)
    pstore = models.CharField('보관장소', max_length=64)
    upload_dt = models.DateTimeField('upload date', auto_now_add=True)
    put = models.IntegerField('입고수량', default=0)
    putdate = models.CharField('입고날짜', max_length=128, blank=True)
    stock = models.IntegerField('재고수량', default=0)
    release = models.IntegerField('출고수량', default=0)
    rfid = models.CharField('RFID', max_length=256, blank=True)

    class Meta:  # 정렬 객체리스트 정렬 기준 pname
        ordering = ('pname',)

    def __str__(self):
        return self.pname

    def get_absolute_url(self):
        return reverse('photo:product_detail', args=(self.id,))


class Order(models.Model):
    product = models.ManyToManyField('Product', through='Order_Product')
    oname = models.CharField('주문자 이름', max_length=32)
    ocall = models.CharField('연락처', max_length=64)
    oaddress = models.CharField('주소', max_length=256)
    oemail = models.CharField('이메일', max_length=128, blank=True)
    omemo = models.TextField('배송메모', blank=True)
    no = models.IntegerField('출고번호', null=True, blank=True)

    class Meta:  # 정렬 객체리스트 정렬 기준 oname
        ordering = ('oname',)

    def __str__(self):
        return self.oname

    def get_absolute_url(self):
        return reverse('photo:order_detail', args=(self.id,))

class Order_Product(models.Model):
     product = models.ForeignKey(Product, on_delete=models.CASCADE)
     order = models.ForeignKey(Order, on_delete=models.CASCADE)
     no = models.IntegerField('출고번호', null=True, blank=True)

class Face(models.Model):
    fname = models.TextField('face 이름', max_length=32)
    fimage = models.ImageField('face 이미지', upload_to='Sorlface/%Y')

    class Meta:
        db_table = 'Face'








