from django.shortcuts import render

# Create your views here.
#from django.http import HttpResponse

#def home(request):
   # return HttpResponse('<h1 style = "color:red; background-color:black;">Blog Home</h1> <h2>hai koon tu bai</h2>')

def about0(request):
    return render(request, 'blog/about.html')   

#def about1(request):
  # return HttpResponse('<p>Main About, if we go to the main urls which is in the testDjango and if let the sring in the path empty it will display the view in the home page</p>')     


# we are using html templets for websites rather than writing in "HttpResponse".
def home(request):
    return render(request, 'blog/home.html') 


