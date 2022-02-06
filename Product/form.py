from django import forms
from Branch.models import Branch

from Product.models import Bad_Product, Category, Product, Product_Type, Returned_Product

class CategoryForm(forms.ModelForm):
    """Form definition for Category."""

    class Meta:
        """Meta definition for Categoryform."""

        model = Category
        fields = '__all__'
        
class ProductTypeForm(forms.ModelForm):
    """Form definition for Product_Type."""

    class Meta:
        """Meta definition for Product_Typeform."""

        model = Product_Type
        fields = '__all__'
        
class ProductForm(forms.ModelForm):
    """Form definition for Product."""
    branches = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                                queryset=Branch.objects.all(),required=False)
    
    class Meta:
        """Meta definition for Productform."""

        model = Product
        fields = '__all__'

class BadProductForm(forms.ModelForm):
    """Form definition for BadProduct."""

    class Meta:
        """Meta definition for BadProductform."""

        model = Bad_Product
        fields = ("product","branch","qty")
    
class ReturnedProductForm(forms.ModelForm):
    """Form definition for ReturnedProduct."""

    class Meta:
        """Meta definition for ReturnedProductform."""

        model = Returned_Product
        fields ='__all__'
        widgets = {
            "date_of_purchase" : forms.widgets.DateInput(attrs={'type':'date'}),
            "date_of_return"  : forms.widgets.DateInput(attrs={'type':'date'})     
        }



