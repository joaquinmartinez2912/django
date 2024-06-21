from django import forms

from product.models import (Product, Category, Supplier, ProductReview, ProductImage)

class CategoryForm(forms.ModelForm):
    class Meta:
        Model = Category
        fields = '__all__' 

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["name",
                  "description",
                  "price",
                  "category",
                  "stock"
                  ]
    
        # Personalizan cada campo
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control w-50"}),
            "description": forms.Textarea(attrs={"class": "form-control"}),
            "price": forms.NumberInput(attrs={"class": "form-control"}),
            "category": forms.Select(attrs={"class": "form-control"}),
            "stock": forms.NumberInput(attrs={"class": "form-control",
                                    "required":"required",
                                    "style": "color:red"}
                                    ),
        }

class ProductReviewForm(forms.ModelForm):
    class Meta:
        model = ProductReview
        fields = [
            "product",
            "author",
            "text",
            "rating"
        ]
    
        widgets = {
            'product': forms.Select(attrs={'class': 'form-control custom-class'}),
            'author': forms.Select(attrs={'class': 'form-control custom-class'}),
            'text': forms.TextInput(attrs={'class': 'form-control custom-class'}),
            'rating': forms.NumberInput(attrs={'class': 'form-control custom-class'}),
        }
  
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)

    #     self.fields["product"].initial = self.instance.product.id
    #     self.fields["author"].initial = self.instance.author.id
    #     self.fields["text"].initial = self.instance.text.id
    #     self.fields["rating"].initial = self.instance.rating.id

class SupplierForm(forms.ModelForm):
    class Meta:
        Model = Supplier
        fields = '__all__' 

class ProductImageForm(forms.ModelForm):
    class Meta:
        model = ProductImage 
        fields = [
            'product',
            'image',
            'description',
        ]
        

