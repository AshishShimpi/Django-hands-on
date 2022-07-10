from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request , *args , **kwargs):
    print(args ,kwargs)
    print(request.user)
    # return HttpResponse('<h1> Hello World</h1>') #string of HTML /can be empty
    return render(request , "home.html" , {})

def contact_view (request ,*args , **kwargs):
    # return HttpResponse('<h1>Contact page</h1>') 
    return render(request , "contact.html" , {})


def About_view (request ,*args , **kwargs):
    # return HttpResponse('<h1>About page</h1>') 
    content= {
        "title" : "this is my text ",
        "my_number" : "1234",
        "my_list" : [123 , 453 , 65456 , "ABG"],
        "my_html" : "<h1> Hello World</h1>" 

    }
    return render(request , "About.html" , content)


def Support_view (request ,*args , **kwargs):
    return HttpResponse('<h1>Support page</h1>') 