from django.db import models

# Create your models here.
class Gallery(models.Model):
    title = models.CharField(max_length=16, verbose_name='제목')
    outer = models.CharField(max_length=16, verbose_name='외투')
    top = models.CharField(max_length=16, verbose_name='상의')
    pants = models.CharField(max_length=16, verbose_name='하의')
    acc = models.CharField(max_length=16, verbose_name='악세서리')
    shoes = models.CharField(max_length=16, verbose_name='신발')
    memo = models.CharField(max_length=50, verbose_name='메모')
    gallery_add_dttm = models.DateTimeField(auto_now_add=True, verbose_name='갤러리 추가시간')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'gallery'
        verbose_name = '갤러리'
        verbose_name_plural = '갤러리'

