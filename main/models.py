from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

class Menu(models.Model):

    title = models.CharField('Название', max_length=255)
    name = models.CharField(max_length=255, unique=True, db_index=True, verbose_name="Имя")

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'

class Items(MPTTModel):
    title = models.CharField('Название', max_length=50, unique=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="Имя")
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children', verbose_name='Родитель')
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, verbose_name='Привязано к меню')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Раздел'
        verbose_name_plural = 'Разделы'


    
