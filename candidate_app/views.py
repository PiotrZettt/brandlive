from django.shortcuts import render, redirect, reverse
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin
from .forms import CandidateForm
from django.views.generic.edit import DeleteView, UpdateView
from .models import CandidateProfile
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


def index(request):
    id = request.user.id

    return redirect('profile-detail', pk=[str(id)])

def query(request):

    if request.user.is_staff:

        result_all = CandidateProfile.objects.all()

        registered_locations = []
        for profile in result_all:
            registered_locations.append(profile.location)
        location_options = set(registered_locations)

        if request.method == 'POST':
            gender = request.POST.get('gender', False)
            age = request.POST.get('age', False)
            location = request.POST.get('location', False)

            searched_result = CandidateProfile.objects.filter(gender=gender).filter(age=age).filter(location=location)

            context = {
                'result_all': result_all,
                'searched_result': searched_result
            }
            return render(request, 'search-result.html', context)
        return render(request, 'search.html', {'results': result_all, 'location_options': location_options})
    else:
        return HttpResponse("<h3> You have no permission to access this site </h3>")


def create_profile(request):
    if request.method == "POST":
        form = CandidateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('user-login')
    else:
        form = CandidateForm()
    context = {
        'form': form,
    }
    return render(request, 'create_profile.html', context)


class CandidateUpdateView(UpdateView):
    model = CandidateProfile
    fields = ['email', 'phone_number', 'location', 'photo', 'note']
    template_name_suffix = '_update_form'


class CandidateDeleteView(DeleteView):
    model = CandidateProfile
    success_url = reverse_lazy('user-login')


class ChangePasswordView(SuccessMessageMixin, PasswordChangeView):
    template_name = 'change_password.html'
    success_message = "Successfully Changed Your Password"
    success_url = reverse_lazy('user-login')


class MyLoginView(LoginView):

    def get_success_url(self):
        if self.request.user.is_staff:
            return reverse('search')
        else:
            url = self.get_redirect_url()
            return url or reverse('profile-detail',
                                  kwargs={'pk': self.request.user.pk })


class CandidateProfileListView(generic.ListView):
    model = CandidateProfile


class CandidateProfileDetailView(generic.DetailView):
    model = CandidateProfile
