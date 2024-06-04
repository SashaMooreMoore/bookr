from django.shortcuts import render


# def index(request):
#     name = request.GET.get("name") or "world"
#     return HttpResponse(f"Hello {name}!")


def index(request):
    name = "World"
    return render(request, "base.html", {"name": name})
    # return render(request, "base.html")


def book_search(request):
    search_text = request.GET.get("search", "")
    return render(request, "search-results.html", {"search_text": search_text})