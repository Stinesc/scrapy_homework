from django.shortcuts import render
from django.views.generic import ListView
from .models import Garment
import redis

redis_connection = redis.Redis(host='localhost', port=6379)


class IndexView(ListView):
    template_name = "jeans_scraping/index.html"
    model = Garment
    start_url = \
            "https://www.lordandtaylor.com/Men/Apparel/Jeans/shop/_/N-4ztf06/Ne-6ja3o7?sre=MHP_MODPE2_L1_PROMO_MENS"

    def post(self, request, *args, **kwargs):
        Garment.objects.all().delete()
        redis_connection.lpush('jeans:start_urls', self.start_url)
        return render(request, self.template_name)
