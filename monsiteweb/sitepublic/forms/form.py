from django.contrib.auth.models import User

from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from sitepublic.models import Collection

# normallement a supprimer
class UserForm(ModelForm):
    class Meta:
        model = User
        #fields = ['username', 'email','first_name', 'last_name', 'password']
        fields = ['username', 'password', 'email']
       
            
    def __init__(self, *args, **kwargs):
        # first call the 'real' __init__()
        super(UserForm, self).__init__(*args, **kwargs)
        # then do extra stuff:
        self.fields['username'].help_text = 'help'
        self.fields['password'].widget = forms.PasswordInput(attrs={'placeholder': 'password'})
        self.fields['password'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget = forms.EmailInput(attrs={'placeholder': 'email'})
        

# normallement aussi a supprimer        
class UserCreationForm2(UserCreationForm):
    class Meta:
        model = User
        #fields = ['username', 'password', ]
        fields = ['username',  ]
        
    def __init__(self, *args, **kwargs):
        # first call the 'real' __init__()
        super(UserCreationForm, self).__init__(*args, **kwargs)
        # then do extra stuff:
        self.fields['username'].widget.attrs['class'] = 'form-control'
        #self.fields['password'].widget = forms.PasswordInput(attrs={'placeholder': 'password'})
        #self.fields['password'].widget.attrs['class'] = 'form-control'
        
    password1 = forms.CharField(label=("Password"),
        widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label=("Password confirmation"),
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        help_text=("Enter ........ the same password as above, for verification."))
        
        
    
    
    pass        
        
       

class User2Form(forms.Form):
    fields = ['username', 'password',]
    username = forms.CharField(max_length=100)
    email = forms.EmailField(label=u"Votre adresse mail")
    password = forms.CharField(max_length=100)
    
    
    
    
class UserLoginForm(ModelForm):
    class Meta:
        model = User
        #fields = ['username', 'email','first_name', 'last_name', 'password']
        fields = ['username', 'password',]
       
            
    def __init__(self, *args, **kwargs):
        # first call the 'real' __init__()
        super(UserLoginForm, self).__init__(*args, **kwargs)
        # then do extra stuff:
        #self.fields['username'].help_text = 'help'
        #self.fields['username'].help_text = 'help'
        self.fields['username'].widget = forms.TextInput(attrs={'placeholder': 'username', 'class': 'form-control'})
        self.fields['password'].widget = forms.PasswordInput(attrs={'placeholder': 'password', 'class': 'form-control'})
        #self.fields['password'].widget.attrs['class'] = 'form-control'
        
        
from django.core.exceptions import ValidationError     
class TestForm(forms.Form):
#class TestForm(ModelForm):

    error_messages = {
        'password_mismatch': ("Les 2 champs sont differents."),
    }

    """
    class Meta:
        model = User
        #fields = ['username', 'email','first_name', 'last_name', 'password']
        #fields = ['username', 'password',]
        fields = ['username', ]
    """
    
    
    """   
    nom_champ1 = forms.CharField(
                #label=("llll"),
                max_length=100,
                widget=forms.PasswordInput(attrs={'class': 'form-control'})
            )
    """
    nom_champ1 = forms.CharField(max_length=100, required = False)
    nom_champ2 = forms.CharField(max_length=100, 
        help_text=("Entrez la même valeur que dans champ1 pour vérification ."))
    
    nom_champ3 = forms.EmailField(max_length=100, )
    
    def clean_nom_champ2(self):
        nom_champ1 = self.cleaned_data.get("nom_champ1")
        nom_champ2 = self.cleaned_data.get("nom_champ2")
        if nom_champ1 != nom_champ2:
                      
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        return self.cleaned_data 
        #return nom_champ2
    
    
    
    
    
    
        #nom_champ1 = forms.CharField(max_length=50,label=("label_nom_champ1"),
            #widget=forms.TextInput(attrs={'class': 'form-control'}))
            
            
from django.forms.widgets import CheckboxSelectMultiple            
class CollectionFormItem(ModelForm):
    class Meta:
        model = Collection
        fields = [
              
              'item',
              
                          
             ]
        widgets={"item": CheckboxSelectMultiple, }
        
    
    
    
    
    
    