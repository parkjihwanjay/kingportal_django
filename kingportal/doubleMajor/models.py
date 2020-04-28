from django.db import models
from django.core.validators import MaxValueValidator

# Create your models here.
class User(models.Model):
    student_id = models.CharField(max_length=50, unique=True)
    apply_count = models.IntegerField(default=0, validators=[
        MaxValueValidator(3)
    ])
    apply_major_list = models.TextField()

    def __str__(self):
        return self.student_id

class ApplyList(models.Model):
    business_administration = models.TextField(default="")
    korean_language = models.TextField(default="")
    english_language = models.TextField(default="")
    philosophy = models.TextField(default="")
    korean_history = models.TextField(default="")
    history = models.TextField(default="")
    psychology = models.TextField(default="")
    sociology = models.TextField(default="")
    german_language = models.TextField(default="")
    french_language = models.TextField(default="")
    chinese_language= models.TextField(default="")
    russian_language = models.TextField(default="")
    japanese_language= models.TextField(default="")
    spanish_language = models.TextField(default="")
    chinese_character = models.TextField(default="")
    linguistic = models.TextField(default="")
    bio_science= models.TextField(default="")
    bio_technology= models.TextField(default="")
    food_engineering = models.TextField(default="")
    ecology_engineering = models.TextField(default="")
    food_resource_technology= models.TextField(default="")
    political_science= models.TextField(default="")
    economics = models.TextField(default="")
    administration= models.TextField(default="")
    statistics = models.TextField(default="")
    mathematics = models.TextField(default="")
    physics = models.TextField(default="")
    chemistry = models.TextField(default="")
    earth_environment_science = models.TextField(default="")
    chemical_engineering_bio_technology= models.TextField(default="")
    new_materials_engineering= models.TextField(default="")
    architecture_environment = models.TextField(default="")
    architecture = models.TextField(default="")
    mechanical_engineering= models.TextField(default="")
    industry_business= models.TextField(default="")
    electronic_engineering= models.TextField(default="")
    education = models.TextField(default="")
    physical_education = models.TextField(default="")
    home_education = models.TextField(default="")
    mathematics_education = models.TextField(default="")
    korean_education= models.TextField(default="")
    english_education= models.TextField(default="")
    geographic_education = models.TextField(default="")
    history_education = models.TextField(default="")
    design_modeling= models.TextField(default="")
    international_study = models.TextField(default="")
    media = models.TextField(default="")
    bio_technology= models.TextField(default="")
    bio_system_science= models.TextField(default="")
    health_environment_science= models.TextField(default="")
    health_policy= models.TextField(default="")
    

