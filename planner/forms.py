from django.forms import ModelForm, DateInput
from planner.models import Event, File

class EventForm(ModelForm):
  class Meta:
    model = Event
    widgets = {
      # 'start_time': DateInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
      # 'end_time': DateInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
      'date': DateInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%d'),
    }
    fields = '__all__'

  def __init__(self, *args, **kwargs):
    super(EventForm, self).__init__(*args, **kwargs)
    self.fields['date'].input_formats = ('%Y-%m-%d',)
    # self.fields['end_time'].input_formats = ('%Y-%m-%dT%H:%M',)

class FileForm(ModelForm):
    class Meta:
        model = File
        fields = ('description', 'document', )