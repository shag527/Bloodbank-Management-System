from django.shortcuts import render
from .models import Donors,BRequests,Contact_Us
from django.contrib.auth import login,authenticate,update_session_auth_hash
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from .forms import EditProfileForm

# Create your views here.
def the_group(user_blood):
    if user_blood=="O Positive":
        the_group=["O Positive","A Positive","B Positive","AB Positive"]

    elif user_blood=="A Positive":
        the_group=["A Positive","AB Positive"]

    elif user_blood=="B Positive":
        the_group=["B Positive","AB Positive"]

    elif user_blood=="AB Positive":
        the_group=["AB Positive"]

    elif user_blood=="O Negative":
        the_group=["O Positive","A Positive","B Positive","AB Positive","O Negative","A Negative","AB Negative","B Negative"]

    elif user_blood=="A Negative":
        the_group=["A Positive","AB Positive","A Negative","AB Negative"]

    elif user_blood=="B Negative":
        the_group=["B Positive","AB Positive","B Negative","AB Negative"]

    elif user_blood=="AB Negative":
        the_group=["AB Positive","AB Negative"]

    return the_group
        

def home(request):
	return render(request,'home.html',{})


def adminlogin(request):
	return render(request,'admin.html',{})	

def aboutus(request):
	return render(request,'aboutus.html',{})	

def eligibility(request):
	return render(request,'eligibility.html',{})	

