from django.urls import path
from .views import CustomerCreateView, CustomerDetailView, CustomerUpdateView, CustomerDeleteView, CustomerListView

urlpatterns = [
    path('', CustomerListView.as_view(), name='customer-list'),  # List view
    path('create/', CustomerCreateView.as_view(), name='customer-create'),  # Create view
    path('<int:pk>/', CustomerDetailView.as_view(), name='customer-detail'),  # Detail view
    path('<int:pk>/update/', CustomerUpdateView.as_view(), name='customer-update'),  # Update view
    path('<int:pk>/delete/', CustomerDeleteView.as_view(), name='customer-delete'),  # Delete view
]
