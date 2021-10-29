# Generated by Django 3.2.8 on 2021-10-10 13:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('vrsta_prometa', '0001_initial'),
        ('artikli', '0001_initial'),
        ('smjene', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Promet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datum', models.DateField(auto_now_add=True)),
                ('kvantiteta', models.IntegerField()),
                ('ukupno', models.DecimalField(decimal_places=2, max_digits=7)),
                ('artikal', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='artikli.artikal')),
                ('smjena', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='smjene.smjena')),
                ('vrstaPrometa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vrsta_prometa.vrstaprometa')),
            ],
        ),
    ]
