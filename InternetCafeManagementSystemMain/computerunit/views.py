from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import ComputerUnit
from admin_app.models import Admin  # Assuming Admin is in admin_app

# List all ComputerUnits
class ComputerUnitListView(View):
    def get(self, request):
        computer_units = ComputerUnit.objects.all()
        return render(request, 'computerunit/computerunit_list.html', {'computer_units': computer_units})

# Create a new ComputerUnit
class ComputerUnitCreateView(View):
    def get(self, request):
        admins = Admin.objects.all()  # Fetch all admins for dropdown
        return render(request, 'computerunit/computerunit_create.html', {'admins': admins})

    def post(self, request):
        availability = request.POST.get('availability') == 'on'  # Checkbox returns 'on' if checked
        admin_id = request.POST.get('adminID')
        admin = Admin.objects.get(pk=admin_id) if admin_id else None
        if admin:
            ComputerUnit.objects.create(availability=availability, adminID=admin)
            return redirect('computerunit_list')
        error = "Admin is required."
        admins = Admin.objects.all()
        return render(request, 'computerunit/computerunit_create.html', {'admins': admins, 'error': error})

# Retrieve ComputerUnit details
class ComputerUnitDetailView(View):
    def get(self, request, pk):
        computer_unit = get_object_or_404(ComputerUnit, pk=pk)
        return render(request, 'computerunit/computerunit_detail.html', {'computer_unit': computer_unit})

# Update a ComputerUnit
class ComputerUnitUpdateView(View):
    def get(self, request, pk):
        computer_unit = get_object_or_404(ComputerUnit, pk=pk)
        admins = Admin.objects.all()
        return render(request, 'computerunit/computerunit_update.html', {'computer_unit': computer_unit, 'admins': admins})

    def post(self, request, pk):
        computer_unit = get_object_or_404(ComputerUnit, pk=pk)
        availability = request.POST.get('availability') == 'on'
        admin_id = request.POST.get('adminID')
        admin = Admin.objects.get(pk=admin_id) if admin_id else None
        if admin:
            computer_unit.availability = availability
            computer_unit.adminID = admin
            computer_unit.save()
            return redirect('computerunit_list')
        error = "Admin is required."
        admins = Admin.objects.all()
        return render(request, 'computerunit/computerunit_update.html', {'computer_unit': computer_unit, 'admins': admins, 'error': error})

# Delete a ComputerUnit
class ComputerUnitDeleteView(View):
    def post(self, request, pk):
        computer_unit = get_object_or_404(ComputerUnit, pk=pk)
        computer_unit.delete()
        return redirect('computerunit_list')
