from django.contrib import admin

from .models import Person
# Register your models here.


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    
    search_fields=['username' ,'email','cin']
    
    list_display=('username','email','cin',)# Register your models here.


