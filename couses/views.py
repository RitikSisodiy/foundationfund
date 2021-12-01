from django.http import request
from django.shortcuts import render
from . models import *
from paytm import Checksum
from django.views.decorators.csrf import csrf_exempt
from paymentintigration.views import getPaytmParam,verifyPaymentRequest,PaypalParam
# Create your views here.
def couses(request,slug=None):
    res= {}
    if slug is not None:
        #for single couse
        res['couse'] = Couses.objects.get(slug = slug)
        return render(request,'couses/single-couse.html',res)
    # for couse list
    res['couseslist'] = Couses.objects.all().order_by('-time')
    return render(request,'couses/couses.html',res)

def paymenthandler(request,slug=None):
    if request.method=="POST":
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        currency=request.POST['currency_code']
        # ammount=float(request.POST['selamount'])
        ammount = request.POST['amount']
        couseob = Couses.objects.get(slug=slug)
        Donation = donation.objects.create(first_name = fname, last_name = lname,  email= email , ammount = ammount,  couse = couseob , currency=currency,transactionid = 'NO transaction')
        Donation.save()
        param_dict,renderhtml =  getPaytmParam(request,Donation.order_id,ammount,email,'handle',currency)
        print(param_dict)
        return renderhtml
    # items = charityblog.objects.get(id = num)
    # pers = str((float(items.blog_raised)*100)/float(items.blog_goal))[:4]
    # return render(request , 'donation/payment.html',{'blog':items,'per':pers})
@csrf_exempt
def hendlerequest(request):
    if request.method =='POST':
        # form = request.POST
        # response_dict= {}
        # for i in form.keys():
        #     response_dict[i]=form[i]
        #     if i == 'CHECKSUMHASH':
        #         checksum = form[i]
        # print(response_dict)
        # MERCHANT_KEY = 'a1Q7vq@5Q#PvFVc@'
        # verify = Checksum.verify_checksum(response_dict,MERCHANT_KEY,checksum)
        verify,response_dict = verifyPaymentRequest(request)
        if verify:
            if response_dict['RESPCODE'] == '01':
                donationblog = donation.objects.get(order_id = response_dict['ORDERID'])
                if donationblog.transactionid == 'NO transaction':
                    Blog = Couses.objects.get(id = donationblog.couse.id)
                    Blog.raised = float(Blog.raised) + float(response_dict['TXNAMOUNT'])
                    Blog.save()
                response_dict['couse'] = float(response_dict['TXNAMOUNT'])
                donationblog.transactionid = response_dict['TXNID']
                donationblog.save()
            else:
                try:
                    Donation=donation.objects.get(order_id=int(response_dict['ORDERID']))
                    Donation.delete()
                except Exception as e:
                    pass
        else:
            print("order unsuccessful because",response_dict['RESPMSG'])
        return render(request,'couses/paymentstatus.html',{'response': response_dict})
def paypalHandler(request,slug):
     if request.method=="POST":
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        currency=request.POST['currency_code']
        # ammount=float(request.POST['selamount'])
        ammount = request.POST['amount']
        couseob = Couses.objects.get(slug=slug)
        Donation = donation.objects.create(first_name = fname, last_name = lname,  email= email , ammount = ammount,  couse = couseob , currency=currency,transactionid = 'NO transaction')
        Donation.save()
        paypal_dict ,form  = PaypalParam(request,Donation.order_id,Donation.email,Donation.ammount)
        return render(request, 'couses/process_payment.html', {'order': Donation, 'form': form})
@csrf_exempt
def payment_done(request):
    return render(request, 'couses/payment_done.html')


@csrf_exempt
def payment_canceled(request):
    return render(request, 'couses/payment_cancelled.html')
