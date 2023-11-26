from django import forms
from .models import Property


class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = ['estate_type', 'location', 'area', 'price']

    # Add custom validation for the estate_type field
    def clean_estate_type(self):
        estate_type = self.cleaned_data.get('estate_type')
        if estate_type not in ['RE', 'CO', 'IN', 'LA']:
            raise forms.ValidationError("Invalid estate type")
        return estate_type

    # Add custom validation for the area field
    def clean_area(self):
        area = self.cleaned_data.get('area')
        if area is not None and area <= 0:
            raise forms.ValidationError("Area must be a positive integer")
        return area

    # Add custom validation for the price field
    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price is not None and price <= 0:
            raise forms.ValidationError("Price must be a positive integer")
        return price


class PropertySearchForm(forms.Form):
    estate_type = forms.ChoiceField(choices=PROPERTY_CHOICES_TUPLE, required=False)
    location = forms.CharField(max_length=255, required=False)

    # Add custom validation for the estate_type field
    def clean_estate_type(self):
        estate_type = self.cleaned_data.get('estate_type')
        if estate_type and estate_type not in ['RE', 'CO', 'IN', 'LA']:
            raise forms.ValidationError("Invalid estate type")
        return estate_type
