from django.db import models
from ..users.models import Users

# Create your models here.



class NormalUserFunctions:

    class Question(models.Model):

        title = models.CharField(max_length=500, verbose_name='Question Title', blank=False)
        info = models.TextField(max_length=1000, verbose_name='Question Text', blank=False)
        date = models.DateField(auto_now_add=True, blank=False)
        answer = models.ForeignKey(Users.NormalUser, on_delete=models.CASCADE)
        lawyerAnswered = models.ForeignKey('Answer', on_delete=models.CASCADE)

    class InPersonConsultation(models.Model):
        province = models.CharField(max_length=200)
        city = models.CharField(max_length=200)
        subject = models.CharField(max_length=1000)
        lawyer = models.ForeignKey(Users.Lawyer, on_delete=models.CASCADE)

    class PhoneConsultation(models.Model):

        location = models.CharField(max_length=200, blank=False)
        subject = models.CharField(max_length=1000, blank=False)
        lawyer = models.ForeignKey(Users.Lawyer, on_delete=models.CASCADE)



    class CheckingDocuments(models.Model):
        pass

    class Transaction(models.Model):



        payment_conditions = [('pending', 'Pending'), ('successful', 'Successful'), ('failed', 'Failed')]

        amount = models.DecimalField(max_length=12, decimal_places=0)
        description = models.TextField(max_length=500, blank=True)
        payment_gate = models.CharField(max_length=50)
        payment_status = models.CharField(max_length=20, choices=payment_conditions, default='pending')
        transaction_id = models.CharField(max_length=100, unique=True)
        user = models.ForeignKey(Users.NormalUser, on_delete=models.CASCADE)
        created_date = models.DateTimeField(auto_now_add=True)
        updated_date = models.DateTimeField(auto_now_add=True)
        # payment_status = models.CharField(max_length=20,
        #                           choices=[('pending', 'Pending'), ('successful', 'Successful'), ('failed', 'Failed')],
        #                           default='pending')

    class Notifications(models.Model):      # ????????
        pass

    class Tickets(models.Model):
        ticket_license = models.CharField(max_length=10, blank=False)
        title = models.CharField(max_length=500, blank=False)
        date = models.DateField(auto_now_add=True)
        time = models.TimeField(auto_now_add=True)




class LawyerFunctions:

    class Answer(models.Model):

        answer = models.TextField(max_length=1500, verbose_name='Answer', blank=False)
        date = models.DateField(auto_now_add=True, blank=False)
        time = models.DateTimeField(auto_now_add=True, blank=False)
        lawyer = models.ForeignKey(Users.Lawyer, on_delete=models.CASCADE)



    class Degree(models.Model):

        title = models.CharField(max_length=100, blank=False)
        university = models.CharField(max_length=200, blank=False)
        lawyer = models.ForeignKey(Users.Lawyer, on_delete=models.CASCADE)


    class Skills(models.Model):

        title = models.CharField(blank=True)
        info = models.TextField(blank=False)
        lawyer = models.ForeignKey(Users.Lawyer, on_delete=models.CASCADE)




