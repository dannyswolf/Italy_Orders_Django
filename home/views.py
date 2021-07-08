from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView
from Spareparts.models import SpareParts
from warehouse.models import (SHARP, KONICA, RICOH, SAMSUNG, EPSON, KYOCERA, OKI, CANON, BROTHER, LEXMARK)


class HomeView(LoginRequiredMixin, ListView):
    model = SpareParts
    template_name = 'home/home.html'
    success_url = reverse_lazy("home")

    def get_context_data(self, *args, **kwargs):
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context['object_list'] = SpareParts.objects.all()

        for obj in context['object_list']:
            obj.pieces = "<font color='red'>Δεν βρέθηκε ο κωδικός</font>"
            if 'konica' in str(obj.Μηχάνημα).lower():
                try:
                    pieces = KONICA.objects.filter(ΚΩΔΙΚΟΣ=f"{obj.ml_code}").first()
                    obj.pieces = pieces.ΤΕΜΑΧΙΑ
                except AttributeError:
                    pass

            elif 'sharp' in str(obj.Μηχάνημα).lower():
                try:
                    pieces = SHARP.objects.filter(ΚΩΔΙΚΟΣ=f"{obj.ml_code}").first()
                    obj.pieces = pieces.ΤΕΜΑΧΙΑ
                except AttributeError:
                    pass

            elif 'ricoh' in str(obj.Μηχάνημα).lower():
                try:
                    pieces = RICOH.objects.filter(ΚΩΔΙΚΟΣ=f"{obj.ml_code}").first()
                    obj.pieces = pieces.ΤΕΜΑΧΙΑ
                except AttributeError:
                    pass
            elif 'samsung' in str(obj.Μηχάνημα).lower():
                try:
                    pieces = SAMSUNG.objects.filter(ΚΩΔΙΚΟΣ=f"{obj.ml_code}").first()
                    obj.pieces = pieces.ΤΕΜΑΧΙΑ
                except AttributeError:
                    pass
            elif 'epson' in str(obj.Μηχάνημα).lower():
                try:
                    pieces = EPSON.objects.filter(ΚΩΔΙΚΟΣ=f"{obj.ml_code}").first()
                    obj.pieces = pieces.ΤΕΜΑΧΙΑ
                except AttributeError:
                    pass
            elif 'kyocera' in str(obj.Μηχάνημα).lower():
                try:
                    pieces = KYOCERA.objects.filter(ΚΩΔΙΚΟΣ=f"{obj.ml_code}").first()
                    obj.pieces = pieces.ΤΕΜΑΧΙΑ
                except AttributeError:
                    pass
            elif 'oki' in str(obj.Μηχάνημα).lower():
                try:
                    pieces = OKI.objects.filter(ΚΩΔΙΚΟΣ=f"{obj.ml_code}").first()
                    obj.pieces = pieces.ΤΕΜΑΧΙΑ
                except AttributeError:
                    pass
            elif 'canon' in str(obj.Μηχάνημα).lower():
                try:
                    pieces = CANON.objects.filter(ΚΩΔΙΚΟΣ=f"{obj.ml_code}").first()
                    obj.pieces = pieces.ΤΕΜΑΧΙΑ
                except AttributeError:
                    pass
            elif 'brother' in str(obj.Μηχάνημα).lower():
                try:
                    pieces = BROTHER.objects.filter(ΚΩΔΙΚΟΣ=f"{obj.ml_code}").first()
                    obj.pieces = pieces.ΤΕΜΑΧΙΑ
                except AttributeError:
                    pass
            elif 'lexmark' in str(obj.Μηχάνημα).lower():
                try:
                    pieces = LEXMARK.objects.filter(ΚΩΔΙΚΟΣ=f"{obj.ml_code}").first()
                    obj.pieces = pieces.ΤΕΜΑΧΙΑ
                except AttributeError:
                    pass
        return context

