# I created this file so that I can understand how forms actually work in django, rather than using just those class-based-views.
# I coundnt understand anything in class-based-views.
from django.forms import ModelForm,formset_factory
from .models import *


class TimerForm(ModelForm):
    class Meta:
        model = Timer
        fields = "__all__"
        exclude = ["published_date"]

class SoundForm(ModelForm):
    class Meta:
        model = Sounds
        fields = "__all__"

class BlockSiteForm(ModelForm):
    class Meta:
        model = BlockSite
        fields = "__all__"


class TasksForm(ModelForm):
    class Meta:
        model = Tasks
        fields = ("task_text",)

    # didnt worked for me.
    # def __init__(self,*args,**kwargs):
    #     # here i just named pomodoro given by user as "selected_timer" and if there is no selected timer in kwargs dictionary then this will return "None".
    #     pomodoro = kwargs.pop("selected_timer",None)
    #     super().__init__(*args,**kwargs)
    #     self.fields["timer"].initial = pomodoro

