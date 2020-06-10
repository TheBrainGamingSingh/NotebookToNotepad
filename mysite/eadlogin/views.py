from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
from django.db import IntegrityError
from django.contrib.auth.models import User, auth
from django.core.files.storage import FileSystemStorage
from .apps import EadloginConfig
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import sys
from subprocess import run, PIPE

# Create your views here.

def homepage (request):
    if request.method == 'POST' :
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)

        if user is None:
            messages.info(request, 'Sorry, wrong username or password. Please try again.')
            return redirect('/')
        else:
            #correct username and password. Redirect to drag and drop page.
            #auth.login(request, user)
            return redirect('upload')
    else:
        return render(request, 'homepage.html')

#from django.shortcuts import render  # Create your views here. 
def upload(request):     
    if request.method == 'POST' and request.FILES['myfile']:         
        myfile= request.FILES['myfile']         
        fs = FileSystemStorage(location="media")         
        filename = fs.save(myfile.name, myfile)         
        uploaded_file_url = fs.url(filename)         
        return render(request, 'upload.html', {'uploaded_file_url': uploaded_file_url,"fileupload":"File uploaded successfully"})     
    return render(request,'upload.html')

def output(request):
    inp = request.POST.get('myfile')
    out = run([sys.executable, 'C:\\Users\\ISHIKA\\Desktop\\EAD Project\\NTN\\src\\main.py'], inp, shell=False, stdout=PIPE)
    print(out)
    return render(request,'output.html', {'data':out.stdout})

class call_model(APIView):
    def get(self,request):
        if request.method == 'GET':
            
            # predict method used to get the prediction
            response = EadloginConfig.Model.infer(sentence)
            
            # returning JSON response
            return JsonResponse(response)