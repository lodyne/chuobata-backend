from rest_framework.generics import ListCreateAPIView

from djapps.skills.models import Category, LearningPath, Skill, Methodology
from djapps.skills.serializers import CategorySerializer, LearningPathSerializer, MethodologySerializer, SkillSerializer

class CategoryView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
class SkillView(ListCreateAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    
class MethodologyView(ListCreateAPIView):
    queryset = Methodology.objects.all()
    serializer_class = MethodologySerializer
    
class LearningPathView(ListCreateAPIView):
    queryset = LearningPath.objects.all()
    serializer_class = LearningPathSerializer

