from django.shortcuts import render

# Create your views here.
from .models import Player
from django.http import HttpResponse
from django.template import loader
from .forms import Team
from ypfcollection.models import Team
import logging
from django.utils import timezone
from django.shortcuts import redirect

def index(request):
    # return HttpResponse("Hello, world. You're at the ypf index.")
        # template = loader.get_template('ypf/index.html')
        return render(request,'ypfcollection/index.html',{'question':"foo"})

# def create_match(request):
    # player = Player.objects.all()
    # template = loader.get_template('ypfcollection/create-match.html')
    # context = {
    # 'player':player,
        # }
    # # return render(request,'ypfcollection/create-match.html',{'player':"foo"})
    # return HttpResponse(template.render(context, request))


	
def create_match(request):
    player = Player.objects.all()
    template = loader.get_template('ypfcollection/create-match.html')
    context = {
    'player':player,
        }
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
    p = Player.objects.all().order_by("-id")[0]
    if request.method == 'POST':
            for key in range(1,p.id + 1):
                                    # print(key,value)
                        data = request.POST.get('player' + str(key))
                        if data is not None:
                         q = Team(player_id = data,match_date = timezone.now())
                         logging.debug(q.player_id)
                         q.save()
                         logging.debug(q.id)
                        
            return redirect('ypfcollection:index')
            logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
            
    else:
     pass   # form = Team()
    return render(request, 'ypfcollection/create-match.html', {'player':player})   

# def collect_payments(request):
    # playing = Player.objects.filter(player__in=Team.objects.filter(match_date='2018-03-19 05:53:08.347028')
	
    # return render(request, 'ypfcollection/create-match.html', {'player':player})   
	
	# pass