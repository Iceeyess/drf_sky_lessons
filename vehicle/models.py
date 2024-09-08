from django.db import models

# Create your models here.
NULLABLE = {'blank': True, 'null': True}


class Car(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название', )
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'машина'
        verbose_name_plural = 'машины'


class Moto(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название', )
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'мотоцикл'
        verbose_name_plural = 'мотоциклы'

class Milage(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, **NULLABLE)
    moto = models.ForeignKey(Moto, on_delete=models.CASCADE, **NULLABLE)

    milage = models.PositiveIntegerField(verbose_name='пробег')
    year = models.PositiveIntegerField(verbose_name='год регистрации')

    def __str__(self):
        return f'{self.moto if self.moto else self.car}'

    class Meta:
        verbose_name = 'пробег'
        verbose_name_plural = 'пробеги'
        ordering = ('-year', )