from django.db import models

class Groom(models.Model):
    # ... fields as defined previously
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    date_of_birth = models.DateField()
    height = models.DecimalField(max_digits=4, decimal_places=2, help_text="Height in feet")
    marital_status = models.CharField(max_length=20, choices=[
        ('single', 'Single'),
        ('divorced', 'Divorced'),
        ('widowed', 'Widowed'),
    ])
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    address = models.TextField()
    education = models.CharField(max_length=100)
    occupation = models.CharField(max_length=100)
    income = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    father_name = models.CharField(max_length=100)
    mother_name = models.CharField(max_length=100)
    family_background = models.TextField()
    religion = models.CharField(max_length=50)
    caste = models.CharField(max_length=50)
    diet = models.CharField(max_length=50)
    smoking_habit = models.CharField(max_length=50)
    drinking_habit = models.CharField(max_length=50)
    hobbies = models.TextField(blank=True, null=True)
    about_me = models.TextField(blank=True, null=True)
    photo = models.ImageField(upload_to='groom_photos/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

