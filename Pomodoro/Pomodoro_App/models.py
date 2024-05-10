from django.db import models

# below validator is imported here becasue PositiveIntegerField is not working.
from django.core.validators import MinValueValidator
from django.urls import reverse
from django.utils import timezone

# Create your models here.
# Creating models based on this website ---> https://pomofocus.io/app
# We created 5 models ---> 5 different tables. 
# 1) Timer
# 2) Tasks
# 3) Sound
# 4) Theme ---> Background theme
# 5) Notification
# 7) Block website

# TODO: Make models more complex once basic website is made.




# connect sound with timer model ----> no need
class Sounds(models.Model):
    sound = models.FileField(upload_to="Audio/uploads/%Y/%m/%d/")
    sound_name = models.CharField(max_length=20)

    def __str__(self):
        return f"Music: {self.sound_name}"

    def get_sounds_url(self):
        # here our 'sound' is FileField attribute thats why we did self.sound.url cause FileField
        # attribute contains the url of the media file.
        return self.sound.url


def get_now_date():
    return timezone.now()

class Timer(models.Model):
    pomodoro = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0)])
    short_break = models.PositiveIntegerField(default=0)
    long_break = models.PositiveIntegerField(default=0)
    auto_start_pomodoros = models.BooleanField(default=False)
    auto_start_breaks = models.BooleanField(default=False)
    number_of_interval = models.PositiveIntegerField(default=0)
    published_date = models.DateTimeField(
        "date published",
        default=get_now_date,
    )

    def __str__(self):
        return f"Pomodoro: {self.pomodoro} ---- Short-Break: {self.short_break} and Long-Break: {self.long_break} ---- Total number of interval: {self.number_of_interval}"

    def get_absolute_url(self):
        return reverse("Pomodoro:settings")


# No need to connect Tasks with Timer in a many-to-one relationship. 
# TODO: You need to figure out how to update and delete the task on the timer.html page without reloading the page again each time.
class Tasks(models.Model):
    task = models.CharField(max_length=100,name = "task_text")
    compeleted = models.BooleanField(default = False)
    published_date = models.DateTimeField("date published", default=get_now_date)
    end_time = models.DateTimeField("Time completed",default = get_now_date)

    def __str__(self):
        return f"Task: {self.task_text}"
    
    def endTime(self):
        if self.compeleted:
            self.end_time = timezone.now()
            
    def get_absolute_url(self):
        return reverse("Pomodoro:index")



# "Theme" model is not related to anybody right now.
class Theme(models.Model):
    IMAGE = "IM"
    COLOR = "CO"
    STATUS_CHOICE = [(IMAGE, "Image"), (COLOR, "Color")]
    status = models.CharField(max_length=2, choices=STATUS_CHOICE, default=COLOR)
    theme_image = models.ImageField(upload_to="Images/uploads/%Y/%m/%d/")
    theme_color = models.CharField(max_length=10)
    theme_name = models.CharField(max_length=20)

    def __str__(self):
        return f"Theme-name: {self.theme_name}"

    # TODO: to complete below class visit https://adamj.eu/tech/2020/03/25/django-check-constraints-one-field-set/
    class Meta: ...


# "Notification" is in many-to-one relationship with "Timer".
# Why "many-to-one" ?
# Because, with same timer ongoing if user set "send_when = evey 5min" --> this means notification will be sent to user every 5min for the same timer.
class Notification(models.Model):
    timer = models.ForeignKey(Timer, on_delete=models.CASCADE)
    notification_text = models.CharField(
        max_length=100, default="Chutiye timer baj gaya"
    )
    # send_when : every or last (5min or ...)
    send_when = models.CharField(max_length=5)
    send_time = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"Notification: '{self.notification_text}' will be sent to you {self.send_when}: {self.send_time}min"


#  We dont need to connect blocksite with timer in many to one relationship.
class BlockSite(models.Model):
    site_url = models.URLField()
    quote = models.CharField(
        max_length=300,
        default="When I let go of what I am, I become what I might be. ~Lao Tzu",
    )

    def __str__(self):
        return f"Website: {self.site_url}"
