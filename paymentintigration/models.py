from django.db import models

# Create your models here.
class PaytmConfig(models.Model):
    title = models.CharField(max_length=100,help_text='add mode for example "( testing config )" ')
    activate = models.BooleanField(help_text=":- check to activate",default=False)
    MID = models.CharField(max_length=100)
    MERCHANT_KEY = models.CharField(max_length=100)
    WEBSITE = models.CharField(max_length=100,choices=(('1','WEBSTAGING'),('2','DEFAULT')),help_text="choose Webstaging for testiing and Default for production")
    PostUrl = models.CharField(max_length=1000, blank=True)
    def __str__(self):
        return self.title
    stage = "https://securegw-stage.paytm.in/order/process"
    production = "https://securegw.paytm.in/order/process"
    def save(self, *args, **kwargs):
        if self.activate:
            data=PaytmConfig.objects.all().exclude(id=self.id)
            data.update(activate=False)
        self.PostUrl = self.production if self.WEBSITE == '2' else self.stage
        super(PaytmConfig, self).save(*args, **kwargs)