def signin(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect("donor")
    else:
        form = UserCreationForm()
    return render(request, 'signin.html', {'form': form})

def tandc(request):
	return render(request,'terms.html',{})	

def admin_in(request):
	return render(request,'admin.html',{})		

def donor(request):
        if request.method == 'POST':
            post=Donors()
            post.name= request.POST.get('person_name')
            post.age= request.POST.get('age')
            post.contact_number= request.POST.get('contact_number')
            post.address= request.POST.get('address')
            post.gender= request.POST.get('sex')
            post.blood_group= request.POST.get('blood_group')
            post.email=request.POST.get('email')
            post.district=request.POST.get('district')
            post.pincode=request.POST.get('pincode')
            post.last_donated_date=request.POST.get('last_donated_date')
            post.major_illness=request.POST.get('major_illness')
            post.the_link=request.user.id
            post.b_request_id=None
            post.save()

                
            num=request.user.id
            userr = get_object_or_404(Donors, the_link=num)
            bg_group=the_group(userr.blood_group)
            args={'user':userr,'requests':BRequests.objects.filter(status=1),'donate_group':bg_group}
            return render(request,'profile.html',args)   

        else:
                return render(request,'donor.html',{'user':request.user.username})    		

def profile(request):
    num=request.user.id
    userr = get_object_or_404(Donors, the_link=num)
    bg_group=the_group(userr.blood_group)
    args={'user':userr,'requests':BRequests.objects.filter(status=1),'donate_group':bg_group}
    return render(request,'profile.html',args)			

def detail(request,pk):
    detail=BRequests.objects.get(id=pk)
    return render(request,'detail.html',{'x':detail})

def favourite(request):
    c_userr=request.user.id
    c_user=Donors.objects.get(the_link=c_userr)
    try:
        selected_request=BRequests.objects.get(id=request.POST.get("donate"))
        if c_user.b_request_id !=None:
            prev_selected_request=c_user.b_request_id
    except:
        error=request.POST.get("donate")
        num=request.user.id
        userr = get_object_or_404(Donors, the_link=num)
        args={'user':userr,'requests':BRequests.objects.all()}
        return HttpResponse("request does not exist")
    else:
        temp=c_user.b_request_id
        c_user.b_request_id=selected_request
        c_user.save()
        d_donors=selected_request.donors_set.all()
        str1=""
        for giver in d_donors:
            str1+=giver.name+" "+giver.contact_number+"\n"
        selected_request.the_donors=str1
        selected_request.save()

        if temp != None:
            prev_selected_request=temp
            d_donors=prev_selected_request.donors_set.all()
            str1=""
            for giver in d_donors:
                str1+=giver.name+" "+giver.contact_number+"\n"
            prev_selected_request.the_donors=str1
            prev_selected_request.save()

        num=request.user.id
        userr = get_object_or_404(Donors, the_link=num)
        bg_group=the_group(userr.blood_group)
        args={'user':userr,'requests':BRequests.objects.filter(status=1),'donate_group':bg_group}
        return render(request,'profile.html',args)
def requests(request):
        if request.method == 'POST':
            post=BRequests()
            post.patient_name= request.POST.get('patientname')
            post.attendant_name= request.POST.get('attendantname')
            post.contact_number= request.POST.get('contactnumber')
            post.blood_group= request.POST.get('bloodgroup')
            post.quantity= request.POST.get('quantity')
            post.hospital_name= request.POST.get('hospital')
            post.deadline=request.POST.get('date')
            post.status=0

            post.save()
                
            return render(request, 'seek.html')  

        else:
                return render(request,'seek.html')
def update(request):
    if request.method == 'POST':
            post=Donors.objects.get(the_link=request.user.id)
            post.name= request.POST.get('person_name')
            post.age= request.POST.get('age')
            post.contact_number= request.POST.get('contact_number')
            post.address= request.POST.get('address')
            post.gender= request.POST.get('sex')
            post.blood_group= request.POST.get('blood_group')
            post.email=request.POST.get('email')
            post.district=request.POST.get('district')
            post.pincode=request.POST.get('pincode')
            post.last_donated_date=request.POST.get('last_donated_date')
            post.major_illness=request.POST.get('major_illness')
            post.password=request.POST.get('psw')
            post.save()

            num=request.user.id
            userr = get_object_or_404(Donors, the_link=num)
            bg_group=the_group(userr.blood_group)
            args={'user':userr,'requests':BRequests.objects.filter(status=1),'donate_group':bg_group}
            return render(request,'profile.html',args)
                 

    else:
            num=request.user.id
            userr = get_object_or_404(Donors, the_link=num)
            bg_group=the_group(userr.blood_group)
            args={'user':userr,'requests':BRequests.objects.filter(status=1),'donate_group':bg_group}
            return render(request,'profile.html',args)

def delete(request):
    postt=request.user.id
    post=Donors.objects.get(the_link=postt)

    temp=post.b_request_id
    post.b_request_id=None
    post.save()
    rrequest=temp
    d_donors=rrequest.donors_set.all()
    str1=" "
    for giver in d_donors:
        str1+=giver.name+" "+giver.contact_number+"\n"
    rrequest.the_donors=str1
    rrequest.save()

    num=request.user.id
    userr = get_object_or_404(Donors, the_link=num)
    bg_group=the_group(userr.blood_group)
    args={'user':userr,'requests':BRequests.objects.filter(status=1),'donate_group':bg_group}
    return render(request,'profile.html',args)
    
def profile_edit(request):
    if request.method=="POST":
        form=EditProfileForm(request.POST,instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form=EditProfileForm(instance=request.user)
        args={'form':form}
        return render(request,'edit_profile.html',args)   

def change_password(request):
    if request.method=="POST":
        form=PasswordChangeForm(data=request.POST,user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request,form.user)
            return redirect('profile')
        else:
            return redirect('change_password')
    else:
        form=PasswordChangeForm(user=request.user)
        args={'form':form}
        return render(request,'change_password.html',args) 

def contact_us(request):
        if request.method == 'POST':
            post=Contact_Us()
            post.firstname= request.POST.get('firstname')
            post.lastname= request.POST.get('lastname')
            post.state= request.POST.get('state')
            post.subject= request.POST.get('subject')
            post.save()
            return redirect('contact')   

        else:
            return render(request,'contact.html')         





