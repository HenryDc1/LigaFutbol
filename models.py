# models.py

from django.db import models

class League(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Team(models.Model):
    name = models.CharField(max_length=200)
    league = models.ForeignKey(League, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Player(models.Model):
    name = models.CharField(max_length=200)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    number = models.IntegerField()

    def __str__(self):
        return self.name

class Match(models.Model):
    date = models.DateTimeField()
    home_team = models.ForeignKey(Team, related_name='home_matches', on_delete=models.CASCADE)
    away_team = models.ForeignKey(Team, related_name='away_matches', on_delete=models.CASCADE)
    league = models.ForeignKey(League, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.home_team} vs {self.away_team} - {self.date}"

class Event(models.Model):
    EVENT_TYPES = (
        ('G', 'Goal'),
        ('Y', 'Yellow Card'),
        ('R', 'Red Card'),
        ('F', 'Foul'),
    )
    type = models.CharField(max_length=1, choices=EVENT_TYPES)
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    time = models.TimeField()

    def __str__(self):
        return f"{self.type} - {self.player} - {self.match}"

class Goal(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    time = models.TimeField()

    def __str__(self):
        return f"Goal: {self.player} - {self.match}"
