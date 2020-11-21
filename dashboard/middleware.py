from .models import GlobalPageHit, Visitor, VisitorPageHit
from django.db.models import F
from django.urls import reverse
from django.conf import settings

from ipware import get_client_ip
import ipinfo
import bleach

class PageViewsMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        requested_url = bleach.clean(request.path)
        
        if reverse('admin:index') in requested_url or \
            reverse('admin:index') + 'login/' in requested_url or \
            requested_url is reverse('admin:index') or \
            'dashboard' in requested_url:
            return self.get_response(request)

        # Create the GlobalPageHit
        page_hit, page_hit_created = GlobalPageHit.objects.get_or_create(page_url=requested_url)
        page_hit.hit_count = F('hit_count') + 1
        page_hit.save()

        # Create the Visitor
        visitor_ip = get_client_ip(request)

        visitor = Visitor.objects.create(ip_address=visitor_ip[0]) 

        # if the ip is not localhost then do a lookup of the country for the ip and the visitor doesn't already exist
        if visitor_ip[0] not in ('localhost', '127.0.0.1'):
            visitor_exists = Visitor.objects.filter(ip_address=visitor_ip[0]).exclude(ip_country='').first()
            if not visitor_exists.exists():
                handler = ipinfo.getHandler(settings.IPINFO_API_KEY)
                details = handler.getDetails(str(visitor_ip[0]))
                if details.country_name is not None:
                    visitor.ip_country = details.country_name
                if details.country is not None:
                    visitor.country_code = details.country
            else:
                visitor.ip_country = visitor_exists.ip_country
                visitor.country_code = visitor_exists.country_code

            visitor.user_agent = request.META['HTTP_USER_AGENT']
            visitor.save()

        if not 'favicon' in requested_url:
            # Create the VisitorPageHit (adds a new entry for each visitor that visits a page)
            visitor_page_hit = VisitorPageHit.objects.create(page_url=requested_url, visitor=visitor)
            visitor_page_hit.user_agent = request.META['HTTP_USER_AGENT']
            visitor_page_hit.referer = request.META.get('HTTP_REFERER', '')
            visitor_page_hit.save() 

        return self.get_response(request)