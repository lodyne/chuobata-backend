from django.db import models
import uuid


class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category(BaseModel):
    """Model definition for Category."""

    name = models.CharField(max_length=50)

    class Meta:
        """Meta definition for Category."""

        db_table = "category"
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        """Unicode representation of Category."""
        return f"{self.name}"


class Skill(BaseModel):
    """Model definition for Skill."""

    name = models.CharField(max_length=50)
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        db_column="category_id",
        related_name="skills",
    )

    class Meta:
        """Meta definition for Skill."""

        db_table = "skill"
        verbose_name = "Skill"
        verbose_name_plural = "Skills"

    def __str__(self):
        """Unicode representation of Skill."""
        return f"{self.name}"


class Methodology(BaseModel):
    """Model definition for Methodologies."""

    name = models.CharField(max_length=50)
    skill = models.ForeignKey(
        Skill,
        on_delete=models.CASCADE,
        db_column="skill_id",
        related_name="methodologies",
    )

    class Meta:
        """Meta definition for Methodologies."""

        db_table = "methodology"
        verbose_name = "Methodology"
        verbose_name_plural = "Methodologies"

    def __str__(self):
        """Unicode representation of Methodologies."""
        return f"{self.name}"


class LearningPath(BaseModel):
    """Model definition for LearningPath."""

    name = models.CharField(max_length=50, null=True, blank=True)
    skill = models.ForeignKey(
        Skill,
        on_delete=models.CASCADE,
        db_column="skill_id",
        related_name="learning_paths",
    )

    class Meta:
        """Meta definition for LearningPath."""

        db_table = "learning_path"
        verbose_name = "LearningPath"
        verbose_name_plural = "LearningPaths"

    def __str__(self):
        """Unicode representation of LearningPath."""
        return f"{self.name}"
