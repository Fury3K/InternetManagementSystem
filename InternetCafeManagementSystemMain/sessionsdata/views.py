from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from .models import SessionData
from .serializers import SessionDataSerializer
from customers.models import Customer
from reservations.models import Reservations
from computerunit.models import ComputerUnit
from admin_app.models import Admin
from datetime import datetime

# List all sessions
class SessionDataListView(View):
    def get(self, request):
        sessions = SessionData.objects.all()
        return render(request, 'sessionsdata/session_list.html', {'sessions': sessions})
    

class StartSessionView(View):
    def get(self, request):
        return render(request, 'sessionsdata/start_session.html')

    def post(self, request):
        start_time_str = request.POST.get('startTime')
        computer_id = request.POST.get('computerID')
        username = request.POST.get('username')

        # Validate and parse time input
        try:
            start_time = datetime.fromisoformat(start_time_str)
        except ValueError:
            return render(request, 'sessionsdata/start_session.html', {
                'error': 'Invalid time format. Please use a valid date-time format.'
            })

        # Validate computer ID
        try:
            computer = get_object_or_404(ComputerUnit, pk=computer_id)
        except ValueError:
            return render(request, 'sessionsdata/start_session.html', {
                'error': 'Invalid computer ID.'
            })

        # Create session data (placeholder logic, modify as needed)
        # Assuming session end time and cost will be handled later
        session_data = {
            'startTime': start_time.time(),  # Storing only time if needed
            'endTime': None,
            'cost': 0.00,
            'computerID': computer.computerID
        }

        # Redirect to a success page or session list after creating the session
        return redirect('session_list')

# Create a new session
class SessionDataCreateView(View):
    def get(self, request):
        context = {
            'customers': Customer.objects.all(),
            'reservations': Reservations.objects.all(),
            'computers': ComputerUnit.objects.all(),
            'admins': Admin.objects.all()
        }
        return render(request, 'sessionsdata/session_create.html', context)

    def post(self, request):
        start_time_str = request.POST.get('startTime')
        end_time_str = request.POST.get('endTime')

        # Validate time format
        try:
            start_time = datetime.fromisoformat(start_time_str).time()
            end_time = datetime.fromisoformat(end_time_str).time()
        except ValueError:
            context = {
                'errors': {'startTime': 'Invalid time format', 'endTime': 'Invalid time format'},
                'customers': Customer.objects.all(),
                'reservations': Reservations.objects.all(),
                'computers': ComputerUnit.objects.all(),
                'admins': Admin.objects.all()
            }
            return render(request, 'sessionsdata/session_create.html', context)

        # Validate IDs from the form, handle empty fields
        try:
            customer = get_object_or_404(Customer, pk=request.POST.get('customerID'))
            reservation = get_object_or_404(Reservations, pk=request.POST.get('reservationID'))
            computer = get_object_or_404(ComputerUnit, pk=request.POST.get('computerID'))
            admin = get_object_or_404(Admin, pk=request.POST.get('adminID'))
        except ValueError:
            context = {
                'errors': {
                    'customerID': 'Invalid customer ID',
                    'reservationID': 'Invalid reservation ID',
                    'computerID': 'Invalid computer ID',
                    'adminID': 'Invalid admin ID'
                },
                'customers': Customer.objects.all(),
                'reservations': Reservations.objects.all(),
                'computers': ComputerUnit.objects.all(),
                'admins': Admin.objects.all()
            }
            return render(request, 'sessionsdata/session_create.html', context)

        # Prepare data for the serializer
        data = {
            'startTime': start_time,
            'endTime': end_time,
            'cost': request.POST.get('cost'),
            'customerID': customer.customerID,  # Correct attribute
            'reservationID': reservation.reservationID,
            'computerID': computer.computerID,
            'adminID': admin.adminID,
        }

        serializer = SessionDataSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return redirect('session_list')
        
        # If serializer has errors, re-render form with errors
        context = {
            'customers': Customer.objects.all(),
            'reservations': Reservations.objects.all(),
            'computers': ComputerUnit.objects.all(),
            'admins': Admin.objects.all(),
            'errors': serializer.errors
        }
        return render(request, 'sessionsdata/session_create.html', context)

# Retrieve session details
class SessionDataDetailView(View):
    def get(self, request, pk):
        session = get_object_or_404(SessionData, pk=pk)
        return render(request, 'sessionsdata/session_detail.html', {'session': session})

# Update a session
class SessionDataUpdateView(View):
     def get(self, request, pk):
        # Fetch the session to be updated
        session = get_object_or_404(SessionData, pk=pk)

        # Render the update form with pre-populated data
        context = {
            'session': session,
            'customers': Customer.objects.all(),
            'reservations': Reservations.objects.all(),
            'computers': ComputerUnit.objects.all(),
            'admins': Admin.objects.all()
        }
        return render(request, 'sessionsdata/session_update.html', context)

     def post(self, request, pk):
        session = get_object_or_404(SessionData, pk=pk)
        
        start_time_str = request.POST.get('startTime')
        end_time_str = request.POST.get('endTime')
        
        try:
            start_time = datetime.fromisoformat(start_time_str).time()
            end_time = datetime.fromisoformat(end_time_str).time()
        except ValueError:
            return render(request, 'sessionsdata/session_update.html', {
                'errors': {'startTime': 'Invalid time format', 'endTime': 'Invalid time format'},
                'session': session,
                'customers': Customer.objects.all(),
                'reservations': Reservations.objects.all(),
                'computers': ComputerUnit.objects.all(),
                'admins': Admin.objects.all()
            })

        data = {
            'startTime': start_time,
            'endTime': end_time,
            'cost': request.POST.get('cost'),
            'customerID': request.POST.get('customerID'),
            'reservationID': request.POST.get('reservationID'),
            'computerID': request.POST.get('computerID'),
            'adminID': request.POST.get('adminID'),
        }

        serializer = SessionDataSerializer(session, data=data)
        if serializer.is_valid():
            serializer.save()
            return redirect('session_list')
        
        context = {
            'session': session,
            'customers': Customer.objects.all(),
            'reservations': Reservations.objects.all(),
            'computers': ComputerUnit.objects.all(),
            'admins': Admin.objects.all(),
            'errors': serializer.errors
        }
        return render(request, 'sessionsdata/session_update.html', context)

# Delete a session
class SessionDataDeleteView(View):
    def post(self, request, pk):
        session = get_object_or_404(SessionData, pk=pk)
        session.delete()
        return redirect('session_list')
