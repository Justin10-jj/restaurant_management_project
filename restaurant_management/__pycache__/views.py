def contact_view(request):
    form=ContactForm(request.POST)
    if request.method=='POST' and form.is_valid():
        name=form.cleaned_data['name']
        email=form.cleaned_data['email']
        message=form.cleaned_data['message']
        full_message=f"Form:{name}<{email>}>\n\n{message}
        send_mail(
            subject="new content form message",
            message=full_message,
            form_email=settings.DEFAULT_FORM_EMAIL,
            recipient_list=['restaurant@gmaul.com'],
        )
        return redirect('contact_sucess')

    return render(request,'homepage.html',{'form':form})