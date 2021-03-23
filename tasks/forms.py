from django import forms
from journal.models import TasksEntry

class TasksEntryForm(forms.ModelForm):
	description = forms.CharField(widget=forms.TextInput(attrs={'size': '80'}))
	category = forms.CharField(widget=forms.TextInput(attrs={'size': '80'}))
	class Meta():
		model = TasksEntry
		fields = ('description', 'category')
