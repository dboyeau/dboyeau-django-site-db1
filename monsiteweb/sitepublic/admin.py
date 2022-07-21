from django.contrib import admin

# Register your models here.

from django.contrib import admin
from sitepublic.models import TypeProduit 
from sitepublic.models import Produit 
from sitepublic.models import TagProduit
from sitepublic.models import Collection


admin.site.register(TypeProduit)
admin.site.register(Produit)
admin.site.register(TagProduit)
admin.site.register(Collection)