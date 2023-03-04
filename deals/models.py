from django.db import models

# Create your models here.



class Category(models.Model):
    category = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.category} category'


class Subcategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE) 
    sub = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.sub} sub category'

class Company(models.Model):
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE) 
    company = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.company}'

class Broadband(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    sub = models.ForeignKey(Subcategory, on_delete=models.CASCADE)
    #main
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    
    #broadband
    speed = models.CharField(max_length=100)
    setup_costs = models.CharField(max_length=100)
    price_of_hardware = models.CharField(max_length=100)
    company_logo = models.ImageField(upload_to="images")
    


    def __str__(self):
        return f'{self.title}'


