# portfoliohub/views.py
#from django.shortcuts import render

#def home(request):
#    return render(request, 'home.html')


from django.shortcuts import render

def home(request):
    imagenes = [
       "https://images.unsplash.com/photo-1522542550221-31fd19575a2d?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8OHx8cG9ydGZvbGlvfGVufDB8fDB8fHww",
       "https://images.unsplash.com/file-1707883121023-8e3502977149image?w=416&dpr=2&auto=format&fit=crop&q=60",
       "https://images.unsplash.com/photo-1674027326254-88c960d8e561?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTJ8fHBhZ2luYXMlMjB3ZWJ8ZW58MHx8MHx8fDA%3D",
       "https://images.unsplash.com/photo-1689421754955-d1595ea47d2b?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8M3x8cGFnaW5hcyUyMG9ubGluZXxlbnwwfHwwfHx8MA%3D%3D",
       "https://images.unsplash.com/photo-1675510183312-d706948b3dbf?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8OHx8cGFnaW5hcyUyMG9ubGluZXxlbnwwfHwwfHx8MA%3D%3D",
       "https://plus.unsplash.com/premium_photo-1683288662019-c92caea8276d?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTN8fHBhZ2luYXMlMjBvbmxpbmV8ZW58MHx8MHx8fDA%3D",
       "https://images.unsplash.com/photo-1740174459726-8c57d8366061?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTR8fHBhZ2luYXMlMjBvbmxpbmV8ZW58MHx8MHx8fDA%3D",
       "https://images.unsplash.com/photo-1663767117374-538a2a266fe1?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTF8fHBhZ2luYXMlMjBvbmxpbmV8ZW58MHx8MHx8fDA%3D",
       "https://images.unsplash.com/photo-1605889551411-d5088704edbe?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTB8fHBhZ2luYXMlMjBvbmxpbmV8ZW58MHx8MHx8fDA%3D",

    ]
    return render(request, 'home.html', {'imagenes': imagenes})
