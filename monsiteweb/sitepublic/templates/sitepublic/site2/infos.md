infos

widgets de formulaires

https://docs.djangoproject.com/fr/4.0/ref/forms/widgets/#styling-widget-instances

validation de formulaires et de champs
https://docs.djangoproject.com/fr/4.0/ref/forms/validation/

Utilisation du système d’authentification de Django¶
https://docs.djangoproject.com/fr/4.0/topics/auth/default/

Utilisation du système d’authentification de Django
https://docs.djangoproject.com/fr/4.0/topics/auth/default/#all-authentication-views

Sommaire de la documentation Django
https://docs.djangoproject.com/fr/4.0/contents/

[docs]class UserCreationForm(forms.ModelForm):
https://docs.djangoproject.com/en/1.8/_modules/django/contrib/auth/forms/


Code source de django.forms.widgets
https://docs.djangoproject.com/fr/2.2/_modules/django/forms/widgets/

Utilisation des formulaires
https://docs.djangoproject.com/fr/4.0/topics/forms/

interressant pour filtrer
https://www.caktusgroup.com/blog/2018/10/18/filtering-and-pagination-django/


Pour sauver les images avec uptae view

<form method="POST" enctype="multipart/form-data"> - it worked, thank you – 
Radek
Apr 10, 2019 at 17:48
Had the same issue, adding <enctype="multipart/form-data"> to the form solved it! – 
David
Sep 5, 20


Django messages

https://docs.djangoproject.com/fr/4.0/ref/contrib/messages/


pour form_valid

https://docs.djangoproject.com/fr/4.0/topics/class-based-views/generic-editing/






Django override get_form on CreateView
views.py
class MyModelAdd(CreateView):
    model = MyModel

    def get_form(self):
        type_form = self.request.GET.get('type')
        if type_form == 'pf':
            self.form_class = PFForm
        else:
            self.form_class = PJForm
        return super(MyModelAdd, self).get_form()