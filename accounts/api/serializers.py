from rest_framework import serializers

from accounts.models import UserProfile
from requestforms.models import Enquiry


class StudentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = UserProfile
        fields = ('id', 'about_me', 'gender', 'birth', 'address', 'zipcode', 'phone')



class EnquiriesSerializer(serializers.ModelSerializer):
    institution_interested = serializers.RelatedField(source='institution_interested')
    country_interested = serializers.RelatedField(source='country_interested')
    study_level_interested = serializers.RelatedField(many=True)
    area_interested = serializers.RelatedField(many=True)
    institution_interested = serializers.RelatedField(many=True)
    
    class Meta:
        model = Enquiry
        ordering = ['created']
        fields = ('id', 'content', 'expected_time',  'institution_interested', 'country_interested',
            'study_level_interested', 'area_interested', 'institution_interested',
            'created', 'more_info')

