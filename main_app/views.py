from django.shortcuts import render

finches = [
  {'breed': 'America Goldfinch', 'habitat': 'open woodlands', 'food': 'seeds'},
  {'breed': 'Black Rosy-Finch', 'habitat': 'tundra', 'food': 'seeds'},
  {'breed': 'Blue Grosbeak', 'habitat': 'open woodlands', 'food': 'insects'},
]

# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def finches_index(request):
  return render(request, 'finches/index.html', {
    'finches': finches
  })