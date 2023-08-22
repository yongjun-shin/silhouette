# Generated by Django 4.2.3 on 2023-08-21 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Gallery",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=16, verbose_name="제목")),
                ("outer", models.CharField(max_length=16, verbose_name="외투")),
                ("top", models.CharField(max_length=16, verbose_name="상의")),
                ("pants", models.CharField(max_length=16, verbose_name="하의")),
                ("acc", models.CharField(max_length=16, verbose_name="악세서리")),
                ("shoes", models.CharField(max_length=16, verbose_name="신발")),
                ("memo", models.CharField(max_length=300, verbose_name="메모")),
                (
                    "gallery_add_dttm",
                    models.DateTimeField(auto_now_add=True, verbose_name="갤러리 추가시간"),
                ),
            ],
            options={
                "verbose_name": "갤러리",
                "verbose_name_plural": "갤러리",
                "db_table": "gallery",
            },
        ),
    ]