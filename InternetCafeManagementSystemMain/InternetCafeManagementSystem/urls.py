"""
URL configuration for InternetCafeManagementSystem project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# urls.py for InternetCafeManagementSystem project
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

from sessionsdata.views import (
    SessionDataCreateView, SessionDataDetailView, 
    SessionDataUpdateView, SessionDataDeleteView, 
    SessionDataListView, StartSessionView
)
from customers.views import (
    CustomerCreateView, CustomerDetailView, 
    CustomerUpdateView, CustomerDeleteView, 
    CustomerListView, customer_login,
    customer_dashboard, customer_register
)
from admin_app.views import (
    AdminListView, AdminCreateView, 
    AdminDetailView, AdminUpdateView, 
    AdminDeleteView, AdminLoginView,
    admin_dashboard,
)

from computerunit.views import (
    ComputerUnitListView, ComputerUnitCreateView,
    ComputerUnitDetailView, ComputerUnitUpdateView,
    ComputerUnitDeleteView, CustomerComputerUnitListView,
)

from reservations.views import (
    ReservationsListView,
    ReservationsCreateView,
    ReservationsDetailView,
    ReservationsUpdateView,
    ReservationsDeleteView,
    ReservationsCustomerCreateView,
)

from customerfeedback.views import (
    CustomerFeedbackListView, 
    CustomerFeedbackCreateView, 
    CustomerFeedbackDetailView, 
    CustomerFeedbackUpdateView, 
    CustomerFeedbackDeleteView
)

urlpatterns = [
    path('', lambda request: redirect('customer_login')), 
    path('login/', customer_login, name='customer_login'),
    path('dashboard/', customer_dashboard, name='customer_dashboard'),
    path('admin_app/login/', AdminLoginView.as_view(), name='admin_login'),
    path('admin_dashboard/', admin_dashboard, name='admin_dashboard'),
    
    path('admin/', admin.site.urls),  # Django's built-in admin site

    # URLs for sessions data app
    path('sessions/', SessionDataListView.as_view(), name='session_list'),  
    path('sessions/create/', SessionDataCreateView.as_view(), name='session_create'),
    path('sessions/<int:pk>/', SessionDataDetailView.as_view(), name='session_detail'),
    path('sessions/<int:pk>/update/', SessionDataUpdateView.as_view(), name='session_update'),
    path('sessions/<int:pk>/delete/', SessionDataDeleteView.as_view(), name='session_delete'),
    path('sessions/start/', StartSessionView.as_view(), name='start_session'),

    # URLs for customers app
    path('customers/', CustomerListView.as_view(), name='customer_list'),
    path('customers/create/', CustomerCreateView.as_view(), name='customer_create'),
    path('customers/<int:pk>/', CustomerDetailView.as_view(), name='customer_detail'),
    path('customers/<int:pk>/update/', CustomerUpdateView.as_view(), name='customer_update'),
    path('customers/<int:pk>/delete/', CustomerDeleteView.as_view(), name='customer_delete'),
    path('login/', customer_login, name='customer_login'),
    path('register/', customer_register, name='customer_register'),

    # URLs for admin management app
    path('admin_app/', AdminListView.as_view(), name='admin_list'),
    path('admin_app/create/', AdminCreateView.as_view(), name='admin_create'),
    path('admin_app/<int:pk>/', AdminDetailView.as_view(), name='admin_detail'),
    path('admin_app/<int:pk>/update/', AdminUpdateView.as_view(), name='admin_update'),
    path('admin_app/<int:pk>/delete/', AdminDeleteView.as_view(), name='admin_delete'),
    
    # URLs for computerunit app
    path('computerunit', ComputerUnitListView.as_view(), name='computerunit_list'),
    path('computerunit/create/', ComputerUnitCreateView.as_view(), name='computerunit_create'),
     path('computerunit/forcustomers/', CustomerComputerUnitListView.as_view(), name='customer_computerunit_list'),
    path('computerunit/<int:pk>/', ComputerUnitDetailView.as_view(), name='computerunit_detail'),
    path('computerunit/<int:pk>/update/', ComputerUnitUpdateView.as_view(), name='computerunit_update'),
    path('computerunit/<int:pk>/delete/', ComputerUnitDeleteView.as_view(), name='computerunit_delete'),

    # URLs for reservations app
    path('reservations/', ReservationsListView.as_view(), name='reservations_list'),
    path('reservations/create/', ReservationsCreateView.as_view(), name='reservations_create'),
    path('reservations/<int:pk>/', ReservationsDetailView.as_view(), name='reservations_detail'),
    path('reservations/<int:pk>/update/', ReservationsUpdateView.as_view(), name='reservations_update'),
    path('reservations/<int:pk>/delete/', ReservationsDeleteView.as_view(), name='reservations_delete'),
    path('reservations/create-customer/', ReservationsCustomerCreateView.as_view(), name='reservations_create_customer'),

    # URLs for customer feedback
    path('customerfeedback', CustomerFeedbackListView.as_view(), name='feedback_list'),
    path('customerfeedback/create/', CustomerFeedbackCreateView.as_view(), name='feedback_create'),
    path('customerfeedback/<int:pk>/', CustomerFeedbackDetailView.as_view(), name='feedback_detail'),
    path('customerfeedback/<int:pk>/update/', CustomerFeedbackUpdateView.as_view(), name='feedback_update'),
    path('customerfeedback/<int:pk>/delete/', CustomerFeedbackDeleteView.as_view(), name='feedback_delete'),
]
