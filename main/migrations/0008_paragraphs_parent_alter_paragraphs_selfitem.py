# Generated by Django 4.2 on 2023-04-07 09:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_alter_paragraphs_selfitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='paragraphs',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='main.paragraphs'),
        ),
        migrations.AlterField(
            model_name='paragraphs',
            name='selfitem',
            field=models.ManyToManyField(blank=True, null=True, to='main.paragraphs', verbose_name='Дочерние пункты'),
        ),
    ]
