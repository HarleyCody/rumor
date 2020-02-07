from django.http import HttpResponse, HttpResponseRedirect
from src.RumorValidator import settings
DEFAULT_REFIRECT_URL = getattr(settings, "DEFAULT_REDIRECT_URL", "http://www.rumor.com:8000")

def wildcard_redirect(request, path=None):
    new_url = DEFAULT_REFIRECT_URL
    if path is not None:
        new_url = DEFAULT_REFIRECT_URL + "/" + path
    return HttpResponseRedirect(new_url)