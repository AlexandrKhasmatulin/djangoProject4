# Create your models here.
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Product(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='id')
    name = models.CharField(max_length=150, verbose_name='Наименование')
    description = models.TextField(max_length=1000, verbose_name='Описание')
    image = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100,
                              verbose_name='Изображение', **NULLABLE)
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    price = models.IntegerField(verbose_name='Цена')
    date_creation = models.CharField(max_length=150, verbose_name='Дата создания')
    date_change = models.CharField(max_length=150, verbose_name='Дата изменения')
    seller = models.ForeignKey("Seller", on_delete=models.CASCADE, **NULLABLE)

    def __str__(self):
        return f'''
        {self.name}, {self.description},
        Категория: {self.category}
        Цена: {self.price}
        Поставщик: {self.seller}
        '''

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='Наименование')
    description = models.TextField(max_length=500, verbose_name='Описание')

    def __str__(self):
        return f'{self.name} {self.description}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
class Seller(models.Model):
    id_name = models.CharField(max_length=100, verbose_name='название поставщика, завода', **NULLABLE)
    address = models.CharField(max_length=100, verbose_name='адрес поставщика, завода', **NULLABLE)

    def __str__(self):
        return f'''
           {self.name}, {self.address},
           '''

    class Meta:
        verbose_name = 'Продавец'
        verbose_name_plural = 'Продавцы'

class Version(models.Model):
    product = models.ForeignKey("Product", on_delete=models.CASCADE)
    # product = models.CharField(max_length=150, verbose_name='Название версии')
    version_number = models.IntegerField(verbose_name='Номер версии',)
    version_name = models.CharField(max_length=150, verbose_name='Название версии', default='base')

    def __str__(self):
        return f' {self.version_number} {self.version_name}'

    class Meta:
        verbose_name = 'Версия'
        verbose_name_plural = 'Версии'
