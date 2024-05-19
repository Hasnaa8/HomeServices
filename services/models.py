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
    
    

# class Provider(models.Model):
#     provider_id = models.IntegerField(primary_key=True)
#     customer = models.OneToOneField(Customer, null=True, blank=True, on_delete=models.CASCADE)
#     service = models.ForeignKey(Service, on_delete=models.CASCADE)
#     desc = models.TextField()
#     worktimeForm = models.TimeField(blank=True)
#     worktimeTo = models.TimeField(blank=True)
#     costdomainForm = models.DecimalField(max_digits=6, decimal_places=2)
#     costdomainTo = models.DecimalField(max_digits=6, decimal_places=2)
#     rating = models.DecimalField(max_digits=2, decimal_places=1)
#     class Meta:
#         verbose_name = 'provider'

# rate_choices = [
#         (1,'2'),(1,'2'),(3,'3'),(4,'4'),(5,'5')
#     ]

# class Review(models.Model):
#     customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
#     provider = models.ForeignKey(Provider, on_delete=models.CASCADE)
#     date = models.DateTimeField(auto_now_add=True)
#     comment = models.TextField(max_length=3000, blank=True)
    
    
#     rate = models.PositiveSmallIntegerField(choices=rate_choices)
#     likes = models.PositiveIntegerField(default=0)
#     unlikes = models.PositiveIntegerField(default=0)
    

#     def __str__(self):
#         return self.Provider.Customer.user.username