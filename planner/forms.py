from django.forms import ModelForm, DateInput
from planner.models import Event, File

class EventForm(ModelForm):
  class Meta:
    model = Event
    widgets = {
      'date': DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
    }
    fields = '__all__'

  def __init__(self, *args, **kwargs):
    super(EventForm, self).__init__(*args, **kwargs)
    self.fields['date'].input_formats = ('%Y-%m-%d',)

class FileForm(ModelForm):
    class Meta:
        model = File
        fields = ('description', 'document', )