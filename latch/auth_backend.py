from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from .helpers import getLatchInstance, getLatchAccountId, getLatchAppId
from .models import LatchSetup
from latch import Latch
from django.core.exceptions import ValidationError


def latch_status(user):
    if  not LatchSetup.objects.exists():
    	# Always return on if is not configured.
    	return 'on'
    l = getLatchInstance()
    # We need to extend the User Config to
    accountID = getLatchAccountId(user)
    if not accountID: 
        # if the user does not have latch configured return on
        return 'on' 
    data = l.status(accountID)
    d = data.get_data()	
    return d['operations'][getLatchAppId()]['status']


class LatchAuthBackend(ModelBackend):
    def authenticate(self, username=None, password=None, **kwargs):
            UserModel = get_user_model()                      
            if username is None:
                username = kwargs.get(UserModel.USERNAME_FIELD)
            try:
                user = UserModel._default_manager.get_by_natural_key(username)
                if latch_status(user) == 'off':
                    UserModel().set_password(password)
                    return None
                if user.check_password(password):
                    return user
            except UserModel.DoesNotExist:
                # Run the default password hasher once to reduce the timing
                # difference between an existing and a non-existing user (#20760).
       	        UserModel().set_password(password)
            except Exception as err:
                raise ValidationError("There was an unknown error: %s" % err.strerror)
		
