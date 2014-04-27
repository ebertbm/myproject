from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from accounts.models import ClientProfile
from requestforms.models import Enquiry
from accounts.api.serializers import EnquiriesSerializer


@api_view(['GET'])
def InstitutionEnquiriesAPI(request):
    client = get_object_or_404(ClientProfile, user=request.user)
    enquiries = Enquiry.objects.filter(client=client)
    serializer = EnquiriesSerializer(enquiries)
    return Response(serializer.data)