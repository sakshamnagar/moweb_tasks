from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView, DeleteView
from .models import *
from django.urls import reverse_lazy
from .forms import *
from django.db.models import Q
from django.core import serializers
from django.http import HttpResponse


#view to render index page
def index(request):
    furits = Fruits.objects.all().order_by('name')
    vegitables = Vegitables.objects.all().order_by('name')
    return render(request, 'index.html', context={'fruits':furits,'vegitables':vegitables})



class VendorView():

    #method to view all vendor objects
    def vendor_view(request):
        vendor = Vendor.objects.all()
        data = serializers.serialize('json', vendor)
        return HttpResponse(data,content_type='application/json')
    
    #method to create vendors
    def vendor_create(request):
        if request.method == "POST":
            first_name = request.POST.get('fname')
            last_name = request.POST.get('lname')
            email = request.POST.get('email')
            image = request.POST.get('image')
            vendor = Vendor(first_name=first_name,last_name=last_name,email=email,image=image)
            vendor.save()
            return HttpResponse('Success')
        else:
            return HttpResponse('Error')

    #method to view all fruits by a particular vendor    
    def vendor_detail(request,pk):
        fruits = Fruits.objects.filter(vendor_fruits__id=pk)
        data = serializers.serialize('json',fruits)
        return HttpResponse(data,content_type='application/jason')


class FruitsView():
    #method to create fruits
    def create_fruits(request):
        if request.method == 'POST':
            vendor = request.POST.get('vendor')
            name = request.POST.get('name')
            quantity = request.POST.get('quantity')
            fruits = Fruits(vendor_fruits_id=vendor,name=name,quantity=quantity)
            fruits.save()
            return HttpResponse('success')
        else:
            return HttpResponse('Error')

    #method to view,sort and search all fruits    
    def view_fruits(request):
        fruits = Fruits.objects.all()
        #search & sort feature
        if request.method == 'GET':
            sorted = request.GET.get('sort')
            query = request.GET.get('query','')
            if sorted:
                fruits = Fruits.objects.all().order_by(sorted)
            if query:
                fruits = Fruits.objects.filter(Q(name__icontains=query))
        data = serializers.serialize('json', fruits)
        return HttpResponse(data, content_type='application/json')
    
    #method to update a fruit
    def update_fruits(request, pk):
        if request.method == "POST":
            name = request.POST.get('name','')
            quantity = (request.POST.get('quantity',''))
            Fruits.objects.filter(pk=pk).update(name=name,quantity=quantity)
            return HttpResponse('Success')
        else:
            return HttpResponse('Error')
        
    #method to soft delete a fruit
    def delete_fruits(request,pk):
        fruits = Fruits.objects.get(pk=pk)
        fruits.soft_del()
        return HttpResponse('success')
        
    #method to view soft-deleted fruits
    def bin_fruits(request):
        fruits = Fruits.allobj.filter(is_deleted=True)
        data = serializers.serialize('json', fruits )
        return HttpResponse(data, content_type='application/json')

    #method to restore soft-deleted fruit
    def restore_fruits(request,pk):
        fruits= Fruits.allobj.get(id=pk)
        fruits.restore()
        return HttpResponse('success')
    

    

class VegitablesView():
    #method to create vegitables 
    def create_vegitables(request):
        if request.method == 'POST':
            vendor = request.POST.get('vendor')
            name = request.POST.get('name')
            quantity = request.POST.get('quantity')
            vegitables = Vegitables(vendor_vegitables_id=vendor,name=name,quantity=quantity)
            vegitables.save()
            return HttpResponse('success')
        else:
            return HttpResponse('Error')

    #method to view,sort and search vegitables    
    def view_vegitables(request):
        vegitables = Vegitables.objects.all()
        #search & sort feature
        if request.method == 'GET':
            sorted = request.GET.get('sort')
            query = request.GET.get('query','')
            if sorted:
                vegitables = Vegitables.objects.all().order_by(sorted)
            if query:
                vegitables = Vegitables.objects.filter(Q(name__icontains=query))
        data = serializers.serialize('json', vegitables)
        return HttpResponse(data, content_type='application/json')
    

    #method to update vegitables
    def update_vegitables(request, pk):
        if request.method == "POST":
            name = request.POST.get('name','')
            quantity = (request.POST.get('quantity',''))
            Vegitables.objects.filter(pk=pk).update(name=name,quantity=quantity)
            return HttpResponse('Success')
        else:
            return HttpResponse('Error')
        
    #method to soft delete vegitables
    def delete_vegitables(request,pk):
        vegitables = Vegitables.objects.get(pk=pk)
        vegitables.soft_del()
        return HttpResponse('success')
        
    #method to view soft deleted vegitables
    def bin_vegitables(request):
        vegitables = Vegitables.allobj.filter(is_deleted=True)
        data = serializers.serialize('json', vegitables )
        return HttpResponse(data, content_type='application/json')

    #method to restore soft deleted vegitables
    def restore_vegitables(request,pk):
        vegitables= Vegitables.allobj.get(id=pk)
        vegitables.restore()
        return HttpResponse('success')

    
#method to add store
def store_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        vendor = request.POST.get('vendor')
        store=Store(name=name)
        store.save()
        store.vendors.add(vendor)
        return HttpResponse('Success')
    else:
        return HttpResponse('Error')

    
#method to view details of a particular store
def store_detail(request,pk):
    store = Store.objects.filter(pk=pk)
    """for i in store.all():
        for j in i.vendors.all():
            print('---------------------VENDORS------------------',j.email)"""
    data = serializers.serialize('json',store)
    return HttpResponse(data, content_type ='application/json')

#method to list all stores
def store(request):
    store = Store.objects.all()
    data = serializers.serialize('json',store)
    return HttpResponse(data, content_type ='application/json')
    
    

