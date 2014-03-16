from django.http import HttpResponseRedirect, HttpResponse
from django.conf import settings
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from .models import LatchSetup, UserProfile
from .forms import LatchPairForm, LatchUnpairForm
from .helpers import getLatchInstance, getLatchAccountId, saveUserAccountId, get_or_create_profile
# Create your views here.

# TODO:
# - use a signal 'delete user' to delete the paired apps
# - add userprofile management to the admin
# 

@login_required
def pair (request, template_name='latch_pair.html'):
    if not LatchSetup.objects.exists():
        return render_to_response('latch_message.html', { 'message': 'Latch is not configured', 'alert_type': 'danger'}, context_instance=RequestContext(request))
    try:
        if getLatchAccountId(request.user) != None:
            return render_to_response('latch_message.html', { 'message': 'Account is already paired', 'alert_type': 'danger'}, context_instance=RequestContext(request))
    except:
           pass
        

    if request.method == 'POST':
        form = LatchPairForm(request.POST)
        if form.is_valid():
            lt = getLatchInstance()
            form.clean()
            # review this code with internet connection
            try:
                accountId = lt.pair(form.cleaned_data['latch_pin'])
                if accountId.get_data().has_key('accountId'):
                    saveUserAccountId(request.user, accountId.get_data()['accountId'])
                    return render_to_response('latch_message.html', { 'message': 'Account paired with Latch', 'alert_type': 'success'}, context_instance=RequestContext(request))
                return render_to_response('latch_message.html', { 'message': 'Account not paired with Latch', 'alert_type': 'danger'}, context_instance=RequestContext(request))
            except Exception as e:
               return render_to_response('latch_message.html', { 'message': 'Error pairing the account: %s' % e, 'alert_type': 'danger'}, context_instance=RequestContext(request))
    else:
        form = LatchPairForm()
    
    return render_to_response(template_name, { 'form': form }, context_instance=RequestContext(request))

@login_required
def unpair (request, template_name='latch_unpair.html'):
    if request.method == 'POST':
        form = LatchUnpairForm(request.POST)
        if form.is_valid():
            do_unpair(request)
    else:
        form = LatchUnpairForm()
    return render_to_response(template_name, { 'form': form }, context_instance=RequestContext(request))

def do_unpair(request, template_name='latch_unpair.html'):
    try:
        if getLatchAccountId():
            lt = getLatchInstance()
            lt.unpair(getLatchAccountId())
        else:
            return render_to_response('latch_message.html', { 'message': 'Your account is not latched', 'alert_type': 'success'}, context_instance=RequestContext(request))
    except UserProfile.DoesNotExist:
        return render_to_response('latch_message.html', { 'message': 'Your account has no profile', 'alert_type': 'danger'}, context_instance=RequestContext(request))
    except Exception as e:
        return render_to_response('latch_message.html', { 'message': 'Error unpairing the account: %s' % e, 'alert_type': 'danger'}, context_instance=RequestContext(request))

# Ccomment the following line if you want to have public status report
@login_required 
def status (request, template_name='latch_status.html'):
    status = []
    if not LatchSetup.objects.exists():     
        status.append('Latch is configured: <b>No</b>')
    else:
        status.append('Latch is configured: <b>Yes</b>')
        lt = getLatchInstance()
        # Clean this part
        appid = getLatchAccountId(request.user) 
        if not appid or len(appid) == 0:
            appid = 'Not configured'
        status.append( 'Your application id is: <b>%s</b>' % appid )
        try:
            acstatus = lt.status(appid)
            if acstatus:        
                d = acstatus.get_data()['operations']
                status.append('Account status: <b>%s</b>' % d.values()[0]['status']) 
                status.append('Application name: <b>%s</b>'%  d.values()[0]['name'])
        except Exception as e:
            status.append('Latch connection error: <b>%s</b>' %  e.message  )
    print status
    return render_to_response(template_name, { 'status': status }, context_instance=RequestContext(request))
            
        
