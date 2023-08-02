from django.db import models

# Create your models here.
class Clothes(models.Model):
    clothes_type = models.CharField(max_length=16, verbose_name='옷 종류')
    clothes_name = models.CharField(max_length=30, verbose_name='옷 이름')
    image_path = models.ImageField(upload_to='media/clothes', null=True, verbose_name='옷 사진')
    clothes_add_dttm = models.DateTimeField(auto_now_add=True, verbose_name='옷 추가시간')

    def __str__(self):
        return self.clothes_name

    class Meta:
        db_table = 'clothes'
        verbose_name = '옷'
        verbose_name_plural = '옷'

class Accessory(models.Model):
    acc_name = models.CharField(max_length=30, verbose_name='악세서리 이름')
    image_path = models.ImageField(upload_to='media/acc', null=True, verbose_name='악세서리 사진')
    acc_add_dttm = models.DateTimeField(auto_now_add=True, verbose_name='악세서리 추가시간')

    def __str__(self):
        return self.acc_name

    class Meta:
        db_table = 'accessory'
        verbose_name = '악세서리'
        verbose_name_plural = '악세서리'

class Shoes(models.Model):
    shoes_name = models.CharField(max_length=30, verbose_name='신발 이름')
    image_path = models.ImageField(upload_to='media/shoes', null=True, verbose_name='신발 사진')
    shoes_add_dttm = models.DateTimeField(auto_now_add=True, verbose_name='신발 추가시간')

    def __str__(self):
        return self.shoes_name

    class Meta:
        db_table = 'shoes'
        verbose_name = '신발'
        verbose_name_plural = '신발'