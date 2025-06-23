from django import forms
from django.contrib.auth.models import User
from .models import Asset, AssetRequest

class AssetForm(forms.ModelForm):
    assigned_to = forms.ModelChoiceField(
        queryset=User.objects.all(),
        required=False,
        empty_label="Not Assigned",
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Asset
        fields = ['name', 'description', 'category', 'department', 'status', 'assigned_to', 'image']
        widgets = {
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Enter a description of the asset...'
            }),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'department': forms.Select(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'})
        } 

class AssetRequestForm(forms.ModelForm):
    purpose = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 3,
            'placeholder': 'Please explain why you need this asset...'
        }),
        required=True
    )

    class Meta:
        model = AssetRequest
        fields = ['purpose'] 