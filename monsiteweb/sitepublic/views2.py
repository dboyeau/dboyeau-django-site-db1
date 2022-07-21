

from django.shortcuts import render

def indexsite1(request):   
          
    #return HttpResponse("Hello, world. You're at the sitepublic index.")
    #return render(request, 'sitepublic/basefils.html')
    #return render(request, 'sitepublic/essai.html')
    #return render(request, 'sitepublic/site2/index.html')
    return render(request, 'sitepublic/index.html2')