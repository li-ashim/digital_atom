import datetime

from django import forms
from bootstrap_datepicker_plus import DateTimePickerInput

from .models import Task, UsefulMaterial


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['task_name', 'content', 'deadline', 'id']
        labels =  {'task_name': 'Задача', 'content': 'Содержание', 'deadline': 'Дедлайн'}
        widgets = {'content': forms.Textarea(attrs={'cols': 80}), 
                   'deadline': DateTimePickerInput(options = {
                       'format': 'DD/MM/YYYY HH:MM',
                       'minDate': datetime.datetime.now().strftime("%d/%m/%Y %H:%M")
                    })}
                   

class AddUsefulForm(forms.ModelForm):
    class Meta:
        model = UsefulMaterial
        fields = ['material_type', 'department' , 'title', 'author', 'description']
        widgets = {'description': forms.Textarea(attrs={'cols': 80})}

      