from django.forms import ModelForm
from basictodo.models import Todo



class TodoForm(ModelForm):

    class Meta():
        model = Todo
        fields = ['title','memo','important']
