from django.urls import path
from django.urls.resolvers import URLPattern
from . import views
from .views import orderHistory, orderDetail

app_name = 'order'

urlpatterns = [
    path('order_success/<int:order_id>/', views.order_success, name = "order_success"),
    path('history/', orderHistory.as_view(), name = "order_history"),
    path('<int:order_id>/', orderDetail.as_view(), name = "order_detail")
]