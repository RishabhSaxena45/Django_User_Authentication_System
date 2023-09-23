from django.http import HttpResponse
from django.urls import reverse_lazy
from django.shortcuts import render , HttpResponse
from django.views.generic import TemplateView , CreateView , ListView , UpdateView , DeleteView , DetailView
from django.views.generic.edit import FormView
from .forms import studentform
from .models import student

# Create your views here.
def hello(request):
    return HttpResponse("Hello")

class home(TemplateView):
    template_name = 'home.html'

class forms(FormView):
    form_class = studentform
    template_name = 'form.html'

class studentcreate(CreateView):
    model = student
    fields = '__all__'
    success_url = reverse_lazy('list')

class studentlist(ListView):
    model = student

class studentdetail(DetailView):
    model = student

class studentupdate(UpdateView):
    model = student
    fields = '__all__'
    success_url = reverse_lazy('list')

class studentdelete(DeleteView):
    model = student
    success_url = reverse_lazy('list')