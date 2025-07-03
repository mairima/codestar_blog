from django.shortcuts import render

# Create your views here.
def my_blog(request):
    if request.method == "POST":
        # handle post
    else:
        # render template or something
        return render(request, 'blog/index.html')