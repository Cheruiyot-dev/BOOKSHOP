# inventory/urls.py
from django.urls import path
from . import views

# Define the app_name for namespacing
app_name = 'inventory'

urlpatterns = [
    path('', views.home, name='home'),
    path('books/', views.book_list, name='book_list'),
    path('add-book/', views.add_book, name='add_book'),
    path('sales/', views.sales_list, name='sales_list'),
    path('sell-book/', views.sell_book, name='sell_book'),
    path('receipt/<int:sale_id>/', views.receipt, name='receipt'),
    # Add other URL patterns as needed
]