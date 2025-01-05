from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Staff
from django.urls import reverse_lazy

# Create your views here.
class StaffListView(ListView):
    model = Staff
    template_name = 'CRUD.html'
    context_object_name = "all_staff_list"

class StaffDetailView(DetailView):
    model = Staff
    template_name = 'staff_detail.html'

class StaffCreateView(CreateView):
    model = Staff
    template_name = 'staff_new.html'
    fields = ['name', 'DOB', 'ID_number', 'staff_type']

class StaffEditView(UpdateView):
    model = Staff
    template_name = 'staff_edit.html'
    fields = ['staff_type']

class StaffDeleteView(DeleteView):
    model = Staff
    template_name = 'staff_delete.html'
    success_url = reverse_lazy('CRUD')
