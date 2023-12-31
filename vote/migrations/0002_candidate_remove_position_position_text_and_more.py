# Generated by Django 4.2.7 on 2023-11-06 09:26

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('vote', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('bio', models.TextField()),
                ('image', models.ImageField(upload_to='candidates/')),
            ],
        ),
        migrations.RemoveField(
            model_name='position',
            name='position_text',
        ),
        migrations.RemoveField(
            model_name='position',
            name='pub_text',
        ),
        migrations.AddField(
            model_name='position',
            name='name',
            field=models.CharField(default=django.utils.timezone.now, max_length=255, unique=True),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Candidates',
        ),
        migrations.AddField(
            model_name='candidate',
            name='position',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vote.position'),
        ),
    ]
