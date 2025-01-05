from django.urls import path
from .views import ProductCat, ProdDetail

app_name = 'shop'

urlpatterns = [
    path('', ProductCat.as_view(), name = 'allProductCat'),
    path('<uuid:category_id>/', ProductCat.as_view(), name = 'categorizedproducts'),
    path('<uuid:category_id>/<uuid:product_id>/', ProdDetail.as_view(), name = 'prod_detail'),
]