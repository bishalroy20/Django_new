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
        # print(form.cleaned_data)
        user = form.save()
        
        login(self.request, user)
        messages.success(self.request, "Account created successfully!")
        return super().form_valid(form) # form_valid function call hobe jodi sob thik thake
    
    def form_invalid(self, form):
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(self.request, f"{field}: {error}")  # Display field-specific errors
        return super().form_invalid(form)
   
    
class UserLoginView(LoginView):
    template_name = 'account/user_login.html'
    def form_valid(self, form):
        messages.info(self.request, "Log in Successfully")  
        return super().form_valid(form)
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
    

