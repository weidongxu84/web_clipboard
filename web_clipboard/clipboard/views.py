# Create your views here.

from django.template import RequestContext, loader
from django.http import HttpResponse, HttpResponseRedirect
from clipboard.models import Clip, User
from clipboard.forms import AddClipForm

def index(request):
    clip_list = Clip.objects.all().order_by('-pub_date')[:10]
    template = loader.get_template('clipboard/index.html')
    form = AddClipForm()
    context = RequestContext(request, {
        'clip_list': clip_list,
        'add_clip_form': form,
    })
    return HttpResponse(template.render(context))
    
def add_clip(request):
    if request.method == 'POST':
        form = AddClipForm(request.POST)
        if form.is_valid():
            user_ip = request.META.get('REMOTE_ADDR')
            try:
                user = User.objects.get(ip_addr=user_ip)
            except (KeyError, User.DoesNotExist):
                user = User(username='anonymous', ip_addr=user_ip)
                user.save()
            text = request.POST['content_text']
            clip = Clip(content_text=text, user=user)
            clip.save()
    return HttpResponseRedirect('..')
