from django.db import models

# Create your models here.


class Car(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название', )
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'машина'
        verbose_name_plural = 'машины'