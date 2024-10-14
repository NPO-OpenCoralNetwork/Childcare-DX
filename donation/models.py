from django.db import models



class Donation(models.Model):
    DONATION_TYPES = [
        ('general', 'General Donation'),
        ('member', 'Membership Donation'),
    ]
    
    PAYMENT_FREQUENCY = [
        ('monthly', 'Monthly'),
        ('yearly', 'Yearly'),
    ]

    donation_type = models.CharField(max_length=10, choices=DONATION_TYPES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_frequency = models.CharField(max_length=10, choices=PAYMENT_FREQUENCY, null=True, blank=True)
    is_anonymous = models.BooleanField(default=False)
    name = models.CharField(max_length=255, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    reason = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.get_donation_type_display()} - {self.amount} yen"

# Create your models here.
