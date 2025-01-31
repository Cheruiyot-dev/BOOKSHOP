from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.title} by {self.author}"
    
    def has_stock(self):
        return self.quantity > 0
    
    def can_sell(self, amount):
        return self.quantity >= amount

class Sale(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity_sold = models.PositiveIntegerField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.quantity_sold} copies of {self.book.title}"

    def total_price(self):
        return self.quantity_sold * self.book.price

    class Meta:
        ordering = ['-date']  # Most recent sales first