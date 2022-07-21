
from django.forms import PasswordInput
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator

# Create your views here.

from django.http import HttpResponse
from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from django.views.generic import DetailView
from django.urls import reverse_lazy
from sitepublic.models import Produit
from sitepublic.models import Collection
from sitepublic.models import TagProduit
from sitepublic.models import TypeProduit
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin




from django.db.models import ProtectedError
from django.contrib import messages

from django.core.exceptions import ValidationError



def index(request):   
          
    
    return render(request, 'sitepublic/site2/index4.html')

def index2(request):   
    greeting =''
    if (request.GET.get('type_produit_filter')) :
        greeting = request.GET.get('type_produit_filter')
        object_list_t= Produit.objects.filter(type_produit__name__contains = greeting)
    else :    
       object_list_t= Produit.objects.all()
       
       
    paginator = Paginator(object_list_t, 20) # Show 5 objets per page
    page = request.GET.get('page')
    
    #return HttpResponse (greeting)
    object_list = paginator.get_page(page)
    
    
    
    return render(request, 'sitepublic/site2/listproduit2fonc.html',
                {'object_list': object_list, 'type_produit_filter': greeting },
            )
                
    
                    
                    
    


class ProduitList(PermissionRequiredMixin,ListView):
    permission_required = ('sitepublic.view_produit',)
    greeting = "36"
    aaaa=""
    bbbb=""
    cccc=""
    
    
    def get_queryset(self):
        
        if (self.request.GET.get('type_produit') ) :
            
            self.aaaa =  self.request.GET.get('type_produit')
            return Produit.objects.filter(type_produit__name__contains = self.aaaa)
                        
        elif (self.request.GET.get('tag_produit') ) :
            self.bbbb =  self.request.GET.get('tag_produit')
            return Produit.objects.filter(tags_produit__tag_name__contains = self.bbbb)
        
        elif (self.request.GET.get('nom_produit') ) :
            self.cccc =  self.request.GET.get('nom_produit')
            return Produit.objects.filter(name__contains = self.cccc)
        
        else :
            return Produit.objects.all()        
            
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        if self.aaaa :
            context['type_produit_filter'] = self.aaaa
        if self.bbbb :
            context['tag_produit_filter'] = self.bbbb
        if self.cccc :
            context['nom_produit_filter'] = self.cccc
        
        # Add in a QuerySet of all the books
        #context['book_list'] = Book.objects.all()
        return context
    
    paginate_by = 20
    template_name="sitepublic/site2/listproduit.html"
    

    
class ProduitCreate(PermissionRequiredMixin,CreateView):
    permission_required = ('sitepublic.add_produit',)
    model = Produit    
    fields = ['name',
              'slug',
              'photo',
              'fichier',
              'type_produit',
              'description',
              'url',
              'date_fin',
              'tags_produit',
              'active',
              
             ]
    
    template_name="sitepublic/site2/createproduit.html"
    def post(self, request, *args, **kwargs):
        
        if request.user.is_authenticated :
            print ('le user est authentifie')
            print (request.user.pk)
            #obj.created_by = self.request.user
            #Produit.objects.created_by = request.user.pk
            print (Produit.name)
            #t=Produit (name= 'nnnbbbb', created_by =request.user)
            #t.save
            """
            form = ProduitForm()
            if form.is_valid():
                name = form.cleaned_data.get('name')
                slug = form.cleaned_data.get('slug')
                type_produit = form.cleaned_data.get('type_produit')
                
                created_by = self.request.user
                produit = Produit.objects.create_produit(name, slug, 
                            created_by
                    )
                produit.save()
         """   
        
        return super().post(self, request, *args, **kwargs)
    
        """
        def form_valid(self, form):
            obj = form.save(commit=False)
            obj.created_by = self.request.user
            obj.save()        
            return http.HttpResponseRedirect(self.get_success_url())
        """   
    
class TypeProduitCreate(PermissionRequiredMixin,CreateView):
    permission_required = ('sitepublic.add_typeproduit',)
    
    #qs = TypeProduit.objects.all()
    #print (qs)
    
    def get_context_data(self, **kwargs):
        context = super(TypeProduitCreate, self).get_context_data(**kwargs)
        context['type_produit'] = TypeProduit.objects.all()
            
        
        return context
    
    model = TypeProduit    
    fields = ['name',
            ]
    
    template_name="sitepublic/site2/createproduit.html"
    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form) 
    
class TagProduitCreate(PermissionRequiredMixin,LoginRequiredMixin,CreateView):
    permission_required = ('sitepublic.add_tagproduit',)
    def get_context_data(self, **kwargs):
        context = super(TagProduitCreate, self).get_context_data(**kwargs)
        context['tag_produit'] = TagProduit.objects.all()
            
        
        return context
    
    
    
    model = TagProduit    
    fields = ['tag_name',
                         
            ]
    
    template_name="sitepublic/site2/createproduit.html"
    
    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)
    
    
    
    
