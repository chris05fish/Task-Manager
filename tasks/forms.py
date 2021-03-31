from django import forms
from tasks.models import TasksEntry
from django.contrib.auth.models import User

options = [
    ('Home','home'),
    ('School', 'school'),
    ('Work', 'work'),
    ('Self improvement', 'self improvement'),
    ('Other', 'other'),
]

class TasksEntryForm(forms.ModelForm):
	description = forms.CharField(widget=forms.TextInput(attrs={'size': '80'}))
	category = forms.CharField(widget=forms.Select(choices=options))
	class Meta():
		model = TasksEntry
		fields = ('description', 'category')
