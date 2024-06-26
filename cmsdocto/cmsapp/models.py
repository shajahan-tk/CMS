from django.db import models

# Create your models here.

# EMR settings >>/
class treatmentsitems(models.Model):
    procedure=models.CharField(max_length=25)
    charges=models.CharField(max_length=25)
    procedurecode=models.CharField(max_length=25)
    Duration=models.IntegerField()
    Session=models.CharField(max_length=50)

class drugitems(models.Model):
    unit=models.CharField(max_length=25)

class complaintsitems(models.Model):
    itemname=models.CharField(max_length=50)  
    manufacture=models.CharField(max_length=50)
    boxsize=models.CharField(max_length=50)
    category=models.CharField(max_length=50)
    purchase=models.CharField(max_length=50)
    packingsize=models.CharField(max_length=50)
    taxable=models.CharField(max_length=50)
    recorder=models.CharField(max_length=50)
    batchno=models.CharField(max_length=50)
    salesrate=models.CharField(max_length=50)
    deviceserialsnumber=models.CharField(max_length=50)
    hsncode=models.CharField(max_length=50)

class Addobservation(models.Model):
    observation=models.CharField(max_length=50) 

class Adddiagnosis(models.Model):
    diagnosis=models.CharField(max_length=50)
    diagnosiscode=models.CharField(max_length=50) 

class Addinvestigation(models.Model):
    investigation=models.CharField(max_length=50)  

class Addfrequency(models.Model):
    frequency=models.CharField(max_length=50)           

# //add new patient//
class Add_patients(models.Model):
    Register_id= models.CharField(max_length=50)
    Category= models.CharField(max_length=10)
    First_name= models.CharField(max_length=1000)
    Last_name= models.CharField(max_length=10)
    Record_no= models.IntegerField(null=True)
    Mobile_no= models.CharField(max_length=100, null=True)
    Email= models.EmailField(max_length=1000, null=True)
    State= models.CharField(max_length=1000, null=True)
    City= models.CharField(max_length=1000, null=True)
    Address= models.TextField(max_length=10000, null=True)
    Date_of_birth= models.DateField()
    Age= models.IntegerField()
    Phone_no= models.CharField(max_length=100, null=True)
    Guardian_name= models.CharField(max_length=100, null=True)
    Op_no= models.IntegerField(null=True)
    Passport_no= models.CharField(max_length=100, null=True)
    Date_of_discharge= models.DateField()
    Gender= models.CharField(max_length=100)
    Country= models.CharField(max_length=100, null=True)
    Blood_group= models.CharField(max_length=100, null=True)
    Paitient_remark= models .CharField(max_length=100, null=True)
    Medical_history= models.CharField(max_length=1000, null=True)
    Paitient_group= models.TextField(max_length=1000, null=True)
    Medical_condititon= models.CharField(max_length=1000, null=True)
    Type= models.CharField(max_length=100,null=True)
    Consultation_fee= models.IntegerField()
    Reffered_by= models.CharField(max_length=1000, null=True)
    Occupation= models.CharField(max_length=100, null=True)
    Photo= models.FileField()
    Doctor= models.CharField(max_length=100, null=True)


# General settings >>/

class Clinicprofiles(models.Model):
    Clinic_name= models.CharField(max_length=100)
    Phone_no= models.CharField(max_length=100, null=True)
    Address= models.TextField(max_length=1000, null=True)
    Locality= models.CharField(max_length=100, null=True)
    State= models.CharField(max_length=100)
    Email= models.EmailField()
    Tax= models.CharField(max_length=100, null=True)
    Default_language= models.CharField(max_length=1000)
    Date_start= models.DateField()
    Pharmacy_name= models.CharField(max_length=100, null=True)
    Specialization= models.CharField(max_length=100, null=True)
    Mobile_no= models.CharField(max_length=100, null=True)
    Slogan= models.CharField(max_length=100, null=True)
    Country= models.CharField(max_length=100)
    City= models.CharField(max_length=100)
    Website= models.CharField(max_length=1000, null=True)
    Zip= models.IntegerField()
    Default_Currency= models.CharField(max_length=100)
    Time_zone= models.CharField(max_length=100)
    Pharmacy_licence_code= models.CharField(max_length=100)

class Patientgroup(models.Model):
    patientgroup=models.CharField(max_length=50,null=True)

class Medicalcondition(models.Model):
    medicalcondition=models.CharField(max_length=50,null=True)
    

class taxmodel(models.Model):
    taxname=models.CharField(max_length=50)
    taxpercentage=models.CharField(max_length=50)
      
class Paymentmethod(models.Model):
    Payment_method=models.CharField(max_length=50,null=True)
    discription=models.CharField(max_length=50,null=True)
    
class Documenttype(models.Model):
    document_type=models.CharField(max_length=50)

