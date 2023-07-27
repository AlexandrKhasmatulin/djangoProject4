from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=150, verbose_name='название')
    slug = models.CharField(max_length=150, verbose_name='slug', null=True, blank=True)
    content = models.TextField(max_length=1000, verbose_name='содержание')
    preview = models.ImageField(verbose_name='изображение')
    date_of_creation = models.CharField(max_length=150, verbose_name='дата создания')
    is_published = models.BooleanField(default=True, verbose_name='опубликовано')
    views_count = models.IntegerField(default=0, verbose_name='просмотры')

    def __str__(self):
        return self.title


class Meta:
    verbose_name = 'статья'
    verbose_name_plural = 'статьи'
