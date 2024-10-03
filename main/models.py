from django.db import models


class Category(models.Model):
    name=models.CharField(max_length=30)


    def __str__(self):
        return self.name


class Firma(models.Model):
    name=models.CharField(max_length=50)

    def __str__(self):
        return self.name



class Shop(models.Model):
    product=models.CharField(max_length=50)
    content=models.TextField()
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    firma=models.ForeignKey(Firma,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.product}, {self.content}"







