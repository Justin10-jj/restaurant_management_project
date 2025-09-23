from django.shortcuts import render
from.models import RestaurantLocation

def Homes(request):
    info=RestaurantLocation.objects.all()
    phone=info.phone_number if info else "phone number unavailabile"
    return render(request,'homepage.html',{'restaurant_phone':phone})

def homeee(request):
    crumbs=[]
    return render(request,'homepage.html',{
        'crumbs':crumbs,
        })

def menu(request):
    crumbs=[{'name':'menu','url':request.path},]
    return render(request,'menulist.html',{'crumbs':crumbs})



def desserts(request):
    crumbs=[
        {'name':'menu','url':'/menu/'},
        {'name':'Desserts'.'url'request.path}
    ]
    return render(request,'desserts.html',{'crumbs':crumbs})

def home(request):
    form=AuthenticationForm(request,data=request.POST or None)
    error=None
if request.method=="POST":
    if form.is_valid():
        user=form.get_User()
        login(request,user)
        return redirect('home')
    else:
        error "invalid username and password"

crumbs=[]
return render(request,home.html),{
    'form':form,'error':error,'crimbs':crumbs
}

def feedback_view(request):
    if request.method=='POST':
        form=FeedBackForms(request.POST)
        if form.is_valid():
            form.save()
            return Redirect('feedback_thank_you')
        else:
            form=FeedBackForms()
        return redirect(request,'feedback_form.html',{'form':for,})


def About(request):
    info=RestaurantLocation.object.first()
    return render(request,'about.html',{
        'restaurant_name':'restaurant',
        'info':info
    })



def SpecialListView(ListView):
    model=Special
    template_name='homepage.html'
    context_object_name='special'



def OpeniongHour(request):
    restaurant=RestaurantLocation.objects.first()
    context={

        'restaurant':restaurant,'opening_hours'restaurat.opening_hour if restaurant else None
    }
    return render(request,'homepage.html',context)



def contact_view(request):
    restaurant=RestaurantLocation.objects.first()
    if request.method=='POST':
        form=ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'conatact_thank_you.html')
        else:
            fprm=ContactForm()
        return render(request,'contact.html',{'form':form,'restaurant':restaurant})


def menu_view(request):
    menu_item=MenuList.objects.all()
    paginator=paginator(menu_item,5)
    page_number=request.GET.get('page')
    page_obj=paginator.get_page(page_number)
    return render(request,'menulist.html','page_obj':page_obj)


def HomeOpenongTime(request):
    opening_hours={
        "monday":"9:00 AM - 9:00 PM ",
        "Tuesday":"(:00 AM - 9:00 PM"
    }
    return render(request,"home.html",{"opening_hours":opening_hours})


class MenuItemByCatagoryView(generic.ListAPIView):
    serializer_class=MenuListSerializer

    def get_queryset(self):
        queryset=MenuList.objects.all()
        catagory_name=self.request.query_params.get("category")
        if category_name:
            queryset=queryset.filter(category_name_iexact=category_name)
        return queryset 



def signup_voew(request):
    email=request>POST.get("email")

    if not is_valid_email(email):
        return JsonResponse({"error"})

    return JsonResponse({"message":"Email is invalid"})



class MenuItemSet(viewsets.modelsViewSet):
    query=MenuList.objects.all()
    seializer_class=MenuListSerializer
    permission_classes=[permission.IsAdminUser]

    def update(self,request,*args,**kwargs):
        try:
            return super()>update(request,*args,**kwargs)
        except Exception as e:
            return Response({"error":str(e)})



class MenuPagination(pageNumberPagination):
    page_size=5
    page_size_query_parm="page_size"
    max_page_size=50

class MenuSearchViewSet(viewsets.ReadOnlyModelViewSet):
    queryset=MenuList.objects.all()
    serializer_class=MenuListSerializer
    pagination_class=MenuPagination
    filter_backends=[filter.SearchFilter]
    search_field=["name"]



def test_restaurant(request):
    r=RestaurantLocation.objects.create(address="123 main st",
    city="new york",state="ny",)
    return JsonResponse({
        "opening_hour":r.opening_hour,"monday":r.get_opening_hours("monday","friday":r.get_opening_hours("friday"))
    })




class UserProfileViewSet(viewsets.ViewSet):
    permission_classes=[permission.IsAuthenticated]

    def retrieve(self,request):
        serializer=UserProfileSerializer(request.user,data=requ\.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serilaizer.data)
        return Response(serilaizer.errors,status=400)