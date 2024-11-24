from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.shortcuts import render
from .models import Customer

# List all customers
class CustomerListView(ListView):
    model = Customer
    template_name = 'customers/customer_list.html'
    context_object_name = 'customers'

# CREATE a new customer
class CustomerCreateView(CreateView):
    model = Customer
    template_name = 'customers/customer_create.html'
    fields = ['username', 'password', 'firstName', 'lastName', 'address', 'middleName', 'contactNumber', 'email']
    success_url = reverse_lazy('customer_list')  # Redirect to the customer list after successful creation

# READ customer details
class CustomerDetailView(DetailView):
    model = Customer
    template_name = 'customers/customer_detail.html'
    context_object_name = 'customer'

# UPDATE a customer
class CustomerUpdateView(UpdateView):
    model = Customer
    template_name = 'customers/customer_update.html'
    fields = ['username', 'password', 'firstName', 'lastName', 'address', 'middleName', 'contactNumber', 'email']
    success_url = reverse_lazy('customer_list')  # Redirect to the customer list after successful update

# DELETE a customer
class CustomerDeleteView(DeleteView):
    model = Customer
    template_name = 'customers/customer_confirm_delete.html'
    success_url = reverse_lazy('customer_list')  # Redirect to the customer list after deletion
