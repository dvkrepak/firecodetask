from django.db import models


class Store(models.Model):
    name = models.CharField(max_length=255, verbose_name='Name')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='Slug')
    city = models.ForeignKey('City', on_delete=models.PROTECT, verbose_name='City')
    street = models.ForeignKey('Street', on_delete=models.PROTECT, verbose_name='Street')
    number = models.IntegerField(verbose_name='Number')
    opening_time = models.TimeField(verbose_name='Opening time')
    closing_time = models.TimeField(verbose_name='Closing time')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Store'
        verbose_name_plural = 'Stores'


class City(models.Model):
    name = models.CharField(max_length=255, verbose_name='Name')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='Slug')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'City'
        verbose_name_plural = 'Cities'


class Street(models.Model):
    name = models.CharField(max_length=255, verbose_name='Name')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='Slug')
    city = models.ForeignKey('City', on_delete=models.PROTECT, verbose_name='City')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Street'
        verbose_name_plural = 'Streets'
