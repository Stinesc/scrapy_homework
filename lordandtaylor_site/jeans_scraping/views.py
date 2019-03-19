from django.shortcuts import render
from django.views.generic import ListView
from .models import Garment
import redis


class IndexView(ListView):
    template_name = "jeans_scraping/index.html"
    model = Garment

    def __init__(self, *args, **kwargs):
        self.r = redis.Redis()
        self.start_url = \
            "https://www.lordandtaylor.com/Men/Apparel/Jeans/shop/_/N-4ztf06/Ne-6ja3o7?sre=MHP_MODPE2_L1_PROMO_MENS"
        super().__init__(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.r.lpush('jeans:start_urls', self.start_url)
        return render(self.request, self.template_name)
