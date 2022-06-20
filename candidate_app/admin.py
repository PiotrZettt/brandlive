from django.contrib import admin
from .models import CandidateProfile

# Register your models here.

admin.site.register(CandidateProfile)

class CandidateProfileAdmin(admin.ModelAdmin):
    model = CandidateProfile
    list_display = ['username',
                 'password1',
                 'password2',
                 'first_name',
                 'last_name',
                 'email',
                 'sex',
                 'age',
                 'phone_number',
                 'location',
                 'photo',
                 'note'
                ]
