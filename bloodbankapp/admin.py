from django.contrib import admin
from .models import Donors,BRequests,Contact_Us

class BRequestsAdmin(admin.ModelAdmin):
	list_display=('patient_name','blood_group','status')
	
	def get_queryset(self,request):
		queryset=super(BRequestsAdmin,self).get_queryset(request)
		queryset=queryset.order_by('status','deadline','blood_group')
		return queryset


admin.site.register(Donors)
admin.site.register(BRequests,BRequestsAdmin)
admin.site.register(Contact_Us)
