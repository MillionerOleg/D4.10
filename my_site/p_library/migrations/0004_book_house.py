# Generated by Django 3.2 on 2021-05-09 14:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('p_library', '0003_rename_copy_count_house_book_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='house',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='p_library.house'),
        ),
    ]
