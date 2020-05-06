from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
STATUS = (
        (0,"InActive"),
        (1,"Active")
)
class Role(models.Model):
    ADMIN = 1
    MANAGER =2
    USER = 3
    ROLE_CHOICES = [
        (ADMIN, 'ADMIN'),
        (MANAGER, 'MANAGER'),
        (USER, 'USER'),
    ]
    role = models.CharField(
        max_length=11,
        default='EMPLOYEE'
    )

    def is_admin(self):
        if self.role == 1:
            return 1
    def is_manger(self):
        if self.role == 2:
            return 1
    def is_employee(self):
        if self.role == 3:
            return 1
    def __str__(self):
       return self.role

class Department(models.Model):
    name = models.CharField(max_length=11)
    status = models.IntegerField(choices=STATUS, default=1)
    updated_on = models.DateTimeField(auto_now= True)
    created_on = models.DateTimeField(auto_now_add=True)
    def __str__(self):
       return self.name


class User(AbstractUser):
    roles = models.ForeignKey(Role,on_delete=models.CASCADE,null=True)
    email = models.EmailField(max_length=254)
    department = models.ForeignKey(Department, on_delete=models.CASCADE,null=True)
    manager = models.ForeignKey('self', on_delete=models.CASCADE,null=True)
    idno = models.CharField(max_length=11)
    name = models.CharField(max_length=255)
    status = models.IntegerField(choices=STATUS, default=1)
    passwordbkp = models.CharField(max_length=255)
    avatar = models.ImageField(upload_to = "media/")
    phone = models.CharField(max_length=255)
    birthday = models.CharField(max_length=255)
    updated_on = models.DateTimeField(auto_now= True)
    created_on = models.DateTimeField(auto_now_add=True)
    

class Leavetype(models.Model):
    leavetype = models.CharField(max_length=255)
    limit = models.IntegerField()
    status = models.IntegerField(choices=STATUS, default=1)
    updated_on = models.DateTimeField(auto_now= True)
    created_on = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.leavetype

class Leave(models.Model):
    reference =  models.ForeignKey(User, on_delete=models.CASCADE)
    leavetype = models.ForeignKey(Leavetype, on_delete=models.CASCADE)
    leavestart = models.CharField(max_length=255,null=True)
    leaveend = models.CharField(max_length=255,null=True)
    reason = models.TextField(null=True)
    subject = models.CharField(max_length=255,null=True)
    comment = models.TextField(null=True)
    status = models.IntegerField(choices=STATUS, default=0)
    updated_on = models.DateTimeField(auto_now= True)
    created_on = models.DateTimeField(auto_now_add=True)
    

class Attendance(models.Model):
    reference =  models.ForeignKey(User, on_delete=models.CASCADE)
    timein = models.CharField(max_length=255)
    timeout = models.CharField(max_length=255)
    totalhour = models.CharField(max_length=255)
    statustimein = models.IntegerField(default=0)
    statustimeout = models.IntegerField(default=0)
    attendancedate = models.DateField(auto_now= False)
    reason = models.TextField()
    comment = models.TextField()
    status = models.IntegerField(choices=STATUS, default=1)
    updated_on = models.DateTimeField(auto_now= True)
    created_on = models.DateTimeField(auto_now_add=True)

class EmployeeNotice(models.Model):
    title =  models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    status = models.IntegerField(choices=STATUS, default=1)
    updated_on = models.DateTimeField(auto_now= True)
    created_on = models.DateTimeField(auto_now_add=True)

class ManagerNotice(models.Model):
    title =  models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    status = models.IntegerField(choices=STATUS, default=1)
    updated_on = models.DateTimeField(auto_now= True)
    created_on = models.DateTimeField(auto_now_add=True)


