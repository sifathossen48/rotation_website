from django.forms import ModelForm
from Contact_Page.models import Contact

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ('name', 'email', 'subject', 'message', )
