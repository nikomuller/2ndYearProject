from django.urls import path
from .views import(
    StaffListView, 
    StaffDetailView, 
    StaffCreateView, 
    StaffEditView, 
    StaffDeleteView
)

urlpatterns = [
    path('', StaffListView.as_view(), name = 'CRUD'),
    path('<int:pk>/', StaffDetailView.as_view(), name = 'staff_detail'),
    path('new/', StaffCreateView.as_view(), name = 'staff_new'),
    path('<int:pk>/edit/', StaffEditView.as_view(), name = 'staff_edit'),
    path('<int:pk>/delete/', StaffDeleteView.as_view(), name = 'staff_delete'),
]