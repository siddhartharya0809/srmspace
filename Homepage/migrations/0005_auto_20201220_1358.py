# Generated by Django 3.1.3 on 2020-12-20 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Homepage', '0004_auto_20201216_1148'),
    ]

    operations = [
        migrations.AddField(
            model_name='notes',
            name='semester',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='notes',
            name='file_type',
            field=models.FileField(null=True, upload_to='Notes/pdfs/'),
        ),
    ]