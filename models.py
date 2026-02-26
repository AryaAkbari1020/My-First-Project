from django.db import models


class User(models.Model):

    full_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)  
    birth_date = models.DateField()
    national_id = models.CharField(max_length=10)  

    def __str__(self):
        return self.full_name


class BankAccount(models.Model):
   
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    password = models.CharField(max_length=100)  
    account_number = models.CharField(max_length=20)
    card_number = models.CharField(max_length=16)
    balance = models.DecimalField(max_digits=12)
    date_created = models.DateField(auto_now_add=True)
    expire_date = models.DateField()

    def __str__(self):
        return f"Account for {self.user.full_name} - {self.account_number}"
