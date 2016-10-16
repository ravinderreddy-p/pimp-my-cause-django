from __future__ import unicode_literals

from django.db import models
from custom_user.models import AbstractEmailUser
from django_countries.fields import CountryField
from s3direct.fields import S3DirectField

class PimpUser(AbstractEmailUser):

    MARKETER = 0
    CAUSE = 1
    USER_TYPE_CHOICES = (
        (MARKETER, "Marketer"),
        (CAUSE, "Cause")
    )

    # basic info
    name = models.CharField(max_length=24, blank=True)
    surname = models.CharField(max_length=24, blank=True)
    phone = models.CharField(max_length=15, blank=True)
    country = CountryField(blank=True)
    city = models.CharField(max_length=85, blank=True)
    postcode = models.CharField(max_length=12, blank=True)

    # professional info
    position = models.CharField(max_length=100, blank=True)
    usertype = models.IntegerField(choices=USER_TYPE_CHOICES, null=True)
    bio = models.CharField(max_length=1000, blank=True)

    # social accounts
    twitter = models.URLField(max_length=100, blank=True)
    linkedin = models.URLField(max_length=100, blank=True)
    website = models.URLField(max_length=100, blank=True)

    image = S3DirectField(dest='user-profile-images', blank=True)
    featured = models.BooleanField(default=False)

class Qualification(models.Model):
    Advertising = models.BooleanField(default=True)
    Branding = models.BooleanField(default=False)
    BusinessDevelopment = models.BooleanField(default=False)
    CustomerInsights = models.BooleanField(default=False)
    DigitalMarketing = models.BooleanField(default=False)
    GraphicDesign = models.BooleanField(default=False)
    Innovation = models.BooleanField(default=False)
    Marketing = models.BooleanField(default=False)
    PR = models.BooleanField(default=False)
    SEO = models.BooleanField(default=False)
    SocialMediaMarketing = models.BooleanField(default=False)
    StrategicMarketing = models.BooleanField(default=False)
    Videography = models.BooleanField(default=False)
    WebDevelopment = models.BooleanField(default=False)

class MarketerProfile(models.Model):
    profile = models.ForeignKey(
        PimpUser,
        limit_choices_to={'usertype': PimpUser.CAUSE }
    )

    qualification = models.ForeignKey(Qualification, on_delete=models.CASCADE)
    experience = models.CharField(max_length=1000, blank=True)
    availability = models.BooleanField(default=True)

class CauseProfile(models.Model):

    DISASTER_RELIEF = 0
    POVERTY_ALLEVIATION = 1
    ENVIRONMENT = 2
    EDUCATION_AND_SKILLS = 3
    ANIMAL_WELFARE = 4
    CHILDREN_AND_YOUTH = 5
    DISABILITY = 6
    HEALTH = 7
    FOOD = 8
    FAMILY_SUPPORT = 9
    CARE_FOR_THE_ELDERY = 10

    CAUSE_CATEGORY_CHOICES = (
        (DISASTER_RELIEF, "Disaster Relief"),
        (POVERTY_ALLEVIATION, "Poverty Alleviation"),
        (ENVIRONMENT, "Environment"),
        (EDUCATION_AND_SKILLS, "Education and Skills"),
        (ANIMAL_WELFARE, "Animal Welfare"),
        (CHILDREN_AND_YOUTH, "Children and Youth"),
        (DISABILITY, "Disability"),
        (HEALTH, "Health"),
        (FOOD, "Food"),
        (FAMILY_SUPPORT, "Family Support"),
        (CARE_FOR_THE_ELDERY, "Care for the Eldery")
    )

    profile = models.ForeignKey(
        PimpUser,
        limit_choices_to={'usertype': PimpUser.CAUSE }
    )

    mission = models.CharField(max_length=1000, blank=True)
    categories = models.CharField(max_length=8, choices=CAUSE_CATEGORY_CHOICES, blank=True)
