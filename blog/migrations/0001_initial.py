# Generated by Django 4.1.7 on 2023-03-22 17:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Autori',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emri_i_punes', models.CharField(max_length=50)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Kategori',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emri', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulli', models.CharField(max_length=255)),
                ('tekst', models.TextField(max_length=300)),
                ('foto', models.ImageField(null=True, upload_to='blog')),
                ('slug', models.SlugField(blank=True)),
                ('autori', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='blog.autori')),
                ('kategori', models.ManyToManyField(to='blog.kategori')),
            ],
        ),
    ]