class Profilepic(models.Model):
    profilepic=models.ImageField(upload_to='srs')



class pharmacysupplier(models.Model):
    suppilername=models.CharField(max_length=50)
    companycode=models.IntegerField()
    companyname=models.CharField(max_length=50)
    contactname=models.CharField(max_length=50)
    email=models.EmailField()
    web=models.CharField(max_length=50)
    phone=models.IntegerField()
    address=models.CharField(max_length=100)
    

class pharmacyunit(models.Model):
    unit=models.CharField(max_length=25)
    

class pharmacyitems(models.Model):
    itemname=models.CharField(max_length=50)  
    manufacture=models.CharField(max_length=50)
    boxsize=models.CharField(max_length=50)
    category=models.CharField(max_length=50)
    purchase=models.CharField(max_length=50)
    packingsize=models.CharField(max_length=50)
    taxable=models.CharField(max_length=50)
    recorder=models.CharField(max_length=50)
    batchno=models.CharField(max_length=50)
    salesrate=models.CharField(max_length=50)
    deviceserialsnumber=models.CharField(max_length=50)
    hsncode=models.CharField(max_length=50)

class pharmacycategory(models.Model):
    itemname=models.CharField(max_length=50)
    manufacture=models.IntegerField()
    description=models.CharField(max_length=50)

class pharmacymanufacture(models.Model):
    manufacture=models.CharField(max_length=50)
    companycode=models.IntegerField()
    companyname=models.CharField(max_length=50)
    contactname=models.CharField(max_length=50)
    email=models.EmailField()
    web=models.CharField(max_length=50)
    phone=models.IntegerField()
    address=models.CharField(max_length=100)

class pharmacysupplier(models.Model):
    suppilername=models.CharField(max_length=50)
    companycode=models.IntegerField()
    companyname=models.CharField(max_length=50)
    contactname=models.CharField(max_length=50)
    email=models.EmailField()
    web=models.CharField(max_length=50)
    phone=models.IntegerField()
    address=models.CharField(max_length=100)
    

class pharmacyunit(models.Model):
    unit=models.CharField(max_length=25)
    

class pharmacyitems(models.Model):
    itemname=models.CharField(max_length=50)  
    manufacture=models.CharField(max_length=50)
    boxsize=models.CharField(max_length=50)
    category=models.CharField(max_length=50)
    purchase=models.CharField(max_length=50)
    packingsize=models.CharField(max_length=50)
    taxable=models.CharField(max_length=50)
    recorder=models.CharField(max_length=50)
    batchno=models.CharField(max_length=50)
    salesrate=models.CharField(max_length=50)
    deviceserialsnumber=models.CharField(max_length=50)
    hsncode=models.CharField(max_length=50)

class pharmacycategory(models.Model):
    itemname=models.CharField(max_length=50)
    manufacture=models.IntegerField()
    description=models.CharField(max_length=50)

class pharmacymanufacture(models.Model):
    manufacture=models.CharField(max_length=50)
    companycode=models.IntegerField()
    companyname=models.CharField(max_length=50)
    contactname=models.CharField(max_length=50)
    email=models.EmailField()
    web=models.CharField(max_length=50)
    phone=models.IntegerField()
    address=models.CharField(max_length=100)


    # pathology ///

class header(models.Model):
    suppliername=models.CharField(max_length=50)


class Addlab(models.Model):
    Lab_name= models.CharField(max_length=100)
    Lab_code=models.CharField(max_length=100)
    Company_name= models.CharField(max_length=100)
    Contact_name=models.CharField(max_length=100)
    Email= models.EmailField()
    Web= models.CharField(max_length=1000)
    Phone= models.CharField(max_length=1000)
    Address= models.CharField(max_length=100)

class Addlabtest(models.Model):
    Test_no= models.IntegerField()
    Test_description= models.CharField(max_length=100)
    Test_charge= models.IntegerField()
    Carry_out= models.CharField(max_length=100)
    Report= models.TextField(max_length=1000)
    Test_type= models.CharField(max_length=100)
    Report_head= models.CharField(max_length=1000)

class Addlabtestpakeges(models.Model):
    Item_name= models.CharField(max_length=1000)
    Manufacture_date= models.DateField()
    Description= models.TextField(max_length=1000)

class Addlabtestdeatail(models.Model):
    labtest_detail=models.CharField(max_length=100)

# dental //

class Dentalwork(models.Model):
    Workname=models.CharField(max_length=50)
    Shade=models.CharField(max_length=50)
    Worktype=models.CharField(max_length=50)
    Alloytype=models.CharField(max_length=50)    

class Addlaboratories(models.Model):
    Labname= models.CharField(max_length=100)   
    Labtype= models.CharField(max_length=100)
    Phone=models.CharField(max_length=50)
    Executive=models.CharField(max_length=50)
    Address=models.CharField(max_length=50)
