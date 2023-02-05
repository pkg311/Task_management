from django.db import models


#

# Create your models here.
class RecurrenceMaster(models.Model):
    Rid = models.AutoField(primary_key=True)
    Rname = models.CharField(null=True, max_length=250)
    AssignedDate = models.DateField()
    EndDate = models.DateField()
    Repeatition = models.CharField(max_length=15)

    def __str__(self):
        return self.Rname

    class meta:
        db_table = "RecurrenceMaster"


class COEMaster(models.Model):
    CID = models.AutoField(primary_key=True)
    CoeDivision = models.CharField(max_length=50)

    def __str__(self):
        return self.CoeDivision

    class meta:
        db_table = "COEMaster"


class RoleMaster(models.Model):
    Role_id = models.AutoField(primary_key=True)
    Rname = models.CharField(max_length=50)

    def __str__(self):
        return self.Rname

    class meta:
        db_table = "RoleMaster"


class UserMaster(models.Model):
    Uid = models.AutoField(primary_key=True)
    Uname = models.CharField(max_length=50)
    email = models.EmailField(max_length=100, null=True)
    password = models.CharField(max_length=20, null=True)
    Utype = models.CharField(max_length=25, default="User", null=True)
    isactive = models.CharField(null=True, default="Inactive", max_length=255)
    CID = models.CharField(null=True, max_length=255)

    def __str__(self):
        return self.Uname

    class meta:
        db_table = "UserMaster"


class TaskMaster(models.Model):
    TId = models.AutoField(primary_key=True)
    Tname = models.CharField(max_length=50)
    TDescription = models.TextField(max_length=500)
    Category = models.CharField(max_length=15)
    CID = models.CharField(null=True, max_length=255)
    Role_id = models.CharField(null=True, max_length=255)
    Tpriority = models.CharField(max_length=10)
    status = models.CharField(max_length=10, default="Unassigned")
    Rname = models.CharField(max_length=255,null=True)
    Attachment = models.FileField(upload_to=None, max_length=254)
    UID = models.CharField(null=True, max_length=255)

    def __str__(self):
        return self.Tname

    class meta:
        db_table = "TaskMaster"

# class MailMaster(models.Model):
#     Email=models.EmailField(primary_key=True)
#     CID = models.ForeignKey(COEMaster, null=True, on_delete=models.CASCADE)
#
#
#     class meta:
#         db_table="MailMaster"
#
#
# class Mail(models.Model):
#     Mail_id=models.IntegerField(primary_key=True)
#     FromEmail = models.EmailField(max_length=200)
#     ToEmail = models.ForeignKey(MailMaster, null=True,on_delete=models.CASCADE)
#     Subject=models.CharField(max_length=255)
#     MailBody=models.TextField(max_length=500)
#
#
#     class meta:
#         db_table = "Mail"
#
