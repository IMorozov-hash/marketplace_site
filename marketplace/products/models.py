from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    content = models.TextField(verbose_name='Описание товара')
    image = models.ImageField(verbose_name= 'Изображение товара', blank = True, null = True, upload_to = 'products/%Y/%m' )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'