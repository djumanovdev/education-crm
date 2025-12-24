from django.db import models


class Teacher(models.Model):
    last_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    
    def __str__(self):
        return f'{self.last_name} {self.first_name}'
    


class Student(models.Model):
    
    full_name = models.CharField(max_length=150)
    phone_nummer = models.CharField(max_length=15, unique=True)
    status = models.BooleanField(default=False)
    is_risk = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.full_name
    
    
class Group(models.Model):
    name = models.CharField(max_length=120)
    teacher = models.ForeignKey(Teacher,on_delete=models.SET_NULL,related_name='groups',null=True,blank=True)
    students = models.ManyToManyField(Student,related_name='groups',blank=True)
    
    def __str__(self):
        return self.name
    
    
class Attendance(models.Model):
    
    STATUS_CHOICES = [
        ('present', 'Kelgan'),
        ('absent', 'Kelmagan'),
        ('late', 'Kechikkan'),
        ('excused', 'Sababli'),
    ]
    
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=50,choices=STATUS_CHOICES,default='absent')
    
    
    def __str__(self):
        return f"{self.group} -- {self.student}"
    
class Payment(models.Model):
    
    STATUS_CHOICES = [
        ('paid','tulangan'),
        ('unpaid','tulanmagan')
    ]
    
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    month = models.DateField()
    status = models.CharField(max_length=50,choices=STATUS_CHOICES,default='unpaid')
    
    
    def __str__(self):
        return f"{self.student} {self.month} {self.status}"
    