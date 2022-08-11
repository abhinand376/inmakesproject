from django.urls import path
from . import views
app_name='ecommerceapp'

urlpatterns = [
    path('',views.apc,name='apc'),
    path('<slug:c_slug>/',views.apc,name='products_by_catogory'),
    path('<slug:c_slug>/<slug:p_slug>/',views.pdetail,name='prodcatdet'),
    ]