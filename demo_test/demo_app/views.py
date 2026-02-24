from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import UserPassesTestMixin
from .models import Product, Order, User
from django.urls import reverse_lazy
# Create your views here.


class UserLoginView(LoginView):
    template_name = 'login.html'


class UserLogoutView(LogoutView):
    template_name = 'login.html'


class UserListView(ListView):
    model = Product


class ViewProduct(ListView):
    

class CreateProduct(CreateView):
    model = Product
    fields = '__all__'
    template_name = 'product_form.html'
    success_url = reverse_lazy

class UpdateProduct(UpdateView):


class DeleteProduct(DeleteView):


class ViewOrder(ListView):



class CreateOrder(CreateView):


class UpdateOrder(UpdateView):


class DeleteOrder(DeleteView):
