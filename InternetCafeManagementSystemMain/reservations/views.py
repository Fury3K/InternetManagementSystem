from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .models import Reservations

class ReservationsListView(ListView):
    model = Reservations
    template_name = 'reservations_list.html'
    context_object_name = 'reservations'

class ReservationsCreateView(CreateView):
    model = Reservations
    template_name = 'reservations/reservations_create.html'
    fields = ['time', 'date', 'status', 'adminID']
    success_url = reverse_lazy('reservations_list')

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
