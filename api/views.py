from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import CandidateProfileSerializer
from candidate_app.models import CandidateProfile
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from .serializers import CandidateProfileSerializer
from rest_framework import viewsets
from rest_framework import permissions


class ProfileViewSets(viewsets.ModelViewSet):

    queryset = CandidateProfile.objects.all()
    serializer_class = CandidateProfileSerializer
    permissions = [permissions.IsAuthenticated]



# def front(request):
#     context = {}
#     return render(request, 'index.html', context)

# @api_view(['GET', "POST"])
# def candidate_api(request):
#     if request.method == 'GET':
#         candidates = CandidateProfile.objects.all()
#         serializer = CandidateProfileSerializer(candidates, many=True)
#         return Response(serializer.data)
#
#     elif request.method == 'POST':
#         serializer = CandidateProfileSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
# @api_view(['DELETE', 'GET', 'PUT'])
# def candidate_detail(request, pk):
#     try:
#         candidate = CandidateProfile.objects.get(pk=pk)
#     except ObjectDoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#         serializer = CandidateProfileSerializer(candidate)
#         return Response(serializer.data)
#
#     elif request.method == 'PUT':
#         serializer = CandidateProfileSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     elif request.method == 'DELETE':
#         candidate.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
