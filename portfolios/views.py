#from django.shortcuts import render

# Create your views here.


#from django.http import HttpResponse

#def index(request):
#    return HttpResponse("¡Hola desde portfolios index!")


from django.shortcuts import render

def portfolio_list(request):
    return render(request, 'portfolios/list.html')
