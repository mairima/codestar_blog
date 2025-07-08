from django.shortcuts import render
from django.views import generic
from .models import Post, Comment, Event

class EventsList(generic.ListView):
    model = Event
    template_name = 'events/events_list.html'  # use your correct template
    context_object_name = 'events'
    
def event_detail(request, event_id):
    # you can later fetch event by ID, but keep it simple for now
    return render(request, "events/event_detail.html", {"event_id": event_id})