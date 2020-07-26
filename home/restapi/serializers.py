from home.models import jschapters, jsdescription
from rest_framework import serializers

class jschaptersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = jschapters
        fields = ['url', 'sno', 'chapter_name']

class jsdescriptionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = jsdescription
        fields = ['url', 'sno', 'title', 'chapters', 'description']