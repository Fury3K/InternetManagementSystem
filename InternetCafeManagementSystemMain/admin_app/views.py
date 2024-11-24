from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import Admin

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
