# Generated by Django 4.2.4 on 2023-08-17 17:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('uploader', '0001_initial'),
        ('garagem', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='veiculo',
            name='capa',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='uploader.image'),
        ),
    ]
