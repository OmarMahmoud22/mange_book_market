from django import forms
from .models import Books ,Category

class BookForm(forms.ModelForm):
    class Meta:
        model = Books
        fields = ['title',
        'author',
        'photo_book',
        'photo_author',
        'pages',
        'price',
        'rental_price_day',
        'rental_period',
        'total_rental',
        'status',
        'category',
        'body'
        ]

        widgets = {
            'title' : forms.TextInput(attrs={'class':'form-control'}),
            'body' : forms.Textarea(attrs={'class':'form-control'}),
            'author' : forms.TextInput(attrs={'class':'form-control'}),
            'photo_book' : forms.FileInput(attrs={'class':'form-control'}),
            'photo_author' : forms.FileInput(attrs={'class':'form-control'}),
            'pages' : forms.NumberInput(attrs={'class':'form-control'}),
            'price' : forms.NumberInput(attrs={'class':'form-control'}),
            'rental_price_day' : forms.NumberInput(attrs={'class':'form-control' , 'id' : 'rentalprice'}),
            'rental_period' : forms.NumberInput(attrs={'class':'form-control' , 'id' : 'rentaldays'}),
            'total_rental' : forms.NumberInput(attrs={'class':'form-control' , 'id':'total'}),
            'status' : forms.Select(attrs={'class':'form-control'}),
            'category' : forms.Select(attrs={'class':'form-control'}),

        }

class CateoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
        
