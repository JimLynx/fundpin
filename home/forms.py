from django import forms


class ContactForm(forms.Form):
    """
    Contact Form for contact page
    """
    name = forms.CharField(required=True)
    from_email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)
