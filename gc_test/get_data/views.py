from django.shortcuts import render,redirect
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Data
from .serializers import DataSerializer
from .forms import childform
from .forms import chkform
from .main import zone_main
from .growth_checker2 import checker
from .growth_velocity import velocity
from .length import zone_height
import requests
import json
import sys
# class ip:
#     ip_dic={}
#     flag=0
#     def init():

class inp:
    dict={}
    def set(self,dic):
        self.dict=dic
    def get(self):
        return self.dict
i = inp()

def child_list(request):
    return render(request,"get_data/child_list.html")

def child_gr(request):
    return render(request,"get_data/child_gr.html")

def height(request):
    return render(request,"get_data/height.html")

def child_form(request):
    if request.method == 'GET':
        form = childform()
        print(form)
        return render(request,'get_data/child_form.html',{'form':form})
    elif request.method == 'POST':
        if request.POST.get('main'):
            form= childform(request.POST)
            if form.is_valid():
                serializer = DataSerializer(data=form.data)
                if serializer.is_valid():
                    serializer.save()
                    dic=zone_main(serializer.data)
                    op= " Zone : " + str(dic['zone']) + '<br>' +"\n Minimum Weight Gain to reach Safe (Light Green) Zone : " + str(dic['minimum_healthy_weight']) + '<br>' + "\n Average Weight of a Healthy Child in this age group  :"+ str(dic['average_weight_for_child'])
                    return render(request,'get_data/child_list.html',{'op': op,'ip' : serializer.data})
                return JsonResponse(serializer.errors, status=400)
        elif request.POST.get('velocity'):
            form= childform(request.POST)
            if form.is_valid():
                serializer = DataSerializer(data=form.data)
                if serializer.is_valid():
                    serializer.save()
                    op=velocity(serializer.data)
                    return render(request,'get_data/child_list.html',{'op': op,'ip' : serializer.data})
                return JsonResponse(serializer.errors, status=400)
        elif request.POST.get('growth_ch'):
            form = childform(request.POST)
            if form.is_valid():
                serializer = DataSerializer(data=form.data)
                if serializer.is_valid():
                    serializer.save()
                    n_form=chkform()
                    i.set(serializer.data)
                  #  print(i.get())
                    request.method= 'POST'
                    return render(request,'get_data/growth.html', {'form':n_form })
                   # growth_checker(request,serializer.data)
                return JsonResponse(serializer.errors, status=400)
        elif request.POST.get('btn_height'):
           # print('test')
           # print('test')
            form = childform(request.POST)
            #field = form['height'].value()
            #field1 = form['weight'].value()
           # print(field)
           # print(field1)
           # print(form)
            if form.is_valid():
                print('form valid')
                print(form)
                serializer = DataSerializer(data=form.data)
                if serializer.is_valid():
                    print(serializer)
                    serializer.save()
                    dic = zone_height(serializer.data)
                    print(dic)
                    print(serializer.data)
                    op = " Zone : " + str( dic['zone']) + '<br>' + "\n Minimum Height Gain to reach Safe (Light Green) Zone : " + str(dic['minimum_healthy_height']) + '<br>' + "\n Average Height of a Healthy Child in this age group  :" + str(dic['average_height_for_child'])
                    print(op)
                    return render(request,'get_data/height.html',{'op': op,'ip' : serializer.data})
                return JsonResponse(serializer.errors, status=400)



def growth_checker(request):
    if request.method == 'POST':
        form= chkform(request.POST)
        if form.is_valid():
            f=form.data
            op=checker(f, i.get())
            print(op)
            print(f.dict())
            print(i.get())
            return render(request,'get_data/child_gr.html',{'op': op,'ip' : i.get(),'id': f.dict()})
    elif request.method == 'GET':
        form = chkform()
        return render(request, 'get_data/growth.html', {'form': form})
    return HttpResponse(form.errors, status=400)








# @csrf_exempt
# def data_list(request):
#
#     if request.method == 'GET':
#         data = Data.objects.all()
#         form = childform()
#         serializer = DataSerializer(data, many=True)
#         print(serializer.data)
#         return render(request, 'get_data/child_form.html', {'form': form})
#         #x = requests.post("http://127.0.0.1:8000/data", data=serializer.data )
#         #print(x.text)
#       #  return JsonResponse(serializer.data, safe=False)
#
#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = DataSerializer(data =data)
#
#         if serializer.is_valid():
#             serializer.save()
#             print(serializer.data)
#
#             #x = requests.post("http://127.0.0.1:8000/data" , data= data)
#             #print(x.text)
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)
