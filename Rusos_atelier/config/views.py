from rest_framework import generics
from .models import AboutUs, Contacts
from .serializers import AboutUsSerializer, ContactsSerializer


class AboutUsAdd(generics.CreateAPIView):
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsSerializer

class AboutUsUpdate(generics.UpdateAPIView):
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsSerializer

class AboutUsDelete(generics.DestroyAPIView):
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsSerializer
    
#ContactViews

class ContactsAdd(generics.CreateAPIView):
    queryset = Contacts.objects.all()
    serializer_class = ContactsSerializer
    
class ContactsUpdate(generics.UpdateAPIView):
    queryset = Contacts.objects.all()
    serializer_class = ContactsSerializer

class ContactsDelete(generics.DestroyAPIView):
    queryset = Contacts.objects.all()
    serializer_class = ContactsSerializer