# Generated by Django 3.1.3 on 2020-12-16 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Homepage', '0003_contact'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notes',
            name='notes_file',
        ),
        migrations.RemoveField(
            model_name='notes',
            name='status',
        ),
        migrations.RemoveField(
            model_name='notes',
            name='upload_date',
        ),
        migrations.RemoveField(
            model_name='notes',
            name='user',
        ),
        migrations.AddField(
            model_name='notes',
            name='title',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='notes',
            name='file_type',
            field=models.FileField(null=True, upload_to='Notes/pdfs'),
        ),
        migrations.DeleteModel(
            name='Signup',
        ),
    ]