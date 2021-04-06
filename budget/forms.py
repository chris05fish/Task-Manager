from django import forms
from budget.models import BudgetEntry
from django.contrib.auth.models import User

options = [
    ('Food','food'),
    ('Clothing', 'clothing'),
    ('Housing', 'housing'),
    ('Education', 'education'),
    ('Entertainment', 'entertainment'),
    ('Other', 'other'),
]

class BudgetEntryForm(forms.ModelForm):
    description = forms.CharField(widget=forms.TextInput(attrs={'size': '80'}))
    category = forms.CharField(widget=forms.Select(choices=options))
    projected = forms.IntegerField(widget=forms.TextInput(attrs={'size': '80'}))
    actual = forms.IntegerField(widget=forms.TextInput(attrs={'size': '80'}))
    class Meta():
        model = BudgetEntry
        fields = ('description', 'category', 'projected', 'actual')
