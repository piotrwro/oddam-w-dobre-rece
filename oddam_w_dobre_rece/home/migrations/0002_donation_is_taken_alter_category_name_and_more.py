# Generated by Django 4.0.2 on 2022-03-09 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='donation',
            name='is_taken',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=255, verbose_name='nazwa kategorii'),
        ),
        migrations.AlterField(
            model_name='institution',
            name='categories',
            field=models.ManyToManyField(to='home.Category', verbose_name='Kategorie darów'),
        ),
        migrations.AlterField(
            model_name='institution',
            name='description',
            field=models.TextField(verbose_name='Opis'),
        ),
        migrations.AlterField(
            model_name='institution',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Nazwa instytucji'),
        ),
    ]
