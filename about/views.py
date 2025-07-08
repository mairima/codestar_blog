from django.shortcuts import render

# Create your views here.
def about(request):
    context = {
        "about": {
            "title": "About Me",
            "content": "<p>Hi there! I'm learning Django.</p>",
            "updated_on": "2025-07-08",
        }
    }
    return render(request, 'about/about.html', context)