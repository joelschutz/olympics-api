from django.db import models

# Create your models here.
class Athlete(models.Model):
    """
    Represents an olympic Athlete
    """
    name = models.CharField(
        blank=False,
        null=False,
        max_length=30
        )
    sex = models.CharField(
        blank=False,
        null=False,
        max_length=1
        )
    height = models.DecimalField(
        blank=True,
        null=True,
        decimal_places=1,
        max_digits=5
        )
    weight = models.DecimalField(
        blank=True,
        null=True,
        decimal_places=1,
        max_digits=5
        )

    class Meta:
        verbose_name = "Athlete"
        verbose_name_plural = "Athletes"

    def __str__(self):
        return self.name


class NOC(models.Model):
    """
    Represents an olympic NOC
    """
    noc = models.CharField(
        blank=False,
        null=False,
        max_length=3
        )
    region = models.CharField(
        blank=False,
        null=False,
        max_length=30
        )
    notes = models.CharField(
        blank=True,
        null=True,
        max_length=30
        )

    class Meta:
        verbose_name = "NOC"
        verbose_name_plural = "NOCs"

    def __str__(self):
        return self.region



class Game(models.Model):
    """
    Represents an olympic Game
    """
    year = models.IntegerField(
        blank=False,
        null=False
        )
    season = models.CharField(
        blank=False,
        null=False,
        max_length=6
        )
    city = models.CharField(
        blank=False,
        null=False,
        max_length=30
        )

    class Meta:
        verbose_name = "Game"
        verbose_name_plural = "Games"

    @property
    def name(self):
        return f'{self.year} {self.season}'

    def __str__(self):
        return self.name

class Sport(models.Model):
    """
    Represents an olympic Sport
    """
    name = models.CharField(
        blank=False,
        null=False,
        max_length=20
        )

    class Meta:
        verbose_name = "Sport"
        verbose_name_plural = "Sports"

    def __str__(self):
        return self.name

class Competition(models.Model):
    """
    Represents an olympic Competition
    """
    name = models.CharField(
        blank=False,
        null=False,
        max_length=200
        )
    sport = models.ForeignKey(
        "Sport", 
        verbose_name='sport', 
        on_delete=models.SET_NULL,
        blank=False,
        null=True)

    class Meta:
        verbose_name = "Competition"
        verbose_name_plural = "Competitions"

    def __str__(self):
        return self.name

class Medal(models.Model):

    name = models.CharField(
        blank=False,
        null=False,
        max_length=7
        )

    class Meta:
        verbose_name = "Medal"
        verbose_name_plural = "Medals"

    def __str__(self):
        return self.name


class Event(models.Model):
    """
    Represents an olympic Event
    """
    athlete = models.ForeignKey(
        'Athlete',
        related_name='events',
        on_delete=models.SET_NULL,
        blank=False,
        null=True
        )
    athlete_age = models.IntegerField(
        blank=False,
        null=True
        )
    athlete_team = models.CharField(
        blank=False,
        null=False,
        max_length=30
        )
    athlete_NOC = models.ForeignKey(
        'NOC',
        related_name='events',
        on_delete=models.SET_NULL,
        blank=False,
        null=True
        )
    game =  models.ForeignKey(
        'Game',
        related_name='events',
        on_delete=models.SET_NULL,
        blank=False,
        null=True
        )
    competition = models.ForeignKey(
        'Competition',
        related_name='events',
        on_delete=models.SET_NULL,
        blank=False,
        null=True
        )
    medal = models.ForeignKey(
        'Medal',
        related_name='events',
        on_delete=models.SET_NULL,
        blank=False,
        null=True
        )

    class Meta:
        verbose_name = "Event"
        verbose_name_plural = "Events"

    def __str__(self):
        return f'{self.athlete} - {self.competition} - {self.game.year}'


