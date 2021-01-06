from django.views.generic import ListView, DetailView, TemplateView
from photo.models import Category, Product, Order, Face, Order_Product
from twsuser.models import twsuser
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from photo.forms import ProductInlineFormSet
import json
import datetime

class CategoryLV(ListView):
    model = Category

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = twsuser.objects.get()
        if self.request.POST:
            context['formset'] = user.company
        else:
            context['company'] = user.company
            context['address'] = user.address
            context['call'] = user.call
            context['email'] = user.email
        return context

class CategoryDV(DetailView):
    model = Category

class ProductDV(DetailView):
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category_list'] = Category.objects.all()
        return context


class OrderDV(DetailView):
    model = Product
    template_name = 'photo/order_detail.html'

class OrderLV(ListView):
    model = Order
    template_name = 'photo/order_list.html'


def Order_Product(request):
    store_list = Order.objects.all()
    context = {'store_list': store_list}
    store = request.POST.getlist('storeResult[]')


    for i in store:
        if i == "A1": #받아온 보관장소가 A1 일때
            a1 = Product.objects.get(pstore="A1") # 등록된 제품 중 보관장소가 A1 인 걸 불러옴
            if (a1.release == 0 and a1.stock == 1): # 조건 - > 출고수량이 0. 재고 수량이 1 일때만
                print(i)
                a1.release += 1  # 출고 +1 재고 -1 즉 이미 처리 된 주문은 계산이 중복해서 일어나지 않도록
                a1.stock -= 1
                a1.save()


        elif i == "A2":
            a2 = Product.objects.get(pstore="A2")
            if (a2.release == 0 and a2.stock == 1):
                print(i)
                a2.release+=1
                a2.stock-=1
                a2.save()

        elif i == "A3":
            a3 = Product.objects.get(pstore="A3")
            if (a3.release == 0 and a3.stock == 1):
                print(i)
                a3.release += 1
                a3.stock -= 1
                a3.save()

        elif i == "B1":
            b1 = Product.objects.get(pstore="B1")
            if (b1.release == 0 and b1.stock == 1):
                print(i)
                b1.release+=1
                b1.stock-=1
                b1.save()

        elif i == "B2":
            b2 = Product.objects.get(pstore="B2")
            if (b2.release == 0 and b2.stock == 1):
                print(i)
                b2.release+=1
                b2.stock-=1
                b2.save()

        elif i == "B3":
            b3 = Product.objects.get(pstore="B3")
            if (b3.release == 0 and b3.stock == 1):
                print(i)
                b3.release += 1
                b3.stock -= 1
                b3.save()

        elif i == "C1":
            c1 = Product.objects.get(pstore="C1")
            if (c1.release == 0 and c1.stock == 1):
                print(i)
                c1.release+= 1
                c1.stock-= 1
                c1.save()

        elif i == "C2":
            c2 = Product.objects.get(pstore="C2")
            if (c2.release == 0 and c2.stock == 1):
                print(i)
                c2.release += 1
                c2.stock -= 1
                c2.save()

        elif i == "C3":
            c3 = Product.objects.get(pstore="C3")
            if (c3.release == 0 and c3.stock == 1):
                print(i)
                c3.release += 1
                c3.stock -= 1
                c3.save()
        else:
            print(0)

    order = request.POST.getlist('orderResult[]')
    for num in order:
        bn = Order.objects.get(pk=num)
        bn.no = num
        bn.save()


    return render(request,'photo/order_product.html', context)

def Input_Product(request):
    product_list = Product.objects.all()
    context = {'product_list': product_list}
    product_id = request.POST.getlist('idResult[]')

    now = datetime.datetime.now()
    for ip in product_id:
        print(ip)
        pro = Product.objects.get(pk=ip)
        if (pro.put == 0 and pro.stock == 0):
            pro.put =+1
            pro.stock =+1
            pro.putdate = now.strftime('%Y-%m-%d %H:%M')
            pro.save()

    return render(request,'photo/input_product.html', context)

class MainView(TemplateView):
    template_name = 'main.html'


class ProductCV(CreateView):
    model = Product
    fields = ('category', 'pname', 'pcost', 'pcontent',
              'pimage', 'psize', 'pweight', 'pship', 'pstore')
    success_url = reverse_lazy('photo:product_change')

    def form_valid(self, form):

        return super().form_valid(form)


class OrderCV(CreateView):
    model = Order
    fields = ('product', 'oname', 'ocall', 'oaddress',
              'oemail', 'omemo')

    success_url = reverse_lazy('photo:index')

    def form_valid(self, form):
        return super().form_valid(form)


class CategoryProductCV(CreateView):
    model = Category
    fields = ('name', 'description')
    success_url = reverse_lazy('photo:product_add')


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['formset'] = ProductInlineFormSet(self.request.POST, self.request.FILES)
        else:
            context['formset'] = ProductInlineFormSet()
        return context

    def form_valid(self, form):
        return super().form_valid(form)

class ProductChangeLV(ListView):
    model = Product
    template_name = 'photo/product_change_list.html'

class ProductControlLV(ListView):
    model = Product
    template_name = 'photo/product_control.html'

class ProductRealLV(ListView):
    model = Product
    template_name = 'photo/product_real.html'

class ProductDelV(DeleteView):
    model = Product
    success_url = reverse_lazy('photo:product_change')

class OrderDelV(DeleteView):
    model = Order
    success_url = reverse_lazy('photo:order_list')

class FaceDelV(DeleteView):
    model = Face
    success_url = reverse_lazy('photo:face')

def face(request):
    if request.method == "GET":
        person_list = Face.objects.all()
        context = {'person_list': person_list}
        return render(request, 'photo/face.html', context)

    elif request.method == "POST":
        face = Face()
        face.fname = request.POST.get('fname', None)
        face.fimage = request.FILES.get('fimage', None)
        face.save()
        return render(request, 'photo/face.html')

def out(request):
    if request.method == "GET":
        return render(request, 'photo/out.html')
    elif request.method == "POST":
        no = request.POST.get('no', None)
        out = Order_Product.objects.filter(order_id=no)
        out.no = request.POST.get('no', None)
        for i in out:
            i.no = request.POST.get('no', None)
            i.save()
        return render(request, 'photo/out.html')








