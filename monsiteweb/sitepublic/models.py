from socketserver import ThreadingUDPServer
from django.db import models

from django.urls import reverse

from django.utils.text import slugify

from django.contrib.auth.models import User

from django.contrib import messages

from django.core.exceptions import ValidationError

# Create your models here.
   
    
class TypeProduit(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey (       
        User, on_delete=models.PROTECT,
        related_name = "typeproduit_creator",  )
    name = models.CharField(max_length=250, unique=True) 
    
    class Meta:
        ordering = ['name']
        
    def get_absolute_url(self):       
        return reverse('n_listproduit')

    def __str__(self):
        return self.name
    
class TagProduit(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey (       
        User, on_delete=models.PROTECT,
        related_name = "tagproduit_creator" )
    tag_name = models.CharField(max_length=250, unique=True)
    
    
    class Meta:
        ordering = ['tag_name']
        
    def get_absolute_url(self):       
        return reverse('n_listproduit')

    def __str__(self):
        return self.tag_name
    
    
class Produit(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey (       
        User, on_delete=models.PROTECT,
        related_name = "produit_creator",  )
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True, blank=True)
    photo = models.ImageField(upload_to='img_produit', blank=True  )
    fichier = models.FileField(upload_to='fic_produit', blank=True)
    type_produit = models.ForeignKey (       
        TypeProduit, on_delete=models.PROTECT,
        related_name = "type_produit_of" )
    description = models.TextField(blank=True, null= True)
    url = models.URLField (blank=True, null= True)
    date_fin = models.DateField(blank=True, null= True)
    tags_produit = models.ManyToManyField(TagProduit, blank=True)
    active = models.BooleanField(default=True)
    
    
    def save(self, *args, **kwargs):
        #if self.slug == "":
        self.slug = slugify (self.name)
        if self.slug == "":
            #messages.error(self.request, 'Modification refusée. Slug vide refusé.')
            raise ValidationError('Self.slug blanc impossible. ')        
        super().save(*args, **kwargs)  # Call the "real" save() method.

    
        
    class Meta:
        ordering = ['-created_at']
        
    #def get_absolute_url(self):       
        #return reverse('n_listproduit')
    
    def get_absolute_url(self):
        return reverse('n_detailproduit', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name
    
    


class Collection(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey (       
        User, on_delete=models.PROTECT,
        related_name = "collection_creator",  )
    title = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True, blank=True)
    photo = models.ImageField(upload_to='img_collection', blank=True  ) 
    description = models.TextField(blank=True, null= True)
    item = models.ManyToManyField(Produit, blank=True)
    active = models.BooleanField(default=True)
    
    def save(self, *args, **kwargs):
        if self.slug == "":
            self.slug = slugify (self.title)
        if self.slug == "":
            #messages.error(self.request, 'Modification refusée. Slug vide refusé.')
            raise ValidationError('Self.slug blanc impossible. ')        
        super().save(*args, **kwargs)  # Call the "real" save() method.
    
    class Meta:
        ordering = ['-created_at']
    
    def get_absolute_url(self):
        return reverse('n_listcollection')
        #return reverse('n_detailproduit', kwargs={'pk': self.pk})
    
    
    def __str__(self):
        return self.title


#



    
    
    
    
    
