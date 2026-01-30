from django.db import models

# Create your models here.
class Product(models.Model):
    id_produk = models.AutoField(primary_key=True)
    nama_produk = models.CharField(max_length=100)
    harga = models.DecimalField(max_digits=10, decimal_places=2)
    kategori = models.ForeignKey('Category', on_delete=models.CASCADE)
    status = models.ForeignKey('Status', on_delete=models.CASCADE)

    def __str__(self):
        return self.nama_produk
    
class Category(models.Model):
    id_kategori = models.AutoField(primary_key=True)
    nama_kategori = models.CharField(max_length=100)

    def __str__(self):
        return self.nama_kategori
    
class Status(models.Model):
    id_status = models.AutoField(primary_key=True)
    nama_status = models.CharField(max_length=100)

    def __str__(self):
        return self.nama_status