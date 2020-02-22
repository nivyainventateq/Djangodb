from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.base import View
from complaint.models import Contacttb



class Test(View):

    def get(self,request,*args,**kwargs):
        list=Contacttb.objects.filter(fname='tejas')
        data={'name':list}
        return render(request,'index.html',data)

    def post(self,request,*args,**kwargs):
        print(request.POST)
        so=Contacttb()
        so.fname=request.POST.get('firstname')
        so.lname=request.POST.get('lastname')
        so.place=request.POST.get('country')
        so.sub=request.POST.get('subject')
        so.save()
        return HttpResponse('<h1> Thank You </h1>')

test=Test.as_view()



    # list = contactinfo.objects.filter(fname='ghgfg')
    #
    # data = {'name': list}
    # return render(request, "hello.html", data)







