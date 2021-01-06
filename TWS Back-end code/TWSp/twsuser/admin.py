from django.contrib import admin
from .models import *

# Register your models here.

class twsuserAdmin(admin.ModelAdmin) :
    list_display = ('username', 'id', 'pw', 'company', 'address', 'call', 'email')


admin.site.register(twsuser, twsuserAdmin) #site에 등록