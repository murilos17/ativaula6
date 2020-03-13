# Generated by Django 3.0.3 on 2020-03-13 23:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(blank=True, max_length=128, null=True, verbose_name='Nome')),
                ('sigla', models.CharField(blank=True, max_length=128, null=True, verbose_name='Sigla')),
                ('data_inicio', models.DateField(blank=True, null=True)),
                ('descricao', models.TextField()),
            ],
            options={
                'verbose_name': 'Evento',
                'verbose_name_plural': 'Eventos',
            },
        ),
        migrations.CreateModel(
            name='Ingresso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.FloatField(blank=True, null=True, verbose_name='Valor')),
                ('data_inicio', models.DateField(blank=True, null=True)),
                ('descricao', models.TextField()),
            ],
            options={
                'verbose_name': 'Ingresso',
                'verbose_name_plural': 'Ingressos',
            },
        ),
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(blank=True, max_length=128, null=True, verbose_name='Nome')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='E-mail')),
            ],
            options={
                'verbose_name': 'Pessoa',
                'verbose_name_plural': 'Pessoas',
            },
        ),
        migrations.CreateModel(
            name='PessoaFisica',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cpf', models.CharField(blank=True, max_length=128, null=True, verbose_name='CPF')),
                ('pessoa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_evento.Pessoa')),
            ],
            options={
                'verbose_name': 'Pessoa Fisica',
                'verbose_name_plural': 'Pessoa Fisica',
            },
        ),
        migrations.CreateModel(
            name='Inscricao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('evento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_evento.Evento')),
                ('ingresso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_evento.Ingresso')),
                ('pessoa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_evento.Pessoa')),
            ],
            options={
                'verbose_name': 'Inscrição',
                'verbose_name_plural': 'Inscrições',
            },
        ),
        migrations.AddField(
            model_name='ingresso',
            name='realizador',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_evento.Pessoa'),
        ),
        migrations.AddField(
            model_name='evento',
            name='realizador',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_evento.Pessoa'),
        ),
    ]
