from django.urls import path, include

urlpatterns = [
    path("", include("inventory.urls", namespace="inventory")),  # ✅ Include inventory app
  

]