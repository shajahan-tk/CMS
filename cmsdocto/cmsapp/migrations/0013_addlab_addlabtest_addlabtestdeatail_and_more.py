# Generated by Django 5.0.6 on 2024-05-20 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmsapp', '0012_alter_profilepic_profilepic'),
    ]

    operations = [
        migrations.CreateModel(
            name='Addlab',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Lab_name', models.CharField(max_length=100)),
                ('Lab_code', models.CharField(max_length=100)),
                ('Company_name', models.CharField(max_length=100)),
                ('Contact_name', models.CharField(max_length=100)),
                ('Email', models.EmailField(max_length=254)),
                ('Web', models.CharField(max_length=1000)),
                ('Phone', models.CharField(max_length=1000)),
                ('Address', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Addlabtest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Test_no', models.IntegerField()),
                ('Test_description', models.CharField(max_length=100)),
                ('Test_charge', models.IntegerField()),
                ('Carry_out', models.CharField(max_length=100)),
                ('Report', models.TextField(max_length=1000)),
                ('Test_type', models.CharField(max_length=100)),
                ('Report_head', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Addlabtestdeatail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('labtest_detail', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Addlabtestpakeges',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Item_name', models.CharField(max_length=1000)),
                ('Manufacture_date', models.DateField()),
                ('Description', models.TextField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Documenttype',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document_type', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='header',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('suppliername', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Medicalcondition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medicalcondition', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Patientgroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patientgroup', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Paymentmethod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Payment_method', models.CharField(max_length=50, null=True)),
                ('discription', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='pharmacycategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('itemname', models.CharField(max_length=50)),
                ('manufacture', models.IntegerField()),
                ('description', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='pharmacyitems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('itemname', models.CharField(max_length=50)),
                ('manufacture', models.CharField(max_length=50)),
                ('boxsize', models.CharField(max_length=50)),
                ('category', models.CharField(max_length=50)),
                ('purchase', models.CharField(max_length=50)),
                ('packingsize', models.CharField(max_length=50)),
                ('taxable', models.CharField(max_length=50)),
                ('recorder', models.CharField(max_length=50)),
                ('batchno', models.CharField(max_length=50)),
                ('salesrate', models.CharField(max_length=50)),
                ('deviceserialsnumber', models.CharField(max_length=50)),
                ('hsncode', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='pharmacymanufacture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manufacture', models.CharField(max_length=50)),
                ('companycode', models.IntegerField()),
                ('companyname', models.CharField(max_length=50)),
                ('contactname', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('web', models.CharField(max_length=50)),
                ('phone', models.IntegerField()),
                ('address', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='pharmacysupplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('suppilername', models.CharField(max_length=50)),
                ('companycode', models.IntegerField()),
                ('companyname', models.CharField(max_length=50)),
                ('contactname', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('web', models.CharField(max_length=50)),
                ('phone', models.IntegerField()),
                ('address', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='pharmacyunit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='taxmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taxname', models.CharField(max_length=50)),
                ('taxpercentage', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='add_patients',
            name='Consultation_fee',
            field=models.IntegerField(),
        ),
    ]