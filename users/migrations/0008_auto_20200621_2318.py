# Generated by Django 2.2.7 on 2020-06-21 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_delete_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='specialty',
            old_name='title',
            new_name='title_kg',
        ),
        migrations.AddField(
            model_name='specialty',
            name='title_ru',
            field=models.CharField(default=1, max_length=100, verbose_name='Специальность'),
            preserve_default=False,
        ),
    ]
