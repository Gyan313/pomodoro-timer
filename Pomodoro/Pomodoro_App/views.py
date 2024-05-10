from django.shortcuts import render, redirect,get_object_or_404
from django.http import Http404
from .models import *
from .forms import *
from django.core import serializers
from django.urls import reverse_lazy

# TODO: There's going to be 2 initial template, I need to build ---->
#      1) timer.html ---> displaying the data stored in databases.
#      2) settings.html ---> contains all the models which we have to take input from user.
#                 a) We need to wrap every model for which we need user input in one form.


# this is the view which provides the settings for the user to fill.
def settings(request):
    timer_form = TimerForm()
    sounds = Sounds.objects.all()
    blocksite_form = BlockSiteForm()

    context = {
        "timer_form": timer_form,
        "blocksite_form":blocksite_form,
        "sounds": sounds,
    }
    return render(request, "Pomodoro_App\\settings.html", context)


# view for the actuall timer.
def pomodoro_timer(request):

    # default values(any random values) for variables.
    pomodoro_sound,breaks_sound = [1,1]

    try:
        # the topmost pomodoro is going to the timer.js
        pomodoro = Timer.objects.order_by("-published_date").first()
        serialized_data = serializers.serialize("json", [pomodoro])
    except Http404:
        return render(
            request,
            "Pomodoro_App\\settings.html",
            {"error_message": "No Pomodoro to start."},
        )
    

    # getting the input from the form which is in settings.html form.
    if request.method == "POST":
        time_form = TimerForm(request.POST)
        task_form = TasksForm(request.POST)
        sound = Sounds.objects.all().first()
        pomodoro_sound = request.POST.get('pomodoro_selected_audio',sound.get_sounds_url())
        breaks_sound = request.POST.get('breaks_selected_audio',sound.get_sounds_url())

        if time_form.is_valid():
            time_form.save()
        elif task_form.is_valid():
            # saving the pomodoro which is presently running before creating task.
            task = task_form.save(commit=False)
            task.timer = pomodoro
            task.save()
        else:
            # redirected to homepage
            return redirect("/")
        
    # If no input to the form is provided by the user, than below sound is gonna go off.
    sound = Sounds.objects.all().first()
    if pomodoro_sound == 1:
        pomodoro_sound = sound.get_sounds_url()
    if breaks_sound == 1:
        breaks_sound = sound.get_sounds_url()

    # below are the values that are being sent to the timer.html template to be rendered.
    latest_task_list = Tasks.objects.all() 

    if request.method == "GET":
        print(request.GET)
        # task = Tasks.objects.get(id = task_id)
        # print(task)

    context = {
        "pomodoro": pomodoro,
        "serialized_data": serialized_data,
        "pomodoro_sound":pomodoro_sound,
        "break_sound":breaks_sound,
        "task_form":TasksForm(),
        "latest_task_list":latest_task_list,
    }

    return render(request, "Pomodoro_App\\timer.html", context)

def deleteTask(request,task_id):
    task = get_object_or_404(Tasks,pk = task_id)
    task.delete()
    # redirect("Pomodoro:timer") ----> this will take me to the previous instance of the pomodoro_timer
    #  view.
    return redirect("Pomodoro:timer")
