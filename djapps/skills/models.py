from django.db import models
import uuid

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Category(BaseModel):
    """Model definition for Category."""

    # TODO: Define fields here
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=True,db_index=True)
    name = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        """Meta definition for Category."""
        db_table = "skill"
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        """Unicode representation of Category."""
        return f"{self.name}"
    
class Skill(BaseModel):
    """Model definition for Skill."""

    # TODO: Define fields here
    id = models.UUIDField(name="Skill identification number",primary_key=True,default=uuid.uuid4,editable=False,db_index=True)
    name = models.CharField(max_length=50,null=True,blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,related_name="category")
    

    class Meta:
        """Meta definition for Skill."""

        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'

    def __str__(self):
        """Unicode representation of Skill."""
        return f"{self.name}"

class Methodology(BaseModel):
    """Model definition for Methodologies."""

    # TODO: Define fields here
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False,db_index=True)
    name = models.CharField(max_length=50,null=True,blank=True)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE,related_name="skill")

    class Meta:
        """Meta definition for Methodologies."""

        verbose_name = 'Methodologies'
        verbose_name_plural = 'Methodologies'

    def __str__(self):
        """Unicode representation of Methodologies."""
        return f"{self.name}"

class LearningPath(models.Model):
    """Model definition for LearningPath."""

    # TODO: Define fields here
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False,db_index=True)
    name = models.CharField(max_length=50,null=True,blank=True)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE,related_name="skill_learner")

    class Meta:
        """Meta definition for LearningPath."""

        verbose_name = 'LearningPath'
        verbose_name_plural = 'LearningPaths'

    def __str__(self):
        """Unicode representation of LearningPath."""
        return f"{self.name}"
