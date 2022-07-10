from django.http import Http404
from django.shortcuts import render ,get_object_or_404, redirect

from .forms import ProductForm , RawProductForm
from .models import Product
# Create your views here.


def show_all_objects(request):
    queryset = Product.objects.all() # Gives list of all objects
    context ={
        'object_list' : queryset
    }
    return render(request  , 'products/products_view.html' , context)


# delete individual objects from database
def product_delete_view(request,my_id):
    obj = get_object_or_404(Product ,id=my_id)
    if request.method == 'POST':
        #confirm delete
        obj.delete()
        return redirect('products/')
    context={
        'object' : obj,

    }
    return render(request , 'products/product_delete.html' , context)

#This form is for directly fetching the object(yet here the method without form fetching the object) and directly looking at any object
def dynamic_lookup_view(request ,my_id):
    # obj = Product.objects.get(id=my_id);
    obj = get_object_or_404(Product ,id=my_id)
    # try:
    #     obj = Product.objects.get(id = my_id)
    # except Product.DoesNotExist:
    #     raise Http404
    context ={
        'object': obj
    }
    return render(request  , 'products/product_lookup.html' , context)

def product_update_view(request , my_id):
    obj = Product.objects.get(id=my_id)
    form = ProductForm(request.POST or None , instance=obj)
    
    if form.is_valid():
        form.save()
        print(form.cleaned_data)
    context={
        'form' : form
    }
    return render(request , 'products/product_create.html', context)


# This function is for showing that form with initial value can be rendered
# def render_initial_data(request):
#     initial_data = {
#         'title': 'this is my title111111'
#     }
#     obj = Product.objects.get(id=1)
#     form =ProductForm(request.POST or None , instance = obj)
#     if form.is_valid():
#         form.save()
        
#     context = {
#         'form':form
#     }
#     return render(request  , "products/product_create.html" , context)


# Raw Form from form.py
# def product_create_view(request):
#     my_form = RawProductForm();
#     if request.method == "POST":
#         my_form = RawProductForm(request.POST);
#         
#         if my_form.is_valid():
#             # new data is good
#             print(my_form.cleaned_data);
#             Product.objects.create(**my_form.cleaned_data);
#         else:
#             print(my_form.errors);
#     context ={
#         'form' : my_form 
#     }
#     return render(request , 'products/product_create.html' , context)


# def product_create_view(request):
#     # print(request.GET);
#     # print(request.POST);
#     # if request.method == "POST":
#     my_new_title=request.POST.get('title');
#     Product.objects.create(my_new_title);
# 
#     print(my_new_title)
#    
#  context ={}
#     return render(request , 'products/product_create.html' , context)

#  creating form from model.py which will be diectly saved 
# model imported in forms.py then class is created then it is imported in views 
# which will be rendered by Django itself into html............just chill

def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        #print data before creating a new instance 
        print(form.cleaned_data);
        # for showing a blank form after saving 
        form = ProductForm()

    context ={
        'form': form
    }
    return render(request , 'products/product_create.html' , context)


# def product_detail_view (request ):
#     obj = Product.objects.get(id=1);
#     # context ={
#     #     'title' : obj.title,
#     #     'description' : obj.description
#     # }
#     context ={
#         'object': obj
#     }
#     return render(request , 'products/detail.html' , context)