class ProduitUpdate(PermissionRequiredMixin,UpdateView):
    permission_required = ('sitepublic.change_produit',)       
    template_name="sitepublic/site2/updateproduit.html"
    model = Produit    
    fields = ['name',
              'slug',
              'photo',
              'fichier',
              'type_produit',
              'description',
              'url',
              'date_fin',
              'tags_produit',
              'active',
              
    
              
             ]
    
    def form_valid(self, form):
        
        if (not self.request.user.is_superuser 
            and self.request.user != self.object.created_by) :
            messages.error(self.request, 'Update refusé. Cet objet be vous appartient pas.')
            return render(self.request, self.template_name,)
            
        
        return super().form_valid(form)
    
    
    #success_url = reverse_lazy('n_listproduit')
    
#    
class ProduitDelete(PermissionRequiredMixin,DeleteView):
    permission_required = ('sitepublic.delete_produit',)
    model = Produit
    template_name="sitepublic/site2/deleteproduit.html"
    def form_valid(self, form):
        
        if (not self.request.user.is_superuser 
            and self.request.user != self.object.created_by) :
            messages.error(self.request, 'Suppression refusée. Cet objet ne vous appartient pas.')
            return render(self.request, self.template_name,)
            
        
        return super().form_valid(form)
    
    success_url = reverse_lazy('n_listproduit')
    

from django.contrib import messages    
class PxxDelete(PermissionRequiredMixin,DeleteView):
    permission_required = ('sitepublic.delete_typeproduit', 'sitepublic.delete_tagproduit')
    #model = Produit
    # model dans url.py
    
    
    
    
    
    template_name="sitepublic/site2/deleteproduit.html"
    
    
    def post(self, request, *args, **kwargs):
        if (self.model == TagProduit) :
            pk = kwargs.get('pk')
            #print (pk)
            p1 = TagProduit.objects.get(pk=pk)
            p2 = p1.produit_set.all()
            p3 = len(p2)
            if (p3 != 0) :
                #print ('deletion refusee')
                messages.error(self.request, 'Suppression refusée. Il y a encore des objets liés.')
                return render(self.request, self.template_name,{'p2' : p2})  
    
    
        return super().post(self, request, *args, **kwargs)

    
    def form_valid(self, form, ):
        
        if (not self.request.user.is_superuser 
            and self.request.user != self.object.created_by) :
            messages.error(self.request, 'Suppression refusée. Cet objet ne vous appartient pas.')
            return render(self.request, self.template_name,)
            
        try:
            self.object.delete()
        except ProtectedError:
            messages.error(self.request, 'Not Deleted because there are linked objects')
            return render(self.request, self.template_name,)
        
        
        
            
        
        
        return HttpResponseRedirect(self.get_success_url()) 
        
    
    success_url = reverse_lazy('n_listproduit')
    
    
    
    
class TypeList(PermissionRequiredMixin,ListView):
    permission_required = ('sitepublic.view_typeproduit',)
    model=TypeProduit
    template_name="sitepublic/site2/listtype.html"
    
class TagList(PermissionRequiredMixin,ListView):
    permission_required = ('sitepublic.view_tagproduit',)
    model=TagProduit
    template_name="sitepublic/site2/listtag.html"
    
    
from django.contrib.auth.models import User

