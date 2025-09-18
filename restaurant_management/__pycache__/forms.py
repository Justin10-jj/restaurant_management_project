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


class FeedbackForms(forms.ModelForm):
    class Meta:
        model=Feedbackss
        field=['name','message']
        widget={'name':forms.TextInput(attrs={'placeholder':'your Name'})}
        'message':form.Textarea(attrs={'placeholder':'your Feedback','row',:4})


class SignUpForm(forms.Form):
    email=forms.EmailField()
    def clean_email(self):
        email=slef.cleaned_data["email"]
        if not is_valid_email(email):
            raise form.ValidationError("invalid")
        return email