from django.shortcuts import render , redirect
from django.contrib.auth import login , logout
from django.views.generic import FormView , View 
from django.urls import reverse_lazy
from .forms import UserRegistrationForm , UserUpdateForm
from django.contrib.auth.views import LoginView , LogoutView
from django.contrib import messages

class UserRegistrationView(FormView):
    template_name = 'account/user_registration.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('profile')
    
    def form_valid(self,form):
        print(form.cleaned_data)
        user = form.save()
        login(self.request, user)
        # print(user)
        return super().form_valid(form) # form_valid function call hobe jodi sob thik thake

   
    
class UserLoginView(LoginView):
    template_name = 'account/user_login.html'
    def get_success_url(self):
        return reverse_lazy('profile')

    
    
def user_logout(request):
    messages.info(request , "Logged Out Successfully")
    logout(request)
    return redirect('home')

class UserAccountUpdateView(View):
    template_name = 'account/profile.html'

    def get(self, request):
        form = UserUpdateForm(instance=request.user)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
        return render(request, self.template_name, {'form': form})
    

