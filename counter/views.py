from django.shortcuts import render
from django.http import HttpResponse

from counter.models import Counter

# Create your views here.
def index(request):
	total = Counter.objects.all().count()
	visitors = Counter.objects.all()
	current_ip = get_current_ip(request)
	context = {'total_online_users': total,'visitors_online':visitors,'curr_ip':current_ip}
	return render(request, 'counter/index.html',context)

def get_visitor_count(request):
	total = Counter.objects.all().count()
	return HttpResponse(total)

def get_current_ip(request):
	x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
	if x_forwarded_for:
		ip = x_forwarded_for.split(',')[0]
	else:
		ip = request.META.get('REMOTE_ADDR')
		return ip

def end_session(request):
	v_ip = get_current_ip(request)
	Counter.objects.filter(ip=v_ip).delete()
	return HttpResponse(v_ip)
