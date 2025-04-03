from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Car
from .forms import CarForm


class AddCarView(LoginRequiredMixin, CreateView):
    model = Car
    form_class = CarForm
    template_name = 'add_brand.html' 
    success_url = reverse_lazy('add_car')  


    def form_valid(self, form):
        return super().form_valid(form)
    

  
    

class EditCarView(LoginRequiredMixin, UpdateView):
    model = Car
    form_class = CarForm
    template_name = 'add_brand.html' 
    success_url = reverse_lazy('add_car') 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'Edit Car'
        return context
