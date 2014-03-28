from django.http import HttpResponse

def index(request):
	return HttpResponse("Rangoapp says Hiiiii! <a href='/rangoapp/about'>About</a>")

def about(request):
	return HttpResponse("RangoApp! Its about page! <a href='/rangoapp'>Index</a>")