from django.db import models
from django.urls import reverse

# Create your models here.

class Item(models.Model):
    image=models.ImageField(upload_to='photos/%Y/%m/%d', null=True, blank=True)
    title=models.CharField(max_length=250)
    slug=models.CharField(max_length=250)
    content=models.TextField()
    price=models.CharField(max_length=10)
    rating=models.CharField(max_length=5)
    category=models.ForeignKey('Category', on_delete=models.SET_NULL, related_name='all_category', null=True)
    tags=models.ManyToManyField('Tags', db_index=True, null=True, related_name='all_tags')
    time_create=models.DateTimeField(auto_now_add=True)
    time_update=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('item', kwargs={'item_slug': self.slug})
    
    class Meta:
        verbose_name='Item'
        verbose_name_plural='Items'
        ordering=['-time_create']

class Category(models.Model):
    name=models.CharField(max_length=250, db_index=True, blank=True, null=True)
    slug=models.CharField(max_length=250, db_index=True, blank=True, null=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name='Category'
        verbose_name_plural='Categories'
    

class Tags(models.Model):
    tag=models.CharField(max_length=250)
    slug=models.CharField(max_length=250)

    def __str__(self):
        return self.tag

    class Meta:
        verbose_name='Tag'
        verbose_name_plural='Tags'

