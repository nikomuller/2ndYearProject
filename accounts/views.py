from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView

from .forms import UserCreationFormCustom
from .models import Profile

# Create your views here.

class SignUpView(CreateView):
    form_class=UserCreationFormCustom
    template_name = "registration/signup.html"
    success_url = reverse_lazy('login')

class UserEditView(UpdateView):
    model=Profile
    template_name = 'registration/edit_profile.html'
    fields=['date_of_birth', 'Address_Line_1', 'Address_Line_2', 'Address_City', 'Address_Country']
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user.profile

class ProfilePageView(DetailView):
    model=Profile
    template_name = 'registration/user_profile.html'

    def get_object(self):
        return self.request.user