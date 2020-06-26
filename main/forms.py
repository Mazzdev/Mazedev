from django import forms


class ContactForm(forms.Form):
    from_email = forms.EmailField(max_length=100, widget=forms.EmailInput(attrs={'placeholder': 'Your e-mail','class' : 'email'}))
    subject = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Subject','class' : 'subject'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Your message','class' : 'message'}))
