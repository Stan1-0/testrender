from rest_framework import serializers, viewsets
from .models import Project, Description

class DescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Description
        fields = ['id', 'description']

class ProjectSerializer(serializers.ModelSerializer):
    Descriptions = DescriptionSerializer(many=True)
    image = serializers.ImageField(source='Project_photo')
    live_link_url = serializers.URLField(source='live_site_url')
    
    class Meta:
        model = Project
        fields = ['Company', 'Project_name', 'year', 'Project_photo', 'live_site_url', 'Descriptions']

    def create(self, validated_data):
        Descriptions_data = validated_data.pop('Descriptions')  # Updated to 'Descriptions'
        project = Project.objects.create(**validated_data)
        for Description_data in Descriptions_data:
            Description.objects.create(project=project, **Description_data)
        return project

    def update(self, instance, validated_data):
        Descriptions_data = validated_data.pop('Descriptions')  # Updated to 'Descriptions'
        instance.Company = validated_data.get('Company', instance.Company)
        instance.year = validated_data.get('year', instance.year)
        instance.Project_name = validated_data.get('Project_name', instance.Project_name)
        instance.live_site_url = validated_data.get('live_site_url', instance.live_site_url)
        instance.Project_photo = validated_data.get('Project_photo', instance.Project_photo)
        instance.save()

        # Update results
        keep_Descriptions = []
        for Description_data in Descriptions_data:
            if 'id' in Description_data:
                Description = Description.objects.get(id=Description_data['id'], project=instance)
                Description.description = Description_data.get('description', Description.description)
                Description.save()
                keep_Descriptions.append(Description.id)
            else:
                Description = Description.objects.create(project=instance, **Description_data)
                keep_Descriptions.append(Description.id)

        # Remove results not included in the request
        instance.results.exclude(id__in=keep_Descriptions).delete()

        return instance

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
