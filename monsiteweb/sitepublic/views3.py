from django.forms import PasswordInput
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator



# Create your views here.

from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from django.views.generic import DetailView
from django.views.generic import FormView

from django.urls import reverse_lazy
from sitepublic.models import Produit
from sitepublic.models import Collection
from sitepublic.models import TagProduit
from sitepublic.models import TypeProduit
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from django.db.models import ProtectedError




from django.contrib import messages

from django.core.exceptions import ValidationError
from django.db import IntegrityError

class ProduitCreate(PermissionRequiredMixin,LoginRequiredMixin,CreateView):
    permission_required = ('sitepublic.add_produit',)
    
    model = Produit
    template_name="sitepublic/site2/createproduit.html"    
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
        form.instance.created_by = self.request.user
        
        try:
            return super().form_valid(form)
        except ValidationError:
            messages.error(self.request, 'Not created because slug empty entrez un nom diffrent de -')
            return render(self.request, self.template_name,)
        
        except IntegrityError:
            messages.error(self.request, 'Not created because Integrity error.')
            return render(self.request, self.template_name,)
        
        
        
class CollectionCreate(PermissionRequiredMixin,LoginRequiredMixin,CreateView):
    permission_required = ('sitepublic.add_collection',)
    model = Collection
    template_name="sitepublic/site2/createcollection.html"    
    fields = ['title',
              'slug',
              'photo',
              'description',
              #'item',
              'active',
            ]
    
    
    
    def form_valid(self, form):
        form.instance.created_by = self.request.user
        
        try:
            return super().form_valid(form)
        except ValidationError:
            messages.error(self.request, 'Not created because slug empty entrez un nom diffrent de -')
            return render(self.request, self.template_name,)
        
        except IntegrityError:
            messages.error(self.request, 'Not created because Integrity error.')
            return render(self.request, self.template_name,)
        
        
        
from django.views.generic.detail import SingleObjectMixin       
        
class CollectionDetail(PermissionRequiredMixin,LoginRequiredMixin,SingleObjectMixin, ListView):
    permission_required = ('sitepublic.view_collection',)
    paginate_by = 20
    
    template_name = "sitepublic/site2/collection_detail.html"

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Collection.objects.all())
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['collection'] = self.object
        return context

    def get_queryset(self):
        return self.object.item.all()
    
from django.contrib.auth.models import User 
from django.contrib.auth.forms import  UserChangeForm
from django.contrib.auth.forms import  PasswordChangeForm 
from django.contrib.auth.forms import  SetPasswordForm

from django.contrib.auth.forms import  SetPasswordForm
 

class UpdateUser(LoginRequiredMixin,UpdateView):
    model=User
    #form_class=UserChangeForm
    #form_class=PasswordChangeForm
    #form_class=SetPasswordForm
    #fields ='__all__'
    
    fields = [
        
        
        'first_name',
        'last_name',
        'email',
    ]
    
    template_name='sitepublic/site2/createuser.html'
    success_url = reverse_lazy('index')
    
    def get_object(self):
        return self.request.user
    
    
    
class UpdateUserPass(LoginRequiredMixin,UpdateView):
    model = User
    form_class = PasswordChangeForm
    
    success_url = reverse_lazy('index')
    
    
    def get_object(self):
        return self.request.user
        
    
    
    template_name = 'sitepublic/site2/createuser.html'
    
    
    def get_form_kwargs(self):
        kwargs = super(UpdateUserPass, self).get_form_kwargs()
        kwargs["user"] = kwargs.pop("instance")
        #kwargs["user"] = self.request.user
        return kwargs
    
    def form_valid(self, form):
        form.save()
        # This is a VERY important step!
        update_session_auth_hash(self.request, self.request.user)
        messages.success(self.request, ("Password changed for %s.") % self.object)
        
        return HttpResponseRedirect(self.get_success_url())

    
    
    
    
        
from django.contrib.auth.decorators import login_required        
from django.contrib.auth import update_session_auth_hash 
from django.shortcuts import redirect      
@login_required
def changepassword(request):
    """View function for the user profile, profile.html."""
    # Get the current user's user object
    # user = request.user
    # # Look-up the username in the database
    # current_user_name = User.objects.get(username=user.username)
    # current_user_avatar = UserProfile.objects.get(user=user.id)
    # If ths is a POST, process it as a password update
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            # This is a VERY important step!
            update_session_auth_hash(request, user)
            messages.success(request,
                             'Your password was successfully updated!',
                             extra_tags='alert-success')
            return redirect('index')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'sitepublic/site2/createuser.html', {
        'form': form,
        # 'current_user': current_user_name,
        # 'user_avatar': current_user_avatar
    }) 
    
    
    
    

        
        
        