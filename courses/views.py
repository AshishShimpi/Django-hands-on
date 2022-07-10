from django.shortcuts import render , get_object_or_404 ,redirect
from django.views import View
from .forms import CourseForm
from .models import Course

# This is process of converting fuctional views to class based views

#BASE VIEW Class = VIEW
#HTTP METHODS
class CourseObjectMix(object):
    model = Course
    def get_object(self):
        id = self.kwargs.get("id")
        obj = None
        if id is not None:
            obj= get_object_or_404(self.model, id=id)  
        return obj

class CourseDeleteView(CourseObjectMix , View):
    template_name = 'courses/course_delete.html'
    def get(self, request,id=None, *args, **kwargs):
        context = {}
        obj =self.get_object()
        if obj is not None:
            context['object'] = obj
        return render (request , self.template_name, context)


    def post(self, request,id=None, *args, **kwargs):     
        context = {}
        obj =self.get_object()
        if obj is not None:
            obj.delete()
            context['object']= None
            return redirect('/courses/')
            
        return render(request , self.template_name, context)



class CourseUpdateView(CourseObjectMix, View):
    template_name = 'courses/course_update.html'

    def get(self, request,id=None, *args, **kwargs):
        context = {}
        obj =self.get_object()
        if obj is not None:
            form = CourseForm(instance=obj)
            context['form']= form
            context['object'] = obj
        return render (request , self.template_name, context)

    def post(self, request,id=None, *args, **kwargs):
        context = {}
        obj =self.get_object()
        if obj is not None:
            form = CourseForm(request.POST , instance=obj)
            if form.is_valid():
                form.save()
            context['form']=form
            context['object']= obj
            
        return render(request , self.template_name, context)

class CourseCreateView(View):
    template_name = 'courses/course_create.html'
    
    def get(self, request, *args, **kwargs):
        form = CourseForm()
        context = {'form' : form}
        return render (request , self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            form = CourseForm()
        context = {'form' : form}
        return render(request , self.template_name, context)


class CourseListView(View):
    template_name= 'courses/course_list.html'
    queryset = Course.objects.all()
    
    def get(self , request  , *args , **kwargs ):
        context={'objects':self.queryset}
        return render(request  , self.template_name , context)

class CourseView(View):
    template_name = 'courses/course_details.html'
    def get(self ,request , id = None,*args , **kwargs):
        context = {}
        if id is not None:
            obj= get_object_or_404(Course , id=id)
            context['object']= obj
        return render(request , self.template_name, context)

def my_fbv(request , *args , **kwargs):
    return render (request , 'About.html')