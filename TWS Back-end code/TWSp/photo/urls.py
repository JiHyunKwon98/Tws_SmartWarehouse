from django.urls import path
from photo import views
from photo.views import MainView, TemplateView

app_name = 'photo'
urlpatterns = [

    path('', views.CategoryLV.as_view(), name='index'),

    path('category', views.CategoryLV.as_view(), name='category_list'),

    path('category/<int:pk>/', views.CategoryDV.as_view(), name='category_detail'),

    path('product/<int:pk>/', views.ProductDV.as_view(), name='product_detail'),

    path('order/<int:pk>/', views.OrderDV.as_view(), name='order_detail'),

    path('main/out/', views.out, name='out'),

    path('order', views.OrderLV.as_view(), name='order_list'),

    path('input_product', views.Input_Product, name='input_product'),

    path('order_product', views.Order_Product, name='order_product'),

    path('main', MainView.as_view(), name='main'),

    path('main/category/add/', views.CategoryProductCV.as_view(), name='category_add'),

    path('main/product/add/', views.ProductCV.as_view(), name='product_add'),

    path('main/order/add/', views.OrderCV.as_view(), name='order_add'),

    path('main/product/change/', views.ProductChangeLV.as_view(), name='product_change'),

    path('main/product/control/', views.ProductControlLV.as_view(), name='product_control'),

    path('main/product/real/', views.ProductRealLV.as_view(), name='product_real'),

    path('main/product/<int:pk>/delete/', views.ProductDelV.as_view(), name='product_delete'),

    path('main/order/<int:pk>/delete/', views.OrderDelV.as_view(), name='order_delete'),

    path('main/face/', views.face, name='face'),
    path('main/face/<int:pk>/delete/', views.FaceDelV.as_view(), name='face_delete'),



]