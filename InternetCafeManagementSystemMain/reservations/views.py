from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django import forms
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .models import Reservations
from django.contrib import messages

class ReservationsListView(ListView):
    model = Reservations
    template_name = 'reservations_list.html'
    context_object_name = 'reservations'

class ReservationsCreateView(CreateView):
    model = Reservations
    template_name = 'reservations/reservations_create.html'
    fields = ['time', 'date', 'status', 'adminID']
    success_url = reverse_lazy('reservations_list')

    def get_form(self):
        form = super().get_form()
        form.fields['date'].widget = forms.DateInput(attrs={
            'type': 'date',
            'class': 'form-control',
        })
        form.fields['time'].widget = forms.TimeInput(attrs={
            'type': 'time',
            'class': 'form-control',
        })
        return form

class ReservationsDetailView(DetailView):
    model = Reservations
    template_name = 'reservations/reservations_detail.html'
    context_object_name = 'reservation'

class ReservationsUpdateView(UpdateView):
    model = Reservations
    template_name = 'reservations/reservations_update.html'
    fields = ['time', 'date', 'status', 'adminID']
    success_url = reverse_lazy('reservations_list')

class ReservationsDeleteView(DeleteView):
    model = Reservations
    template_name = 'reservations/reservations_delete.html'
    success_url = reverse_lazy('reservations_list')

class ReservationsCustomerCreateView(CreateView):
    model = Reservations
    template_name = 'reservations/reservations_customer.html'
    fields = ['time', 'date']  # Only allow customers to select time and date
    success_url = reverse_lazy('customer_dashboard')  # Redirect to the reservation list page after success

    def form_valid(self, form):
        # Set the adminID to None since it's not required for customer reservations
        form.instance.adminID = None
        # Call the parent class's form_valid method
        response = super().form_valid(form)
        
        # Add a success message
        messages.success(self.request, "Reservation successfully created!")
        return response

    def get_form(self):
        form = super().get_form()
        form.fields['date'].widget = forms.DateInput(attrs={'type': 'date'})
        form.fields['time'].widget = forms.TimeInput(attrs={'type': 'time'})
        return form