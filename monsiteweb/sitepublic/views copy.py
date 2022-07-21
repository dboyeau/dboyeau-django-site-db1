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
from sitepublic.models import TagProduit
from sitepublic.models import TypeProduit
from django.contrib.auth.mixins import LoginRequiredMixin




from django.db.models import ProtectedError



def index(request):   
          
    #return HttpResponse("Hello, world. You're at the sitepublic index.")
    #return render(request, 'sitepublic/basefils.html')
    #return render(request, 'sitepublic/essai.html')
    #return render(request, 'sitepublic/site2/index.html')
    return render(request, 'sitepublic/site2/index3.html')

def index2(request):   
    #greeting = "type3500"
    #greeting = "type"    
    #return HttpResponse("Hello, world. You're at the sitepublic index.")
    #return render(request, 'sitepublic/basefils.html')
    #return render(request, 'sitepublic/essai.html')
    #return render(request, 'sitepublic/site2/index.html')
    
    #object_list= Produit.objects.filter(type_produit__name__startswith = greeting)
    #if (request.method) == 'GET':
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
                
    
                    
                    
    


class ProduitList(ListView):
    greeting = "36"
    aaaa=""
    bbbb=""
    #def get(self, request,  *args, **kwargs):
    #    self.temp = request.GET.get('type_produit')
    #    return super(ProduitList, self).get(request, *args, **kwargs)
    #queryset = Produit.objects.filter(type_produit__name__startswith = greeting)
    
    #greeting =self.request.POST['type']
    
    def get_queryset(self):
        #if self.request.method == 'GET' :
            if (self.request.GET.get('type_produit') ) :
                #print (self.request.GET.get('type_produit'))
                #print ('rrrre')
                self.aaaa =  self.request.GET.get('type_produit')
                return Produit.objects.filter(type_produit__name__contains = self.aaaa)
                          
            elif (self.request.GET.get('tag_produit') ) :
                self.bbbb =  self.request.GET.get('tag_produit')
                return Produit.objects.filter(tags_produit__tag_name__contains = self.bbbb)
            else :
                return Produit.objects.all()        
            #return Produit.objects.filter(type_produit__name__contains = self.aaaa)
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        if self.aaaa :
            context['type_produit_filter'] = self.aaaa
        if self.bbbb :
            context['tag_produit_filter'] = self.bbbb
        
        # Add in a QuerySet of all the books
        #context['book_list'] = Book.objects.all()
        return context
    
    
    
    #queryset = Produit.objects.filter(type_produit__name__contains = greeting)
    
    
    
    #def get(self, request,  *args, **kwargs):
        # self.greeting = request.GET.get('type_produit')
        #return super(ProduitList, self).get(request, *args, **kwargs)
        #return HttpResponse(self.greeting)
    
    
    
    
    #queryset = Produit.objects.filter(name__startswith='produit_le_tennis9')
    
    
    
    #queryset = Produit.objects.filter(type_produit__name__startswith = 'type_le_tennis905')
    # exemple depuis l autre cote de la relation ForeignKey
    #Songs.objects.filter(genre__genre='Jazz')
    
    #queryset = Produit.objects.all()
    paginate_by = 20
    template_name="sitepublic/site2/listproduit.html"
    
# ppppppppp
    
class ProduitCreate(CreateView):
    
    model = Produit    
    fields = ['name',
              'slug',
              'photo',
              'fichier',
              'type_produit',
              'tags_produit'
              
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
    
class TypeProduitCreate(LoginRequiredMixin,CreateView):
    
    model = TypeProduit    
    fields = ['name',
            ]
    
    template_name="sitepublic/site2/createproduit.html"
    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form) 
    
class TagProduitCreate(LoginRequiredMixin,CreateView):
    
    model = TagProduit    
    fields = ['tag_name',
                         
            ]
    
    template_name="sitepublic/site2/createproduit.html"
    
    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)
    
class ProduitUpdate(UpdateView):
    
    model = Produit    
    fields = ['name',
              'slug',
              'photo',
              'fichier',
              'type_produit',
              'tags_produit'
              
             ]
    
    template_name="sitepublic/site2/updateproduit.html"
    success_url = reverse_lazy('n_listproduit')
    
# pointp    
class ProduitDelete(DeleteView):
    model = Produit
    template_name="sitepublic/site2/deleteproduit.html"
    def form_valid(self, form):
        
        if (not self.request.user.is_superuser 
            and self.request.user != self.object.created_by) :
            messages.error(self.request, 'Suppression refusée. Cet objet be vous appartient pas.')
            return render(self.request, self.template_name,)
            
        
        #self.object.delete()
        #return HttpResponseRedirect(self.get_success_url())
        return super().form_valid(form)
    
    success_url = reverse_lazy('n_listproduit')
    

from django.contrib import messages    
class PxxDelete(DeleteView):
    #model = Produit
    
    template_name="sitepublic/site2/deleteproduit.html"
    """
    def post(self, request, *args, **kwargs):
        try:
            return self.delete(request, *args, **kwargs)
        except ProtectedError:
            #print ('errorrrrrr')
            messages.error(request, 'Not Deleted because there are linked objects')
            #return HttpResponse("Deletion refusée.")
            #return render(request, self.template_name,{'messages': messages,  })
            return render(request, self.template_name,{})
            
            # render the template with your message in the context
            # or you can use the messages framework to send the message
    """
    def form_valid(self, form):
        
        if (not self.request.user.is_superuser 
            and self.request.user != self.object.created_by) :
            messages.error(self.request, 'Suppression refusée. Cet objet be vous appartient pas.')
            return render(self.request, self.template_name,)
            
        try:
            self.object.delete()
        except ProtectedError:
            messages.error(self.request, 'Not Deleted because there are linked objects')
            return render(self.request, self.template_name,)
        
        
        
        
        
        return HttpResponseRedirect(self.get_success_url()) 
        #return super().form_valid(form)
    
    success_url = reverse_lazy('n_listproduit')
    
    
    
    
class TypeList(ListView):
    model=TypeProduit
    template_name="sitepublic/site2/listtype.html"
    
class TagList(ListView):
    model=TagProduit
    template_name="sitepublic/site2/listtag.html"
    
    
from django.contrib.auth.models import User
#user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')

# At this point, user is a User object that has already been saved
# to the database. You can continue to change its attributes
# if you want to change other fields.
#>>> user.last_name = 'Lennon'
#>>> user.save()

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
            return HttpResponseRedirect('/listproduit/')

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
            # Redirect to a success page
            #return HttpResponseRedirect('/listproduit/')
            #return redirect('/zoneprivee/')  
            return redirect('n_listproduit')
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
    #template_name="sitepublic/site2/zoneprivee.html"
    
    
from django.contrib.auth import logout
from django.shortcuts import redirect
def logout_view(request):
    logout(request)
    # Redirect to a success page.
    #return redirect("https://www.djangoproject.com")
    return redirect('index2')

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

class ProduitDetail(DetailView):
    model = Produit    
    #fields = []
    
    #template_name="sitepublic/site2/detailproduit.html"
    
    
    def get_context_data(self, **kwargs):
        context = super(ProduitDetail, self).get_context_data(**kwargs)
        context['tags_produit'] = TagProduit.objects.filter(
            produit__pk=self.object.pk)
        
        return context


   



    




