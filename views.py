from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from .models import League, Match, Goal, Team, Player
from django.http import Http404


def league_detail(request):
    try:
        league = League.objects.first()
        if league is None:
            raise Http404("No leagues available.")
        matches = Match.objects.filter(league=league)
        teams = Team.objects.filter(league=league)  # Get the teams for the league
        return render(request, 'league_detail.html', {'league': league, 'matches': matches, 'teams': teams})
    except League.DoesNotExist:
        raise Http404("No leagues available.")
    
def match_detail(request, match_id):
    match = Match.objects.get(id=match_id)
    goals = Goal.objects.filter(match=match)
    return render(request, 'match_detail.html', {'match': match, 'goals': goals})

def team_detail(request, team_id):
    team = Team.objects.get(id=team_id)
    players = Player.objects.filter(team=team)
    return render(request, 'team_detail.html', {'team': team, 'players': players})

def player_ranking(request, league_id):
    league = League.objects.get(id=league_id)
    players = Player.objects.filter(team__in=league.teams.all()).order_by('-goals')
    return render(request, 'player_ranking.html', {'players': players})


def match_list(request):
    matches = Match.objects.all()
    return render(request, 'myapp/match_list.html', {'matches': matches})

def match_detail(request, pk):
    match = Match.objects.get(pk=pk)
    return render(request, 'myapp/match_detail.html', {'match': match})