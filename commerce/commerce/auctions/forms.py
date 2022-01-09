from django import forms

from .models import User, category, listing, bid, comment

class createListing(forms.ModelForm):
    class Meta:
        model = listing
        fields = [
            #'poster',
            'title',
            'description',
            'startPrice',
            'image',
            'categorized'
        ]
        widgets = {
            #spent 2 hours trying to figure out why my form is not saving to the db and it was all cuz of this user hidden input form :))
            #'poster': forms.HiddenInput(attrs={
                #'class': "form-control",
                #'style': '',
                #'placeholder': ''
            #}),
            'title': forms.TextInput(attrs={
                'class': "form-control",
                'style': '',
                'placeholder': 'item name / title'
            }),
            'description': forms.Textarea(attrs={
                'class': "form-control",
                'style': '',
                'placeholder': 'Item description',
                'rows': 7
            }),
            'startPrice': forms.NumberInput(attrs={
                'class': "form-control",
                'style': '',
                'placeholder': 'Starting price'
            }),
            'image': forms.URLInput(attrs={
                'class': "form-control",
                'style': '',
                'placeholder': 'Image url (optional)'
            }),
            'categorized': forms.Select(attrs={
                'class': "form-control",
                'style': '',
                'selected': 'Choose a category (optional)'

            })
        }

class addComment(forms.ModelForm):
    class Meta:
        model = comment
        fields = [
            'commento'
        ]
        widgets = {
            'commento': forms.TextInput(attrs={
                'class': "form-control",
                'style': '',
                'placeholder': 'Add a comment'
            })
        }
    

class createBiding(forms.ModelForm):
    #want to link this
    def __init__(self, minAmount, *args, **kwargs):
        super(createBiding, self).__init__(*args, **kwargs)
        self.fields['bidAmount'] = forms.DecimalField(min_value=minAmount,widget=forms.NumberInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px; margin-top: 7px;',
                'placeholder': 'Place your bid'}))
    #with this # i think its done dekita !
    class Meta:
        model = bid
        fields = [
            'bidAmount'
        ]
        #canIdoThis = {
            #'bidAmount': forms.DecimalField(min_value=minAmount)
        #}
        """
        widgets = {
            'bidAmount': forms.NumberInput(attrs={
                'class': "form-control",
                'style': '',
                'placeholder': 'Place your bid'
            })
        }
        """
    
