# Generated by Django 3.1.2 on 2021-05-25 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='album',
            options={'verbose_name': 'Disque'},
        ),
        migrations.AlterModelOptions(
            name='artist',
            options={'verbose_name': 'Aritste'},
        ),
        migrations.AlterModelOptions(
            name='booking',
            options={'verbose_name': 'Réservation'},
        ),
        migrations.AlterModelOptions(
            name='contact',
            options={'verbose_name': 'Prospect'},
        ),
        migrations.AlterField(
            model_name='album',
            name='available',
            field=models.BooleanField(default=True, verbose_name='disponible'),
        ),
        migrations.AlterField(
            model_name='album',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='date de création'),
        ),
        migrations.AlterField(
            model_name='album',
            name='picture',
            field=models.ImageField(upload_to='store/static/store/img', verbose_name="chemin d'image"),
        ),
        migrations.AlterField(
            model_name='album',
            name='reference',
            field=models.IntegerField(null=True, verbose_name='Réference'),
        ),
        migrations.AlterField(
            model_name='album',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Titre'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='contacted',
            field=models.BooleanField(default=False, verbose_name='Demande traité?'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name="date d'envoie"),
        ),
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(max_length=200, verbose_name='email'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Nom'),
        ),
    ]
