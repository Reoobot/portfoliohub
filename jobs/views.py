# from django.shortcuts import render

# Create your views here.



#from django.http import HttpResponse

#def index(request):
#    return HttpResponse("¡Hola desde portfolios index JOBS!")


from django.shortcuts import render

def job_list(request):
    return render(request, 'jobs/list.html')
