from django.db import models
from django.core.validators import MaxValueValidator

# Create your models here.
class User(models.Model):
    # hash_token = models.TextField()
    student_id = models.CharField(max_length=50, unique=True)
    apply_count = models.IntegerField(default=0, validators=[
        MaxValueValidator(3)
    ])
    apply_major_list = models.TextField()

    def __str__(self):
        return self.student_id

class ApplyList(models.Model):
    business_administration = models.TextField(default="", blank=True)
    korean_language = models.TextField(default="", blank=True)
    english_language = models.TextField(default="", blank=True)
    philosophy = models.TextField(default="", blank=True)
    korean_history = models.TextField(default="", blank=True)
    history = models.TextField(default="", blank=True)
    psychology = models.TextField(default="", blank=True)
    sociology = models.TextField(default="", blank=True)
    german_language = models.TextField(default="", blank=True)
    french_language = models.TextField(default="", blank=True)
    chinese_language= models.TextField(default="", blank=True)
    russian_language = models.TextField(default="", blank=True)
    japanese_language= models.TextField(default="", blank=True)
    spanish_language = models.TextField(default="", blank=True)
    chinese_character = models.TextField(default="", blank=True)
    linguistic = models.TextField(default="", blank=True)
    bio_science= models.TextField(default="", blank=True)
    bio_technology= models.TextField(default="", blank=True)
    food_engineering = models.TextField(default="", blank=True)
    ecology_engineering = models.TextField(default="", blank=True)
    food_resource_technology= models.TextField(default="", blank=True)
    political_science= models.TextField(default="", blank=True)
    economics = models.TextField(default="", blank=True)
    administration= models.TextField(default="", blank=True)
    statistics = models.TextField(default="", blank=True)
    mathematics = models.TextField(default="", blank=True)
    physics = models.TextField(default="", blank=True)
    chemistry = models.TextField(default="", blank=True)
    earth_environment_science = models.TextField(default="", blank=True)
    chemical_engineering_bio_technology= models.TextField(default="", blank=True)
    new_materials_engineering= models.TextField(default="", blank=True)
    architecture_environment = models.TextField(default="", blank=True)
    architecture = models.TextField(default="", blank=True)
    mechanical_engineering= models.TextField(default="", blank=True)
    industry_business= models.TextField(default="", blank=True)
    electronic_engineering= models.TextField(default="", blank=True)
    education = models.TextField(default="", blank=True)
    physical_education = models.TextField(default="", blank=True)
    home_education = models.TextField(default="", blank=True)
    mathematics_education = models.TextField(default="", blank=True)
    korean_education= models.TextField(default="", blank=True)
    english_education= models.TextField(default="", blank=True)
    geographic_education = models.TextField(default="", blank=True)
    history_education = models.TextField(default="", blank=True)
    design_modeling= models.TextField(default="", blank=True)
    international_study = models.TextField(default="", blank=True)
    media = models.TextField(default="", blank=True)
    bio_technology= models.TextField(default="", blank=True)
    bio_system_science= models.TextField(default="", blank=True)
    health_environment_science= models.TextField(default="", blank=True)
    health_policy= models.TextField(default="", blank=True)
    

