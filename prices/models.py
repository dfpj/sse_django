from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django_eventstream import send_event


class Currency(models.Model):
    title = models.CharField(max_length=255)
    code = models.CharField(max_length=8)

    def __str__(self):
        return self.title


class PriceAction(models.Model):
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
    price = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.currency} - {self.price}"


@receiver(post_save,sender=PriceAction)
def price_actions_events(sender,instance,created,**kwargs):
    if created:
        created = str(instance.created)
        price = str(instance.price)
        send_event('prices','actions',{'created':created,'price':price})