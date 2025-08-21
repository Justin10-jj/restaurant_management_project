from django import forms
form.models import Feedbacks,ContactSubmission

class FeedbackForm(form.ModelForm):
    class Meta:
        model=Feedback
        field=['comment']
        widget={
            'comment':forms.Textarea(attrs={
                'row':5,
                'placeholder':'Leave your feedback here..'
            }),
        }


class ContactForm(forms.ModelForm):
    class Meta:
        model=ContactSubmission
        field=['name','email']