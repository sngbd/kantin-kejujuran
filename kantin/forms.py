from django import forms


class CreateForm(forms.Form):
    name = forms.CharField(max_length=100)
    description = forms.CharField(widget=forms.Textarea)
    price = forms.IntegerField(min_value=0, label="Price (IDR)")
    image = forms.CharField(max_length=500, required=True, label="Image (URL)")


class BalanceBox(forms.Form):
    balance = forms.IntegerField(min_value=0, label="Insert balance")
    

choices = [
    ('-', '-----'), 
    ('DTASC', 'Date Created (Ascending)'), ('DTDSC', 'Date Created (Descending)'),
    ('NMASC', 'Product Name (Ascending)'), ('NMDSC', 'Product Name (Descending)')
    ]


class SortChoice(forms.Form):
    sort = forms.ChoiceField(choices=choices, widget=forms.Select(attrs={"onChange":'this.form.submit()'}))