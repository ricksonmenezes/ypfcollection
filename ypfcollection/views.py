from django.shortcuts import render

# Create your views here.
from .models import Player
from django.http import HttpResponse
from django.template import loader
from .forms import Team
from ypfcollection.models import Team
from ypfcollection.models import Match
import logging
from django.utils import timezone
from django.shortcuts import redirect
import datetime
from django.http import JsonResponse

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
    # return render(request,'ypfcollection/create-match.html',{'player':"foo"})
    # return HttpResponse(template.render(context, request))


        
def create_match(request):
    player = Player.objects.all()
    template = loader.get_template('ypfcollection/create-match.html')
    context = {
    'player':player,
        }
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
    # logging.debug('reaches before')
    p = Player.objects.all().order_by("-id")[0]
    if request.method == 'POST':
            # logging.debug('also ' + str(p.id))
            for key in range(1,p.id + 1):
                                    # print(key,value)
                        data = request.POST.get('player' + str(key))
                        if data is not None:
                         q = Team(player_id = data,match_date = timezone.now())
                         # logging.debug(q.player_id)
                         q.save()
                         # logging.debug(q.id)
                         addMatchFee = True
            if addMatchFee is True:
              logging.debug('reaches')
              m = Match.objects.filter(match_date__contains=datetime.date.today())
              if not m:
               m = Match(amount = request.POST.get('matchfee'),match_date = timezone.now())
               m.save()
            return redirect('ypfcollection:index')
            logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
            
    else:
     pass
    return render(request, 'ypfcollection/create-match.html', {'player':player})   

def collect_payments(request):
    if request.method == 'POST':
     logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
     logging.debug('reaches after post')
     p = Player.objects.all().order_by("-id")[0]
     for key in range(1,p.id + 1):
                                    
                        data = request.POST.get('creditamt' + str(key))
                        logging.debug('credit: ' +str(data))
                        if data is not None:
                         Player.objects.filter(pk=key).update(amount=data)
    
     return redirect('ypfcollection:index')
    else:
	
     player = Player.objects.filter(id__in=Team.objects.filter(match_date__gte=timezone.now().date()).values_list('player_id',flat=True))
     match = Match.objects.filter(match_date__contains=datetime.date.today()).first()
     logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
     logging.debug('comes here?')
     context = {'player':player, 'match':match}
     # return render(request, 'ypfcollection/collect-payments.html', {'player':player,'match':match})   
     return render(request, 'ypfcollection/collect-payments.html', context)   
    pass
	
def get_credit(request):
    userId = request.GET['playerid']
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
    logging.debug('valueuserid' + str(userId))
    data = {
     'creditamt': Player.objects.filter(id=userId).values_list('amount',flat=True).first()
    }
    return JsonResponse(data)
    pass
