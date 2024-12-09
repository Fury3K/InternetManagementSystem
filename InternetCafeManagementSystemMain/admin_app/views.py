from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.contrib.auth import authenticate, login  # Add this line
from django.contrib import messages
from .models import Admin
from computerunit.models import ComputerUnit

# List all Admins
class AdminListView(View):
    def get(self, request):
        admins = Admin.objects.all()
        return render(request, 'admin_app/admin_list.html', {'admins': admins})

# Create a new Admin
class AdminCreateView(View):
    def get(self, request):
        return render(request, 'admin_app/admin_create.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username and password:
            Admin.objects.create(username=username, password=password)
            return redirect('admin_list')
        error = "Both username and password are required."
        return render(request, 'admin_app/admin_create.html', {'error': error})

# Retrieve Admin details
class AdminDetailView(View):
    def get(self, request, pk):
        admin = get_object_or_404(Admin, pk=pk)
        return render(request, 'admin_app/admin_detail.html', {'admin': admin})

# Update an Admin
class AdminUpdateView(View):
    def get(self, request, pk):
        admin = get_object_or_404(Admin, pk=pk)
        return render(request, 'admin_app/admin_update.html', {'admin': admin})

    def post(self, request, pk):
        admin = get_object_or_404(Admin, pk=pk)
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username and password:
            admin.username = username
            admin.password = password
            admin.save()
            return redirect('admin_list')
        error = "Both username and password are required."
        return render(request, 'admin_app/admin_update.html', {'admin': admin, 'error': error})

# Delete an Admin
class AdminDeleteView(View):
    def post(self, request, pk):
        admin = get_object_or_404(Admin, pk=pk)
        admin.delete()
        return redirect('admin_list')

class AdminLoginView(View):
    template_name = 'admin_app/admin_login.html'

    def get(self, request):
        # Render the login form
        return render(request, self.template_name)

    def post(self, request):
        username = request.POST.get('username')  
        password = request.POST.get('password')

        # Authenticate the admin using the provided username and password
        try:
            admin = Admin.objects.get(username=username, password=password)
            # Store the admin's ID in the session
            request.session['adminID'] = admin.adminID  # Correct primary key field for Admin
            messages.success(request, f"Welcome {admin.username}!")  # Adjust welcome message as needed
            return redirect('admin_dashboard')  # Redirect to the admin dashboard
        except Admin.DoesNotExist:
            messages.error(request, "Invalid username or password. Please try again.")

        return render(request, self.template_name)
    
def admin_dashboard(request):
    computer_units = ComputerUnit.objects.all()
    return render(request, 'admin_app/admin_dashboard.html', {'computer_units': computer_units})
