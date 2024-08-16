from django.shortcuts import render,redirect
from django.views import View 
from django.http import HttpResponse
from django.views.generic import CreateView,TemplateView,ListView,DeleteView,UpdateView
from ContactApp.forms import RegisterForm,UserLoginForm,ContactForm
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from ContactApp.models import ContactModel


# Create your views here.
class HomeView(TemplateView):
    template_name="index.html"

class RegisterView(CreateView):
    template_name="register.html"
    form_class=RegisterForm
    model=User
    success_url=reverse_lazy("home_view")

    def form_valid(self,form):
        fname=form.cleaned_data.get("first_name")
        lname=form.cleaned_data.get("last_name")
        uname=form.cleaned_data.get("username")
        email=form.cleaned_data.get("email")
        passw=form.cleaned_data.get("password")
        User.objects.create_user(first_name=fname,last_name=lname,username=uname,email=email,password=passw)
        messages.success(self.request,'registration successfull')
        return redirect("home_view")

class UserLoginView(View):
    def get(self,request):
        form=UserLoginForm()
        return render(request,'login.html',{'form':form})
    def post(self,request):
        uname=request.POST.get("username")
        passw=request.POST.get("password")
        user=authenticate(request,username=uname,password=passw)
        if user:
            login(request,user) 
            messages.success(request,"Welcome")
            return redirect("home_view")
        else:
            messages.error(request,"invalid credentials")
            return redirect("login_view")

class UserLogoutView(View):
    def get(self,request):
        logout(request)
        return redirect("login_view")

class AddContactView(CreateView):
    template_name='add_contact.html'
    form_class=ContactForm
    model=ContactModel
    success_url=reverse_lazy("home_view")
    def post(self,request):
        if request.user.is_authenticated:
            form=ContactForm(request.POST)
            if form.is_valid():
                name=form.cleaned_data.get('name')
                phone=form.cleaned_data.get('phone')
                user=request.user
                ContactModel.objects.create(name=name,phone=phone,user=user)
                messages.success(request,"Contact Added")
                return redirect('home_view')
        else:
            messages.error(request,"You Should Login First")
            return redirect('login_view')

class ContactListView(ListView):
    template_name='list.html'
    model=ContactModel
    context_object_name='con'
    def get_queryset(self):
        return ContactModel.objects.filter(user=self.request.user)

    

class ContactDeleteView(DeleteView):
    model=ContactModel
    success_url=reverse_lazy('home_view')
    template_name='login.html'
    pk_url_kwarg='id'

class ContactUpdateView(UpdateView):
    model=ContactModel
    form_class=ContactForm
    template_name='update.html'
    pk_url_kwarg='id'
    success_url=reverse_lazy('list_view')
    def form_valid(self,form):
        messages.success(self.request,"Updated")
        return super().form_valid(form)