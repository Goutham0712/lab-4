
from django.shortcuts import render
from .models import Contacts
from django.http import HttpResponseRedirect


from django.shortcuts import render

def home(request):
    contact_list = Contacts.objects.order_by('first_name')

    return render(request, 'index.html')



def help_page(request):
    
    return render(request, 'help.html')


def contacts(request):
    # Fetch all contacts from the database
    contact_list = Contacts.objects.order_by('first_name')
    

    if request.method == 'POST':
        # Retrieve form data
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')

        # Create a new Contact instance and save it to the database
        new_contact = Contacts(first_name=first_name, last_name=last_name, email=email)
        new_contact.save()
        
        # Redirect to the contacts page to display the updated list
    
    # Render contacts.html template with contact_list
    return render(request, 'contacts.html', {'contacts': contact_list})
