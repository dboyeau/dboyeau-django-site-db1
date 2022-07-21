from sitepublic.models import Produit
from sitepublic.models import TypeProduit




def AddDataProduit(ii):
              
       print("Les cons 6")       
       t = TypeProduit(name = "type_le_tennis" + str(ii))
       t.save()
       p = Produit(name = "produit_le_tennis" + str(ii), slug ="slug_produit_le_tennis" + str(ii),  type_produit = t)
       p.save()
       
       
       
       print("Les cons 6")
       
def AddDataProduits(): 
       for i in range(1001, 2000):
               AddDataProduit(i)
