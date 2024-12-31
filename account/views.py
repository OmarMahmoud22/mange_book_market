from django.contrib import messages
from .form import UserResitrationForm , UserEditForm , ProfielEditForm
from django.shortcuts import render
from .models import Profile
#from .form import LoginForm
#from django.contrib.auth import authenticate , login
#from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

#def index(request):
 #   if request.method =='POST':
  #      #if request is post
   #     form = LoginForm(request.POST)
    #    #put the data sent on form
     #   if form.is_valid():
      #      #if this data valid as form feuld settings
       #     cd = form.cleaned_data
        #    # get all field on form
         #   user = authenticate(request , username=cd['username'] , password=cd['password'])
          #  # get auth func to macksure the username on db exactlly the username in field useing cd value
            
          #  if user is not None:
           #     # if value have is none mean not in db

            #    if user.is_active:
                    # if active => active it bool on db 
              #      login(request , user)
             #       # login with request and user and return sussecfull
               #     return HttpResponse('sussesfull')
               # else : 
                #    return HttpResponse('disable account.')    
            #else : 
             #       return HttpResponse('disable account.')    

  #  else :

   #     form = LoginForm()        

        # if data get return form fadyy
    #return render(request , 'account/index.html' , {'form': form})





def regester(request):
    if request.method == 'POST':
        #if type of reqest is post
        user_form = UserResitrationForm(request.POST)
        #put it on form
        if user_form.is_valid():
            # if valid
            new_user = user_form.save(commit=False)
            #dont save 
            new_user.name = new_user.set_password(user_form.cleaned_data['password'])
            # mack sure the password was haching
            new_user.save()
            Profile.objects.create(user=new_user)
            #save
            return render(request , 'account/regester_done.html' , {'new_user' : new_user})
            # reteurn done
        
        
    else:
        user_form = UserResitrationForm()    
        #if reqest is get return form page
    return render(request , 'registration/regster_form.html' , {'user_form':user_form})
            

@login_required
def edit(request):
    if request.method == 'POST' :
        user_form = UserEditForm(instance=request.user , data=request.POST)
        prof_form = ProfielEditForm(instance=request.user , data=request.POST ,files = request.FILES)
        if user_form.is_valid() and prof_form.is_valid():
            user_form.save()
            prof_form.save()
            messages.success(request , 'profile has been updated successfully.')
        else:
            messages.error(request , 'error in updating')    
    else:
        user_form = UserEditForm(instance=request.user )
        prof_form = ProfielEditForm(instance=request.user )
    return render(request , 'account/edit.html' , {'user_form' : user_form  , 'prof_form' : prof_form})    



