from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import Customer
from .serializers import CustomerSerializer

# List all customers
class CustomerListView(View):
    def get(self, request):
        customers = Customer.objects.all()
        return render(request, 'customers/customer_list.html', {'customers': customers})

# CREATE a new customer
class CustomerCreateView(APIView):
    def get(self, request):
        # Render the customer creation form
        return render(request, 'customers/customer_create.html')

    def post(self, request):
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return redirect('customer-list')  # Redirect to the customer list view
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# READ customer details
class CustomerDetailView(View):
    def get(self, request, pk):
        customer = get_object_or_404(Customer, pk=pk)
        return render(request, 'customers/customer_detail.html', {'customer': customer})

# UPDATE a customer
class CustomerUpdateView(View):
    def get(self, request, pk):
        customer = get_object_or_404(Customer, pk=pk)
        return render(request, 'customers/customer_update.html', {'customer': customer})

    def post(self, request, pk):
        customer = get_object_or_404(Customer, pk=pk)
        serializer = CustomerSerializer(customer, data=request.POST)  # Use request.POST
        if serializer.is_valid():
            serializer.save()
            return redirect('customer-list')  # Redirect after updating
        return render(request, 'customers/customer_update.html', {'customer': customer, 'errors': serializer.errors})

# DELETE a customer
class CustomerDeleteView(View):
    def post(self, request, pk):
        customer = get_object_or_404(Customer, pk=pk)
        customer.delete()
        return redirect('customer-list')  # Redirect after deletion
