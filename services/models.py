from django.db import models

# Create your models here.
class Service(models.Model):
    services_list = [
        ('air conditioning','air conditioning'),
        ('aliminume fitting','aliminume fitting'),
        ('Architecture Engineering','Architecture Engineering'),
        ('Blacksmith','Blacksmith'), ('carpenters','carpenters'), 
        ('Ceramics and tiling','Ceramics and tiling'),
        ('decorastions','decorastions'),
        ('Civil Engineering','Civil Engineering'),
        ('electrician','electrician'),
        ('glass','glass'), ('house painting','house painting'),
        ('movers','movers'), ('plumbers','plumbers'), 
        ('Roof insulation','Roof insulation'), 
        ('solar energy','solar energy'), 
        ('Central gas installations','Central gas installations')
    ]
    category = models.CharField(max_length=50,null=True,blank=True, choices=services_list)
    image = models.ImageField(upload_to='photos/%y/%m/%d')


    def __str__(self):
        return self.category

    class Meta:
        verbose_name = 'service'

    @staticmethod
    def get_all_servicess():
        return Service.objects.all()
    