from django.shortcuts import render
from django.views import View
from .models import Hobby, Kategori, SlagsModel

class Index(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'fritid/index.html')

class About(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'fritid/about.html')

class Slags(View):
    def get(self, request, *args, **kwargs):
        perler = Hobby.objects.filter(
            kategori__name__contains='Perler'
        )
        knipling = Hobby.objects.filter(
            kategori__name__contains='Knipling'
        )
        filt = Hobby.objects.filter(
            kategori__name__contains='Filt'
        )
        papir =Hobby.objects.filter(
            kategori__name__contains='Papir'
        )

        context = {
            'perler': perler,
            'knipling': knipling,
            'filt': filt,
            'papir': papir,
        }

        return render(request, 'fritid/slags.html', context)

    def post(self, request, *args, **kwargs):
        slags_items = {
            'items': []
        }

        items = request.POST.getlist('items[]')

        for item in items:
            hobby_item = Hobby.objects.get(pk__contains=int(item))
            item_data = {
                'id': hobby_item.pk,
                'titel': hobby_item.title,
                'pris': hobby_item.pris,
            }

            slags_items['items'].append(item_data)

            pris = 0
            items_ids = []

        for item in slags_items['items']:
            pris += item['pris']
            items_ids.append(item['id'])

        slags = SlagsModel.objects.create(pris=pris)
        slags.items.add(*items_ids)

        context = {
            'items': slags_items['items'],
            'pris': pris
        }

        return render(request, 'fritid/slags_confirmation.html', context)