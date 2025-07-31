from rest_framework.serializers import ModelSerializer

from djapps.skills.models import Category, LearningPath, Skill, Methodology


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class SkillSerializer(ModelSerializer):
    category = CategorySerializer(many = True)
    class Meta:
        model = Skill
        fields = (
            "name",
            "category",
        )
        
class MethodologySerializer(ModelSerializer):
    skill = SkillSerializer(many = True)
    class Meta:
        model = Methodology
        fields = (
            "name",
            "skill",
        )
        
class LearningPathSerializer(ModelSerializer):
    skill = SkillSerializer(many=True)
    class Meta:
        model = LearningPath
        fields = (
            "name",
            "skill",
        )