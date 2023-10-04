from django.http import HttpResponseRedirect


def index(_):
    return HttpResponseRedirect("store/get/")
