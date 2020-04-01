from django.urls import path

from . import views

urlpatterns = [
    path('', views.index_goods, name='index_goods_url'),
    path('category/<str:slug>/', views.category_detail, name='category_detail_url'),
    # path('product/<str:slug>/', views.product_detail, name='product_detail_url'),
    path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail_url'),
    path('delivery/', views.delivery_detail, name='delivery_detail_url'),
    path('contacts/', views.contacts_detail, name='contacts_detail_url')
]
