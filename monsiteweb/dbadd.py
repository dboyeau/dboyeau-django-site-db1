from sitepublic.models import Produit
from sitepublic.models import TypeProduit


t = Typeproduit(name = "type127")
p = Produit(name = "produit127", type_produit = t)
t.save()
p.save()