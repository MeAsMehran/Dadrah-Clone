from django.db import models
from my_users.models import NormalUser, Lawyer

# Create your models here.



class NormalUserFunctions:

    class Question(models.Model):
        id = models.AutoField(primary_key=True)
        title = models.CharField(max_length=500, verbose_name='Question Title', blank=False)
        question_text = models.TextField(max_length=1000, verbose_name='Question Text', blank=False)
        date = models.DateField(auto_now_add=True, blank=False)
        user_id = models.ForeignKey('my_users.NormalUser', on_delete=models.CASCADE)


    class InPersonConsultation(models.Model):
        id = models.AutoField(primary_key=True)
        province = models.CharField(max_length=200)
        city = models.CharField(max_length=200)
        subject = models.CharField(max_length=1000)
        lawyer_id = models.ForeignKey('my_users.Lawyer', on_delete=models.CASCADE)

    class PhoneConsultation(models.Model):
        id = models.AutoField(primary_key=True)
        location = models.CharField(max_length=200, blank=False)
        subject = models.CharField(max_length=1000, blank=False)
        lawyer_id = models.ForeignKey('my_users.Lawyer', on_delete=models.CASCADE)



    class CheckingDocuments(models.Model):
        pass

    class Transaction(models.Model):
        id = models.AutoField(primary_key=True)
        payment_conditions = [('pending', 'Pending'), ('successful', 'Successful'), ('failed', 'Failed')]

        amount = models.DecimalField(max_length=12, decimal_places=2, max_digits=10)
        description = models.TextField(max_length=500, blank=True)
        payment_gate = models.CharField(max_length=50)
        payment_status = models.CharField(max_length=20, choices=payment_conditions, default='pending')
        transaction_id = models.CharField(max_length=100, unique=True)
        user_id = models.ForeignKey('my_users.NormalUser', on_delete=models.CASCADE)
        created_date = models.DateTimeField(auto_now_add=True)
        updated_date = models.DateTimeField(auto_now_add=True)
        # payment_status = models.CharField(max_length=20,
        #                           choices=[('pending', 'Pending'), ('successful', 'Successful'), ('failed', 'Failed')],
        #                           default='pending')

    class Notifications(models.Model):      # ????????
        pass

    class Tickets(models.Model):
        id = models.AutoField(primary_key=True, )
        ticket_license = models.CharField(max_length=10, blank=False, )
        title = models.CharField(max_length=500, blank=False, )
        date = models.DateField(auto_now_add=True, )
        time = models.TimeField(auto_now_add=True, )
        user_id = models.ForeignKey('my_users.NormalUser', on_delete=models.CASCADE)




class LawyerFunctions:

    class Answer(models.Model):
        id = models.AutoField(primary_key=True)
        answer = models.TextField(max_length=1500, verbose_name='Answer', blank=False)
        date = models.DateField(auto_now_add=True, blank=False)
        time = models.DateTimeField(auto_now_add=True, blank=False)
        lawyer_id = models.ForeignKey('my_users.Lawyer',related_name='answer', on_delete=models.CASCADE)



    class Degree(models.Model):
        id = models.AutoField(primary_key=True  )
        title = models.CharField(max_length=100, blank=False)
        university = models.CharField(max_length=200, blank=False)
        lawyer_id = models.ForeignKey('my_users.Lawyer', on_delete=models.CASCADE)


    class Skills(models.Model):
        id = models.AutoField(primary_key=True, )
        title = models.CharField(max_length=75, blank=True)
        info = models.TextField(blank=False)


    class SocialMedia(models.Model):
        id = models.AutoField(primary_key=True)
        instagram = models.URLField(unique=True, blank=True, )
        telegram = models.URLField(unique=True, blank=True, )
        lawyer_id = models.ForeignKey('my_users.Lawyer', on_delete=models.CASCADE)
        
    
    class Location(models.Model):
        id = models.AutoField(primary_key=True)
        province = models.CharField(max_length=50, blank=False, )
        city = models.CharField(max_length=50, blank=True, )
        user_id = models.ForeignKey('my_users.Lawyer', on_delete=models.CASCADE)


    class InPersonConsultation(models.Model):
        id = models.AutoField(primary_key=True)
        location = models.CharField(max_length=75, blank=False)
        subject = models.CharField(max_length=1000, blank=False)



    class PhoneConsultation(models.Model):
        id = models.AutoField(primary_key=True)
        location = models.CharField(max_length=75, blank=False)
        subject = models.CharField(max_length=1000, blank=False)
        lawyer = models.ForeignKey('my_users.Lawyer', on_delete=models.CASCADE)

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
