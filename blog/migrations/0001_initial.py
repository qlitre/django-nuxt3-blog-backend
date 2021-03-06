# Generated by Django 3.2.13 on 2022-05-14 23:02

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import mdeditor.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='カテゴリ名')),
                ('slug', models.SlugField(max_length=32, verbose_name='スラッグ')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='タグ名')),
                ('slug', models.SlugField(max_length=32, verbose_name='スラッグ')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40, verbose_name='タイトル')),
                ('slug', models.SlugField(max_length=40, verbose_name='スラッグ')),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to='', verbose_name='サムネイル')),
                ('description', models.TextField(verbose_name='紹介文')),
                ('main_text', mdeditor.fields.MDTextField()),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='作成日')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='blog.category', verbose_name='カテゴリ')),
                ('tag', models.ManyToManyField(blank=True, to='blog.Tag', verbose_name='タグ')),
            ],
            options={
                'ordering': ('-created_at',),
            },
        ),
    ]
