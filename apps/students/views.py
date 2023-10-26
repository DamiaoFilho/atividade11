from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
# Create your views here.
from .models import Student
from .forms import StudentForm

class ListView(ListView):
    model = Student
    template_name = "list_view.html"

class CreateView(CreateView):
    model = Student
    template_name = "create_view.html"
    form_class = StudentForm
    success_url = "/"

class DetailView(DetailView):
    model = Student
    template_name = "detail_view.html"

class UpdateView(UpdateView):
    model = Student
    form_class = StudentForm
    template_name = "create_view.html"
    success_url = "/"

class DeleteView(DeleteView):
    model = Student
    success_url = "/"
    template_name = "student_confirm_delete.html"