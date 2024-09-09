from django.shortcuts import render
from django.core.mail import send_mail
from django.core.mail import send_mass_mail

def home(request):
    subject="test_mail from django server"
    message="this is a demo-test mail"
    from_email="utkarshlovespokemon@gmail.com"
    recipient_list=["utkarshlovespokemon@gmail.com"]
    send_mail(subject,message,from_email,recipient_list)