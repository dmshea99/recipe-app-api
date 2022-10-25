# Generated by Django 3.2.16 on 2022-10-19 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_quote_recipe'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quote',
            name='tag1',
            field=models.CharField(blank=True, choices=[('Inspirational', 'Inspirational'), ('Political', 'Political'), ('Cynical', 'Cynical'), ('Dark', 'Dark'), ('Comical', 'Comical'), ('Literary', 'Literary'), ('Friends', 'Friends'), ('Love', 'Love'), ('Wisdom', 'Wisdom'), ('Poetry', 'Poetry'), ('Health', 'Health')], max_length=50),
        ),
        migrations.AlterField(
            model_name='quote',
            name='tag2',
            field=models.CharField(blank=True, choices=[('Inspirational', 'Inspirational'), ('Political', 'Political'), ('Cynical', 'Cynical'), ('Dark', 'Dark'), ('Comical', 'Comical'), ('Literary', 'Literary'), ('Friends', 'Friends'), ('Love', 'Love'), ('Wisdom', 'Wisdom'), ('Poetry', 'Poetry'), ('Health', 'Health')], max_length=50),
        ),
        migrations.AlterField(
            model_name='quote',
            name='tag3',
            field=models.CharField(blank=True, choices=[('Inspirational', 'Inspirational'), ('Political', 'Political'), ('Cynical', 'Cynical'), ('Dark', 'Dark'), ('Comical', 'Comical'), ('Literary', 'Literary'), ('Friends', 'Friends'), ('Love', 'Love'), ('Wisdom', 'Wisdom'), ('Poetry', 'Poetry'), ('Health', 'Health')], max_length=50),
        ),
    ]
