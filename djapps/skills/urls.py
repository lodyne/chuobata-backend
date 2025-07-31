from django.urls import path

from djapps.skills.views import (
    CategoryView,
    LearningPathView,
    MethodologyView,
    SkillView,
)

app_name = "skills"

urlpatterns = [
    path("category/", CategoryView.as_view(), name="category"),
    path("skill/", SkillView.as_view(), name="skill"),
    path("methodology/", MethodologyView.as_view(), name="methodology"),
    path("learning_path/", LearningPathView.as_view(), name="learning_path"),
]
