from django.http import JsonResponse


def store_list(_):
    return JsonResponse({"msg": "store_list summoned"})