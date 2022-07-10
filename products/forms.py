from django import forms

from .models import Product


class ProductForm(forms.ModelForm):
    title        = forms.CharField(label='' ,widget = forms.TextInput(attrs={ "placeholder" : "This is title" }))
    # email = forms.EmailField()
    description  = forms.CharField(required = False , widget =forms.Textarea(
                                    attrs= {
                                         "placeholder" : "This is Text area",
                                        "id": "this is id of description",
                                        "class" : "class of des",
                                        "rows" : 20,
                                        "columns" : 100
                                    }                  
                                )
                            )
    price        = forms.DecimalField()
    summary      = forms.CharField(required = False)
    # featured     = forms.CharField(required = False)
    class Meta :
        model = Product
        fields = [
            'title',
            'description',
            'price',
            'summary'
            # 'featured'
        ]
    # def clean_title(self , *args, **kwargs):
    #     title = self.cleaned_data .get("title")
    #     if not "CFE" in title:
    #         raise forms.ValidationError('This is not a CFE title')
    #     if not "news" in title:
    #         raise forms.ValidationError("this is not a news title ")
    #     return title

    # def clean_email(self , *args , **kwargs):
    #     email = self.cleaned_data.get("email")
    #     if not email.endswith("edu"):
    #         raise forms.ValidationError("this is not valid email")
    #     return email



class RawProductForm(forms.Form):
    title        = forms.CharField(label='' ,widget = forms.TextInput(attrs={ "placeholder" : "This is title" }))
    description  = forms.CharField(required = False , widget =forms.Textarea(
                                    attrs= {
                                        "placeholder" : "This is Text area",
                                        "id": "this is id of description",
                                        "class" : "class of des",
                                        "rows" : 20,
                                        "columns" : 100
                                    }                  
                                )
                            )
    price        = forms.DecimalField(initial = 168.25)
    summary      = forms.CharField(required = False)