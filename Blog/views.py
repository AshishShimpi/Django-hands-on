from django.shortcuts import render , get_object_or_404 ,redirect
# from django.http import Http404

from .forms import ArticleForm
from .models import Article
from django.urls import reverse
from django.views.generic import (
    CreateView, 
    DetailView,
    ListView, 
    UpdateView,
    DeleteView
)
# Create your views here.

class ArticleCreateView(CreateView):
    template_name= 'blogs/article_create.html'
    form_class = ArticleForm
    # queryset = Article.objects.all()  

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

class ArticleListView(ListView):
    template_name= 'blogs/article_list.html'
    queryset = Article.objects.all()            #django is going to look for  <Blog>/<modelname>_list.html

class ArticleDetailView(DetailView):
    template_name= 'blogs/article_details.html'
    # queryset = Article.objects.all() 

    def get_object (self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Article ,id=id_)  

class ArticleUpdateView(UpdateView):
    template_name= 'blogs/article_create.html'
    form_class = ArticleForm
    
    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Article ,id=id_)  

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)


class ArticleDeleteView(DeleteView):
    template_name= 'blogs/article_delete.html'
    # success_url='/'

    def get_object (self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Article ,id=id_)  
    #delete view does not delete anything unless it has routing function unlike createview which creates the view regardless of routing function
    def get_success_url(self):
        return reverse("Blog:article_list")
        

# This are normal view methods
# def article_list(request):
#     queryset = Article.objects.all()
#     context={
#         'article':queryset
#     }
#     return render(request , 'blogs/article_list.html' , context)

# def dynamic_article_view(request , my_id):
#     obj = get_object_or_404(Article ,id=my_id)
#     # print(obj)
#     context ={
#         'article' :obj
#     }
#     return render(request , 'blogs/article_details.html' , context)

