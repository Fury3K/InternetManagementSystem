from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .models import CustomerFeedback

class CustomerFeedbackListView(ListView):
    model = CustomerFeedback
    template_name = 'customerfeedback/customerfeedback_list.html'
    context_object_name = 'feedbacks'


class CustomerFeedbackCreateView(CreateView):
    model = CustomerFeedback
    template_name = 'customerfeedback/customerfeedback_create.html'
    fields = ['customerFeedback', 'customerID', 'adminID']
    success_url = reverse_lazy('feedback_list')


class CustomerFeedbackDetailView(DetailView):
    model = CustomerFeedback
    template_name = 'customerfeedback/customerfeedback_detail.html'
    context_object_name = 'feedback'


class CustomerFeedbackUpdateView(UpdateView):
    model = CustomerFeedback
    template_name = 'customerfeedback/customerfeedback_update.html'
    fields = ['customerFeedback', 'customerID', 'adminID']
    success_url = reverse_lazy('feedback_list')


class CustomerFeedbackDeleteView(DeleteView):
    model = CustomerFeedback
    template_name = 'customerfeedback/customerfeedback_delete.html'
    context_object_name = 'feedback'
    success_url = reverse_lazy('feedback_list')
