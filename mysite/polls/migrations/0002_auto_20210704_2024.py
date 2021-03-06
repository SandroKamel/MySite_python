# Generated by Django 3.2.3 on 2021-07-04 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Movie_id', models.IntegerField(max_length=10)),
                ('Movie_original_languag', models.CharField(max_length=4)),
                ('Movie_original_title', models.CharField(max_length=100)),
                ('Movie_overview', models.CharField(max_length=1000)),
                ('Movie_popularity', models.IntegerField(max_length=8)),
                ('Movie_poster_path', models.CharField(max_length=100)),
                ('Movie_release_date', models.DateField(blank=True)),
                ('Movie_title', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='Choice',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
    ]
