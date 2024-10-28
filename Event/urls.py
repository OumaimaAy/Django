from django.urls import path
from .forms import EventForm
from .views import AddEventView  # Import the renamed class


from .views import *
urlpatterns = [
    # path('bonjour/',  hello),
    
    # path('list/' , listEvent , name="list"),
    # path('add/' , AddEventView.as_view() , name="addEvent"),
        path('add/', AddEventView.as_view(), name='addEvent'),  # Correctly reference the class
        path('events/', EventListView.as_view(), name='eventList'),  # Ajoutez cette ligne

    # path('details/<int:ide>' , detailsEvent , name="details"),

    # path('listEvent/' , List.as_view()),
    # path('addEvent/' , add.as_view()),
    # path('update/<int:pk>' , UpdateEvent.as_view() , name="update"),
    # path('delete/<int:pk>' , DeleteEvent.as_view() , name="delete"),
    # path('participer/<int:eventId>' , participer , name="participer"),
    # path('cancel/<int:eventId>' , cancel , name="cancel"),
    # path('generate-description/' , generate_description , name="generate_description"),
    # path('generateImage/' , generate_image , name="generate_image"),

 

] 