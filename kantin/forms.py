from django import forms


class CreateForm(forms.Form):
    name = forms.CharField(label='', max_length=100, widget=forms.TextInput(
       attrs={
           'class': 'form-control',
           'placeholder': 'Name',
       }))
    description = forms.CharField(label='', widget=forms.Textarea(
       attrs={
           'class': 'form-control',
           'placeholder': 'Description',
       }))
    price = forms.IntegerField(min_value = 0, label='', widget=forms.NumberInput(
       attrs={
           'class': 'form-control',
           'placeholder': 'Price (IDR)',
       }))
    image = forms.CharField(max_length=1000, required=True, label='', widget=forms.TextInput(
        attrs={
           'class': 'form-control',
           'placeholder': 'Image (URL)',
        }))


class BalanceBox(forms.Form):
    balance = forms.IntegerField(min_value = 0, label='', widget=forms.NumberInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Insert balance',
        }))
    

choices = [
    ('-', '-----'), 
    ('DTASC', 'Date Created (Ascending)'), ('DTDSC', 'Date Created (Descending)'),
    ('NMASC', 'Product Name (Ascending)'), ('NMDSC', 'Product Name (Descending)')
    ]


class SortChoice(forms.Form):
    sort = forms.ChoiceField(label='', choices=choices, widget=forms.Select(
        attrs={
            'onChange':'this.form.submit()',
            'class': 'form-control',
        }))
