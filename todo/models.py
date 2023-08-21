from django.db import models

# Create your models here.
class Record(models.Model):
    title = models.CharField(max_length=250, verbose_name='title')
    description = models.TextField(verbose_name='desc')
    created_time = models.DateTimeField(auto_now_add=True)
    tasks_done = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f'{self.title}'
