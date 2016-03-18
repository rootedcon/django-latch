from .models import LatchSetup, UserProfile
from latch import Latch

def getLatchInstance():
        if not LatchSetup.objects.exists():
                return None
        ls = LatchSetup.objects.get(id=1)
        return Latch(ls.latch_appid, ls.latch_secret)

def getLatchAppId():
    if not LatchSetup.objects.exists():
        return None
    ls = LatchSetup.objects.get(id=1)
    return ls.latch_appid

def getLatchAccountId(user):
    try:
        appid = user.userprofile.latch_accountId
        return appid
    except:
        return None

def get_or_create_profile(user):
    profile = None
    try:
        profile = user.get_profile()
    except UserProfile.DoesNotExist:
        profile = UserProfile.objects.create(user=user)
    return profile

def saveUserAccountId(user, accountId):
    profile = get_or_create_profile(user)
    profile.latch_accountId = accountId
    profile.save()
    
def deleteUserAccountId(accountId):
    try:
        UserProfile.objects.get(latch_accountId = accountId).delete()
    except UserProfile.DoesNotExist:
        return None
