from django.db import models

# Create your models here.
class TopLiked(models.Model):
    title = models.CharField(max_length = 256)
    amount = models.IntegerField(default = 0)

    class Meta:
        ordering = ['-amount']

    def __str__(self):
        return "%s - %d" % (self.title, self.amount)
