from django.db import models
from django.contrib.auth.models import User


class TicketModel(models.Model):
    status_list = (
        ('Active', 'Active'),
        ('Used', 'Used')
    )
    ticket_id = models.OneToOneField(
        User, on_delete=models.CASCADE)
    duration = models.CharField(max_length=4)
    status = models.CharField(choices=status_list, max_length=7)
