from django import forms
from .models import Book, Sale

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ["title", "author", "price", "quantity"]

class SellBookForm(forms.ModelForm):
    book = forms.ModelChoiceField(
        queryset=Book.objects.filter(quantity__gt=0),  # Only show books with stock
        empty_label="Select a book",
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    quantity_sold = forms.IntegerField(
        min_value=1,
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Sale
        fields = ["book", "quantity_sold"]

    def clean(self):
        cleaned_data = super().clean()
        book = cleaned_data.get("book")
        quantity_sold = cleaned_data.get("quantity_sold")

        if book and quantity_sold:
            if quantity_sold > book.quantity:
                raise forms.ValidationError(
                    f"Cannot sell {quantity_sold} copies. Only {book.quantity} available in stock."
                )
        
        return cleaned_data