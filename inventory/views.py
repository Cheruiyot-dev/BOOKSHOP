from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Book, Sale
from .forms import BookForm, SellBookForm

def home(request):
    """Home page view"""
    return render(request, "inventory/home.html")

def book_list(request):
    books = Book.objects.all()
    return render(request, 'inventory/book_list.html', {'books': books})
def add_book(request):
    """Add a new book"""
    if request.method == "POST":
        form = BookForm(request.POST)
       
        if form.is_valid():
            form.save()
            return redirect("inventory:book_list")  # ✅ Redirect to book list
    else:
        form = BookForm()
    return render(request, "inventory/add_book.html", {"form": form})

def sell_book(request):
    if request.method == "POST":
        form = SellBookForm(request.POST)
        if form.is_valid():
            book = form.cleaned_data["book"]
            quantity_sold = form.cleaned_data["quantity_sold"]

            if book.quantity >= quantity_sold:
                # Use form.save() instead of manual creation
                sale = form.save()
                
                # Update book quantity
                book.quantity -= quantity_sold
                book.save()
                
                messages.success(request, f"✅ Sold {quantity_sold} copies of '{book.title}'!")
                # Change this line to redirect to receipt
                return redirect("inventory:receipt", sale_id=sale.id)  # Changed this line
            else:
                messages.error(request, "❌ Not enough stock!")
    else:
        form = SellBookForm()

    return render(request, "inventory/sell_book.html", {"form": form})
def sales_list(request):  # ✅ Keep the original name
    all_sales = Sale.objects.all()  # ✅ Retrieve all sales
    return render(request, "inventory/sales_list.html", {"sales": all_sales})
def receipt(request, sale_id):
    """Generate a receipt for a sale"""
    sale = get_object_or_404(Sale, id=sale_id)
    return render(request, "inventory/receipt.html", {"sale": sale})
