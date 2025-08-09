from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    context = {
        'movies' : ['Maze Runner', 'Spider Man', 'The Dark Knigh', 'The Man Of Steel']
    }
    return render(request, 'movies/index.html/', context)

def favseries(request):
    series = {
        'series': ['Teen Wolf', 'Outer Banks', 'Cobra Kai', 'Money Heist', "Stranger Things",
                   'Breaking Bad']
        }
    return render(request, 'movies/about.html/', series)
    

# appname/templates/appname/index.html
# movies/templates/movies/index.html
