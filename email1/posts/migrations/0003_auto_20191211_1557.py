# Generated by Django 3.0 on 2019-12-11 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_posts_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='category',
            field=models.ManyToManyField(default=0, related_name='categories', to='posts.Category'),
        ),
    ]