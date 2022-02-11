from django.db import models

# Create your models here.
class Pizzas(models.Model):
    """A pizza for eating"""
    name = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    
  
class Toppings(models.Model):
            """Toppings for the pizza"""
            pizzas = models.ForeignKey(Pizzas,on_delete=models.CASCADE)
            name = models.TextField()
            date_added = models.DateTimeField(auto_now_add=True)
            
            def __str__(self):
                """Return a string representation of the model created"""
                return self.name   