from django.forms import ModelForm
from .models import CandidateProfile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CandidateForm(UserCreationForm):

    class Meta:
        model = CandidateProfile
        fields =['username',
                 'password1',
                 'password2',
                 'first_name',
                 'last_name',
                 'email',
                 'gender',
                 'age',
                 'phone_number',
                 'location',
                 'photo',
                 'note'
                 ]


class CandidateFormUpdate(ModelForm):

    class Meta:
        model = CandidateProfile
        fields = [
                 'email',
                 'phone_number',
                 'location',
                 'photo',
                 'note'
                 ]
