from rest_framework import serializers
from candidate_app.models import CandidateProfile


class CandidateProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CandidateProfile
        fields = [
            'id',
            'username',
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
