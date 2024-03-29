# Generated by Django 4.2.3 on 2023-07-12 19:10

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_home_about_summary_home_hero_background_img_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=300, null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=1000, null=True)),
                ('article_status', models.CharField(blank=True, choices=[('publish', 'publish'), ('draft', 'draft')], max_length=100, null=True)),
                ('slug', models.CharField(blank=True, max_length=1000, null=True, unique=True)),
                ('lead_img', models.ImageField(blank=True, null=True, upload_to='media_files/blog')),
                ('lead_img_alt', models.CharField(blank=True, help_text='alt text of an image', max_length=1000, null=True)),
                ('date_created', models.DateField(auto_now_add=True, null=True)),
                ('date_updated', models.DateField(blank=True, null=True)),
                ('content', tinymce.models.HTMLField()),
                ('summary', models.TextField(blank=True, help_text='31 letters max will give a better out look', null=True)),
                ('author', models.CharField(blank=True, default='wmecreatives', max_length=200, null=True)),
                ('author_image', models.ImageField(blank=True, null=True, upload_to='media_files/authorImg')),
                ('author_image_atlt_text', models.CharField(blank=True, help_text='alt text of an image', max_length=1000, null=True)),
                ('youtube_video_link', models.TextField(blank=True, null=True)),
                ('num_views', models.CharField(blank=True, max_length=30, null=True)),
                ('read_time', models.CharField(blank=True, max_length=30, null=True)),
                ('category', models.ManyToManyField(blank=True, to='blog.categories')),
            ],
        ),
    ]
