from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.shortcuts import render,redirect
from .models import Customer
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def customer_dashboard(request):
    # Retrieve the customer's name from the session
    customer_name = request.session.get('customer_name', 'Guest')
    return render(request, 'customers/customer_dashboard.html', {'user': {'first_name': customer_name}})

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
    

def customer_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # Authenticate the customer (basic example without hashing)
        try:
            customer = Customer.objects.get(username=username, password=password)
            # Use customerID instead of id
            request.session['customerID'] = customer.customerID  # Correct primary key field
            messages.success(request, f"Welcome {customer.firstName}!")
            return redirect('customer_dashboard')  # Redirect to customer dashboard after successful login
        except Customer.DoesNotExist:
            messages.error(request, "Invalid username or password. Please try again.")

    return render(request, 'customers/customer_login.html')

def customer_register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        first_name = request.POST['firstName']
        last_name = request.POST['lastName']
        address = request.POST['address']
        middle_name = request.POST.get('middleName', '')  # Optional field
        contact_number = request.POST['contactNumber']
        email = request.POST['email']

        # Check if username or email already exists
        if Customer.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists. Please choose a different one.')
            return render(request, 'customers/customer_registration.html')

        if Customer.objects.filter(email=email).exists():
            messages.error(request, 'An account with this email already exists.')
            return render(request, 'customers/customer_registration.html')

        # Create and save the new customer
        new_customer = Customer.objects.create(
            username=username,
            password=password,  # Passwords should be hashed, but for now, we'll keep it simple.
            firstName=first_name,
            lastName=last_name,
            address=address,
            middleName=middle_name,
            contactNumber=contact_number,
            email=email
        )
        new_customer.save()

        messages.success(request, 'Registration successful! You can now log in.')
        return redirect('customer_login')  # Redirect to login page after successful registration

    return render(request, 'customers/customer_registration.html')