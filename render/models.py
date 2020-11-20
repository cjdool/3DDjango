from django.db import models

class Service(models.Model):
    STATUS_CHOICES = (
        ('WAIT', 'Waiting in Queue'),
        ('EXEC', 'Executing'),
        ('FAIL', 'Fail'),
        ('SUCC', 'Success'),
        ('QUIT', 'Quited by Admin')
    )
    request_time = models.DateTimeField(name='date_requested')
    start_time = models.DateTimeField(name='date_started', null=True, blank=True)
    end_time = models.DateTimeField(name='date_ended', null=True, blank=True)
    status = models.CharField(max_length=4, choices=STATUS_CHOICES, name='data_status')
    emailaddress = models.EmailField(name='email_address')

