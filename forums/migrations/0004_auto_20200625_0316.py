# Generated by Django 2.2.7 on 2020-06-24 21:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('forums', '0003_comment_forum'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='forum',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='forums.Forum', verbose_name='Форум'),
        ),
    ]
