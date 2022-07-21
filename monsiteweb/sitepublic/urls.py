from django.urls import path
from django.views.generic import TemplateView
from sitepublic.views import ProduitList
from sitepublic.views import CollectionList
from sitepublic.views import TypeList
from sitepublic.views import TagList

#from sitepublic.views import ProduitCreate
from sitepublic.views3 import ProduitCreate
from sitepublic.views3 import CollectionCreate
from sitepublic.views3 import CollectionDetail
from sitepublic.views3 import UpdateUser
from sitepublic.views3 import UpdateUserPass




#from sitepublic.views import ProduitCreate
from sitepublic.views import TypeProduitCreate
from sitepublic.views import TagProduitCreate
from sitepublic.views import ProduitUpdate
from sitepublic.views import CollectionUpdateItem
from sitepublic.views import CollectionUpdate
from sitepublic.views import ProduitDelete
from sitepublic.views import CollectionDelete

from sitepublic.views import PxxDelete
from sitepublic.views import ProduitDetail
from sitepublic.views import PagePrivee
from sitepublic.views import testform_view

from sitepublic.models import TypeProduit
from sitepublic.models import TagProduit


from . import views
from . import views2
from . import views3



urlpatterns = [
    #path('', views.index, name='index'),
    path('site1', views2.indexsite1, name='indexsite1'),
    #path('', views.index2, name='index2'),
    path('', views.index, name='index'),
    path('createuser/', views.CreateUser, name='CreateUser'),
    path('updateuser/', UpdateUser.as_view(), name='UpdateUser'),
    path('updateuserpass/', UpdateUserPass.as_view(), name='UpdateUserPass'),
    path('createuser2/', views.register, name='register'),
    path('changepassword/', views3.changepassword, name='changepassword'),
    path('login/', views.loginview, name='loginn'),
    path('logout/', views.logout_view, name='logoutt'),
    path('listproduit/', ProduitList.as_view(), name='n_listproduit'),
    path('listcollection/', CollectionList.as_view(), name='n_listcollection'),
    path('listtype/', TypeList.as_view(), name='n_listtype'),
    path('listtag/', TagList.as_view(), name='n_listtag'),    
    path('adproduit/', ProduitCreate.as_view(), name='n_adproduit'),
    path('adcollection/', CollectionCreate.as_view(), name='n_adcollection'),
    path('adtypeproduit/', TypeProduitCreate.as_view(), name='n_adtypeproduit'),
    path('adtagproduit/', TagProduitCreate.as_view(), name='n_adtagproduit'),
    path('updproduit/<int:pk>/', ProduitUpdate.as_view(), name='n_updproduit'),
    path('updtagprod/<int:pk>/', ProduitUpdate.as_view(fields = ['tags_produit',]), name='n_updtagprod'),
    path('updcollectionitem/<int:pk>/', CollectionUpdateItem.as_view(), name='n_upditemcollection'),
    path('updcollection/<int:pk>/', CollectionUpdate.as_view(), name='n_updcollection'),
    path('delproduit/<int:pk>/', ProduitDelete.as_view(), name='n_delproduit'),
    path('delcollection/<int:pk>/', CollectionDelete.as_view(), name='n_delcollection'),
    path('deltype/<int:pk>/', PxxDelete.as_view(model = TypeProduit), name='n_deltype'),
    path('deltag/<int:pk>/', PxxDelete.as_view(model = TagProduit), name='n_deltag'),
    path('detailproduit/<int:pk>/', ProduitDetail.as_view(template_name="sitepublic/site2/detailproduit.html"), name='n_detailproduit'),
    path('detailproduittags/<int:pk>/', ProduitDetail.as_view(template_name="sitepublic/site2/detailproduittags.html"), name='n_detailproduittags'),
    path('detailcollection/<int:pk>/', CollectionDetail.as_view(), name='n_detailcollection'),
    #path('delproduit/<slug:slug>/', ProduitDelete.as_view(), name='n_delproduit'),
    path('zoneprivee/', PagePrivee, name='zoneprivee'),
    path('testform/', testform_view, name='testform'),
    
    
    
    
]




