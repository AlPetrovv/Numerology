# Generated by Django 4.1.7 on 2023-03-24 15:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('psychomatrix', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Celebrities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=55, unique=True)),
                ('birth_day', models.DateField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='PsychomatrixBaseCelebrity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('celebrity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='psychomatrixbase_in_celebrity', to='psychomatrix.celebrities')),
                ('characteristic', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='psychomatrixbase_in_celebrity', to='psychomatrix.psychomatrixbasecontent')),
            ],
        ),
        migrations.CreateModel(
            name='PsychomatrixAdditionalCelebrity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('celebrity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='psychomatrixadditional_in_celebrity', to='psychomatrix.celebrities')),
                ('characteristic', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='psychomatrixadditional_in_celebrity', to='psychomatrix.psychomatrixadditionalcontent')),
            ],
        ),
        migrations.AddField(
            model_name='psychomatrixadditionalcontent',
            name='celebrities',
            field=models.ManyToManyField(related_name='psychomatrixadditional', through='psychomatrix.PsychomatrixAdditionalCelebrity', to='psychomatrix.celebrities'),
        ),
        migrations.AddField(
            model_name='psychomatrixbasecontent',
            name='celebrities',
            field=models.ManyToManyField(related_name='psychomatrixbase', through='psychomatrix.PsychomatrixBaseCelebrity', to='psychomatrix.celebrities'),
        ),
    ]
