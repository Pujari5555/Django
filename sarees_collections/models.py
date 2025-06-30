from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Saree(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='sarees/')
    price = models.DecimalField(max_digits=10, decimal_places=2, default=999.00)

  # 💰 New field
    uploaded_at = models.DateTimeField(auto_now_add=True)
