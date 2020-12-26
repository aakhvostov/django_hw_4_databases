from django.db import models
from django.template.defaultfilters import slugify


class Phone(models.Model):
    name = models.CharField(max_length=150, verbose_name='Модель')
    image = models.TextField(verbose_name='Фото')
    price = models.IntegerField(verbose_name='Цена')
    release_date = models.DateField(verbose_name='Дта релиза')
    lte_exists = models.BooleanField(verbose_name='ЛТЕ')
    slug = models.SlugField(verbose_name='URL', max_length=50, unique=True)

    def __str__(self):
        return f"{self.name} цена {self.price}"

    def get_slug(self):
        self.slug = slugify(self.name)
