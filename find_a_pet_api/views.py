from django.shortcuts import render
from django.contrib.auth import authenticate, login 
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from django.views.decorators.csrf import csrf_exempt
import json
from .models import CustomUser
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.forms.utils import ErrorDict

def index(request):
    return render(request, 'index.html')

def extract_error_messages(errors):
    error_messages = {}
    for field, field_errors in errors.items():
        error_messages[field] = [str(error) for error in field_errors]
    return error_messages

def extract_login_error_messages(errors):
    if isinstance(errors, ErrorDict):
        return {field: [error for error in errors[field]] for field in errors}
    return errors

@csrf_exempt 
@api_view(['POST'])
def user_signup(request):
    if request.method == 'POST':
        CustomUser.objects.all()
        data = json.loads(request.body)['formData']
        username = data['email']
        data['username'] = username
        data['first_name'] = data['firstName']
        data['last_name'] = data['lastName']
        form = CustomUserCreationForm(data)
        if form.is_valid():
            form.save()
            return Response({'Success': True}, content_type='application/json')
        else:
          errors = extract_error_messages(form.errors)
          print(errors, 'errors11')
          return Response({'Error': errors})
    else:
        return Response({'Error':  'Bad request'}, content_type='application/json')

@csrf_exempt 
@api_view(['POST'])
def user_login(request):
    if request.method == 'POST':
        data = json.loads(request.body)['formData']
        data['username'] = data['email']
        form = CustomAuthenticationForm(data=data)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)    
                return Response({'Success': True})
        else:
          errors = extract_login_error_messages(form.errors)
          return Response({'Error': errors})
    else:
        return Response({'Error':  'Bad request'}, content_type='application/json')