from django.http import HttpResponseRedirect
from .forms.form import UserForm
from .forms.form import User2Form 
from django.contrib.auth.models import User 
def CreateUser(request):
    #form = UserForm()
    #a
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        #form = User2Form(request.POST)
        form = UserForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            email = form.cleaned_data.get('email')
            user = User.objects.create_user(username, email, password,)
            user.save()
            #aa=form.cleaned_data
            #uuu=aa.get('username')
            
            
            return HttpResponseRedirect('/listproduit/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = UserForm()
        #pass

    
    
    
    #a
    

    return render(request, 'sitepublic/site2/createuser.html', {'form': form})

    pass



#...
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
#...

def login(request, **kwargs):
    
    #...
    PasswordInput
    

from .forms.form import UserCreationForm2

def register(request):
    if request.method == 'POST':
        f = UserCreationForm2(request.POST)
        if f.is_valid():
            f.save()
            messages.success(request, 'Account created successfully')
            #return HttpResponseRedirect('/listproduit/')
            #return HttpResponseRedirect('//')

    else:
        f = UserCreationForm2   ()

    return render(request, 'sitepublic/site2/register.html', {'form': f})


from .forms.form import UserLoginForm
from django.contrib.auth import authenticate, login

def loginview(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            
            #return redirect('n_listproduit')
            return redirect('index')
        #...
        else:
        # Return an 'invalid login' error message.
            form = UserLoginForm()
            messages.error(request, 'Pas de correspondance trouvée')
            return render(request, 'sitepublic/site2/login.html',{'form': form} )
                    #return HttpResponse('<h1>user non authentifie</h1>')
        
    form = UserLoginForm()
    return render(request, 'sitepublic/site2/login.html', {'form': form})



#from django.views.generic import View
def PagePrivee(request):
    #class PagePrivee(View):
    b = 10
    a ='a'
    queryset = {'a':150000}
    
    
    return render(request, 'sitepublic/site2/zoneprivee.html', queryset)
    
    
    
from django.contrib.auth import logout
from django.shortcuts import redirect
def logout_view(request):
    logout(request)
    
    return redirect('index')

from .forms.form import TestForm
def testform_view(request):
    
    if request.method == 'POST':
        f = TestForm(request.POST)
        """
        fichier = open("/home/db1/data.txt", "a")
        fichier.write("Bonjour monde")
        fichier.write(request)
        fichier.close()
        print (request.method)
        
        """
        
        if f.is_valid():
            messages.success(request, 'Resultat successfully')
            return HttpResponseRedirect('/listproduit/')

    else:
            f = TestForm()
        
          
    return render(request, 'sitepublic/site2/testform.html', {'form': f})

class ProduitDetail(PermissionRequiredMixin,DetailView):
    permission_required = ('sitepublic.view_produit',)
    model = Produit    
        
    
    def get_context_data(self, **kwargs):
        context = super(ProduitDetail, self).get_context_data(**kwargs)
        context['tags_produit'] = TagProduit.objects.filter(
            produit__pk=self.object.pk)
        
        return context



class CollectionList(PermissionRequiredMixin,LoginRequiredMixin,ListView):
    permission_required = ('sitepublic.view_collection',)
    greeting = "36"
    aaaa=""
    bbbb=""
    cccc=""
    
    
    def get_queryset(self):
        
        if (self.request.GET.get('type_produit') ) :
            
            self.aaaa =  self.request.GET.get('type_produit')
            return Collection.objects.filter(type_produit__name__contains = self.aaaa)
                        
        elif (self.request.GET.get('tag_produit') ) :
            self.bbbb =  self.request.GET.get('tag_produit')
            return Collection.objects.filter(tags_produit__tag_name__contains = self.bbbb)
        
        elif (self.request.GET.get('nom_collection') ) :
            self.cccc =  self.request.GET.get('nom_collection')
            return Collection.objects.filter(title__contains = self.cccc)
        
        else :
            return Collection.objects.all()        
            
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        if self.aaaa :
            context['type_produit_filter'] = self.aaaa
        if self.bbbb :
            context['tag_produit_filter'] = self.bbbb
        if self.cccc :
            context['nom_collection_filter'] = self.cccc
        
        # Add in a QuerySet of all the books
        #context['book_list'] = Book.objects.all()
        return context
    
    paginate_by = 20
    template_name="sitepublic/site2/listcollection.html"
    
    
from django.forms.models import modelform_factory 
from django.forms.widgets import CheckboxSelectMultiple 
from django.forms import Textarea 
from .forms.form import CollectionFormItem 
    
class CollectionUpdateItem(PermissionRequiredMixin,UpdateView):
    permission_required = ('sitepublic.change_collection',)
            
    template_name="sitepublic/site2/updatecollection.html"
    model = Collection 
    form_class = CollectionFormItem
    
    
    
       
    
    
    
    
    def form_valid(self, form):
        
        if (not self.request.user.is_superuser 
            and self.request.user != self.object.created_by) :
            messages.error(self.request, 'Update refusé. Cet objet ne vous appartient pas.')
            return render(self.request, self.template_name,)
            
        
        return super().form_valid(form)
    
    
    #success_url = reverse_lazy('n_listproduit')
    
# 

class CollectionUpdate(PermissionRequiredMixin,UpdateView):
    permission_required = ('sitepublic.change_collection',)
            
    template_name="sitepublic/site2/updatecollection.html"
    model = Collection 
    #form_class = CollectionFormItem
    #form = CollectionForm()
    
    
    fields = ['title',
              'slug',
              'photo',
              'description',
              'item',
              'active',
              
    
              
             ]
    
      
    def form_valid(self, form):
        
        if (not self.request.user.is_superuser 
            and self.request.user != self.object.created_by) :
            messages.error(self.request, 'Update refusé. Cet objet be vous appartient pas.')
            return render(self.request, self.template_name,)
            
        
        return super().form_valid(form)
    
    
    #success_url = reverse_lazy('n_listproduit')
    
# 

class CollectionDelete(PermissionRequiredMixin,DeleteView):
    permission_required = ('sitepublic.delete_collection',)
    model = Collection
    template_name="sitepublic/site2/deletecollection.html"
    def form_valid(self, form):
        
        if (not self.request.user.is_superuser 
            and self.request.user != self.object.created_by) :
            messages.error(self.request, 'Suppression refusée. Cet objet ne vous appartient pas.')
            return render(self.request, self.template_name,)
            
        
        return super().form_valid(form)
    
    success_url = reverse_lazy('n_listcollection')   


    




