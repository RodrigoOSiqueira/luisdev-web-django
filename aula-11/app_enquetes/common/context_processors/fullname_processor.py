def fullname_processor(request):
    context = {}
    if request.user and request.user.is_authenticated:
        context["fullname"] = f"{request.user.first_name} {request.user.last_name}"

    return context