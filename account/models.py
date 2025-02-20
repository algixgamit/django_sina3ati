# from django.db import models
# from django.contrib.auth.models import AbstractUser,BaseUserManager
# from django.db.models.deletion import CASCADE
# from django.conf import  settings
# from django.contrib.auth import get_user_model


# class User(AbstractUser):
#     username = models.CharField(null=False, blank=False,max_length=50, unique=True)   
#     email_enreg = models.EmailField(verbose_name="email_enreg", max_length=60, unique=False)
#     account_type  = models.CharField(verbose_name="account_type",null=True, blank=True,max_length=7,default='admin') #teacher admin  student
#     date_of_birth =  models.DateField(null=True, blank=True,max_length=8)    
#     USERNAME_FIELD = 'username'
 
#     def __str__(self):
#         return self.username

# class Admin_Sirap(models.Model):#settings.AUTH_USER_MODEL
#     user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
#     Admin_Sirap_name = models.CharField(null=True, blank=True,max_length=200)
#     level =models.FloatField(null=True, blank=True,default=0) 
#     Admin_Sirap_Position = models.CharField(null=True, blank=True,max_length=200)

#     # Student_niveau = models.CharField(null=True, blank=True,max_length=200)
#     # Student_topic = models.CharField(null=True, blank=True,default=0,max_length=200)
    
#     def __str__(self):
#         return self.user.username  

# class Admin_Custmer(models.Model):#settings.AUTH_USER_MODEL
#     user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
#     Admin_Custmer_name = models.CharField(null=True, blank=True,max_length=200)
#     Admin_Custmer_Oraganisation =  models.CharField(null=True, blank=True,max_length=200)
#     Admin_Custm_Position = models.CharField(null=True, blank=True,max_length=200)

    
#     def __str__(self):
#         return self.user.username   

# class Manager_Customer(models.Model):#settings.AUTH_USER_MODEL
#     user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
#     Manager_Customer_name = models.CharField(null=False, blank=False,max_length=200)
#     Manager_Custmer_Oraganisation =  models.CharField(null=True, blank=True,max_length=200)
#     Manager_Customer_Position = models.CharField(null=True, blank=True,max_length=200)
#     def __str__(self):
#         return self.user   

# class Technical_Customer(models.Model):#settings.AUTH_USER_MODEL
#     user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
#     Technical_Customer_name = models.CharField(null=False, blank=False,max_length=200)
#     Technical_Custmer_Oraganisation =  models.CharField(null=True, blank=True,max_length=200)
#     Technical_Customer_Position = models.CharField(null=True, blank=True,max_length=200)
#     def __str__(self):
#         return self.user    

# class Triale_Customer(models.Model):#settings.AUTH_USER_MODEL
#     user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
#     Trial_Customer_name = models.CharField(null=False, blank=False,max_length=200)
#     Trial_Customer_Organisation = models.CharField(null=False, blank=False,max_length=200)
#     Trial_Customer_Position = models.CharField(null=True, blank=True,max_length=200)
#     Trial_Customer_login_date = models.CharField(null=True, blank=True,max_length=200)
#     def __str__(self):
#         return self.user    






# """ class timeup(models.Model):
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     room = models.ForeignKey(Room, on_delete=models.CASCADE)
#     time_of_activated = models.TimeField()
#     date_of_activated = models.DateField()
#     name=
#     class Meta:
#         ordering = ['-updated', '-created']

#     def __str__(self):
#         return self.name """