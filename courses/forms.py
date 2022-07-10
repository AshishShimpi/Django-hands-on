from django import forms
from .models import Course


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = [
            'title'
        ]
    def clean_title(self):
        title  = self.cleaned_data.get('title')
        if title.lower() == 'ass':
            raise forms.ValidationError('This is not a valid Title')
        return title
