from django.db import models

# Create your models here.

class Note(models.Model):
    title = models.CharField(max_length=120)
    body = models.TextField(blank=True)
    created = models.DateTimeField( auto_now_add=True)
    

    # class Meta:
    #     verbose_name = _("note")
    #     verbose_name_plural = _("notes")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("note_detail", kwargs={"pk": self.pk})
