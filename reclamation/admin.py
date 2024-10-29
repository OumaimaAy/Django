from django.contrib import admin
from .models import Reclamation,Response
from django.db import models  # Import models to resolve the undefined variable error

# Register your models here.

@admin.register(Reclamation)
class ReclamationAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'status', 'priority', 'category', 'sentiment', 'created_at')
    list_filter = ('status', 'priority', 'category')
    search_fields = ('title', 'description', 'user__username')

     # Custom method to convert sentiment values to numeric order
    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        sentiment_order = {
            "Very Negative": 1,
            "Negative": 2,
            "Neutral": 3,
            "Positive": 4,
            "Very Positive": 5,
        }
        # Annotate queryset with a numeric sentiment order
        return queryset.annotate(
            sentiment_order_num=models.Case(
                models.When(sentiment="Very Negative", then=models.Value(1)),
                models.When(sentiment="Negative", then=models.Value(2)),
                models.When(sentiment="Neutral", then=models.Value(3)),
                models.When(sentiment="Positive", then=models.Value(4)),
                models.When(sentiment="Very Positive", then=models.Value(5)),
                default=models.Value(3),  # Default to 'Neutral'
                output_field=models.IntegerField(),
            )
        ).order_by('sentiment_order_num')  # Sort by numeric sentiment order
    
    
@admin.register(Response)
class ResponseAdmin(admin.ModelAdmin):
    list_display = ('reclamation', 'user', 'content', 'created_at')
    search_fields = ('reclamation__title', 'user__username', 'content')
    list_filter = ('created_at', 'reclamation__status')
    raw_id_fields = ('reclamation',)


