from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from accounts.models import UserProfile, ClientProfile
from institution.models import Institution
from requestforms.models import Enquiry
from accounts.api.serializers import StudentSerializer, EnquiriesSerializer

# Create your views here.
@api_view(['GET'])
def StudentDetailAPI(request):
    student = get_object_or_404(UserProfile, user=request.user)
    serializer = StudentSerializer(student)
    return Response(serializer.data)


@api_view(['GET'])
def StudentEnquiriesAPI(request):
    student = get_object_or_404(UserProfile, user=request.user)
    enquiries = Enquiry.objects.filter(student=student)
    serializer = EnquiriesSerializer(enquiries)
    return Response(serializer.data)