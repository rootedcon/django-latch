from django.contrib import admin
from .models import LatchSetup

class LatchSetupAdmin(admin.ModelAdmin):
	list_display = ('latch_appid', 'latch_secret')
	def has_add_permission(self, request):
#		if LatchSetup.objects.all().count() == 0:
#			return True
#		return False
		return not LatchSetup.objects.exists()

admin.site.register(LatchSetup, LatchSetupAdmin)

	
