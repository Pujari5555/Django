from django.contrib import admin
from .models import Saree, Category

# Register Category
admin.site.register(Category)

# Register Saree with custom display if needed
class SareeAdmin(admin.ModelAdmin):
    list_display = ['category', 'price', 'uploaded_at']

admin.site.register(Saree, SareeAdmin)  # ✅ Only this line should register Saree
