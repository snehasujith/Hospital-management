from django.contrib import admin

# Register your models here.
from.models import Department,Doctors,Booking
admin.site.register(Department)
admin.site.register(Doctors)

class BookindAdmin(admin.ModelAdmin):
    list_display = ('id', 'p_name', 'p_email', 'doc_name', 'booking_date','booked_on')

admin.site.register(Booking, BookindAdmin)