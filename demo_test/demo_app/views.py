from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import UserPassesTestMixin
from .models import Product, Order, User
from django.urls import reverse_lazy
# Create your views here.


class AdminOnlyMixin(UserPassesTestMixin):
    def test_func(self):
        user = self.request.user
        return user.groups.filter(name__in=['Admin']).exists()


class StaffOnlyMixin(UserPassesTestMixin):
    def test_func(self):
        user = self.request.user
        return user.groups.filter(name__in=['Admin', 'Manager']).exists()


class UserLoginView(LoginView):
    template_name = 'login.html'


class UserLogoutView(LogoutView):
    template_name = 'login.html'


class UserListView(ListView):
    model = Product


class ViewProduct(ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'product_list.html'

    def get_queryset(self):
        user = self.request.user
        is_staff = user.is_authenticated and user.groups.filter(name__in=['Admin', 'Manager']).exists()

        if is_staff:
            sort = self.request.GET.get('sort')
            if sort:
                queryset = queryset.order_by(sort)

            search = self.request.GET.get('search')
            if search:
                queryset = queryset.filter(name__icontains=search)
        return queryset


class CreateProduct(AdminOnlyMixin, CreateView): 
    model = Product
    fields = '__all__'
    template_name = 'product_form.html'
    success_url = reverse_lazy


class UpdateProduct(AdminOnlyMixin, UpdateView):


class DeleteProduct(AdminOnlyMixin, DeleteView):


class ViewOrder(ListView):
    model = Order
    context_object_name = 'Orders'

    def get_queryset(self):
        user = self.request.user
        is_staff = user.is_authenticated and user.groups.filter(name__in=['Admin', 'Manager']).exists()

        if is_staff:
            sort = self.request.GET.get('sort')
            if sort:
                queryset = queryset.order_by(sort)

            search = self.request.GET.get('search')
            if search:
                queryset = queryset.filter(name__icontains=search)
        return queryset



class CreateOrder(CreateView):


class UpdateOrder(UpdateView):


class DeleteOrder(DeleteView):
