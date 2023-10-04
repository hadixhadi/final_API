from django.db import models
from django.urls import reverse
# Create your models here.

class Post(models.Model):
    name = models.CharField(max_length=250, null=True, blank=True, verbose_name='نام و نام خانوداگی')
    id_code = models.BigIntegerField(primary_key=True, verbose_name='کد شناسایی')
    father_name = models.CharField(max_length=250, verbose_name='نام پدر')
    history = models.TextField(null=True, blank=True, verbose_name='خاطرات')
    life_history = models.TextField(null=True, blank=True, verbose_name='زندگی نامه')
    devise = models.TextField(null=True, blank=True, verbose_name='وصیت نامه')

    def __str__(self):
        return f"{self.id_code} -- {self.name}"

    def get_absolute_url(self):
        return reverse('delete', kwargs={'id_code': self.id_code})

    class Meta:
        verbose_name_plural = "پست ها"


class Image(models.Model):
    dataClass = models.ForeignKey(Post, on_delete=models.CASCADE,
                                  null=True, blank=True,
                                  related_name='image')
    image = models.ImageField(upload_to="images/")

    class Meta:
        verbose_name_plural = "عکس ها"