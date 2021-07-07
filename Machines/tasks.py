from celery import shared_task
from celery_progress.backend import ProgressRecorder
from datetime import datetime
import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
from requests_html import HTML
from django.conf import settings
import yaml
from yaml import CLoader as Loader
import traceback
from .models import Machines
from Spareparts.models import SpareParts
"""
ITALIA
"""

with open(settings.CREDENTIALS, "r", encoding='utf8') as cred:
    cred_obj = yaml.load(cred, Loader=Loader)

ital_login_url = cred_obj["ital_login_url"]["url"]
ital_payload = cred_obj['ital_payload']
info_login_url = cred_obj["info_login_url"]["url"]
info_payload = cred_obj['info_payload']

session = requests.Session()
# headers = {"User-Agent": "Mozilla/5.0 (X11; CrOS x86_64 12871.102.0) AppleWebKit/537.36 (KHTML, like Gecko) "
#                          "Chrome/81.0.4044.141 Safari/537.36"}
retry = Retry(connect=3)
adapter = HTTPAdapter(max_retries=retry)
session.mount('http://', adapter)
session.mount('https://', adapter)
response = session.post(ital_login_url, data=ital_payload)
info_response = session.post(info_login_url, data=info_payload)


@shared_task(bind=True)
def get_ital_price(self, machine_id):
    machine = Machines.objects.get(pk=machine_id)
    spare_parts = SpareParts.objects.filter(Μηχάνημα=machine)
    progress_recorder = ProgressRecorder(self)
    for i, spare_part in enumerate(spare_parts):
        if spare_part.ital_code is None or spare_part.ital_code == 0 or spare_part.ital_code == "0":
            continue
        try:

            ital_requests_url = f'https://www.itrip.it/default.php?t=ecomm&act=personal&search=1&codice={spare_part.ital_code}'
            with session.get(ital_requests_url) as ital_html:
                ital_html_data = ital_html.text
                ital_data = HTML(html=ital_html_data)
                ital_price = ital_data.find(".col5")
                spare_part.ital_price = str(ital_price[0].text).replace(",", ".") + " €"
                spare_part.save()
                print(f"{spare_part} Italia Price Saved")
            progress_recorder.set_progress(i + 1, len(spare_parts), f'{spare_part.description} Τιμή Ιταλίας {ital_price[0].text} € Αποθηκεύτηκε')
        except Exception:
            print(traceback.print_exc())
            continue
    machine.prices_date = datetime.today().strftime("%d/%m/%Y")
    machine.save()
    return 'Η διαδικασία ολοκληρώθηκε'


@shared_task(bind=True)
def get_info_price(self, machine_id):
    machine = Machines.objects.get(pk=machine_id)
    spare_parts = SpareParts.objects.filter(Μηχάνημα=machine)
    progress_recorder = ProgressRecorder(self)
    for i, spare_part in enumerate(spare_parts):
        if spare_part.info_site_code is None or spare_part.info_site_code == 0 or spare_part.info_site_code == "0":
            continue
        try:
            info_requests_url = f'http://www.infocopy.gr/index.php?com=products1&id={spare_part.info_site_code}'
            with session.get(info_requests_url) as info_html:
                info_html_data = info_html.text
                info_data = HTML(html=info_html_data)
                info_price = info_data.find(".m_nb")
                clean_info_price = info_price[1].text[-8:].splitlines()
                spare_part.info_price = clean_info_price[-1]
                spare_part.save()
                print(f"{spare_part} Info-Copy Price Saved")
            progress_recorder.set_progress(i + 1, len(spare_parts), f'{spare_part.description} Τιμή Info-Copy {clean_info_price[-1]} Αποθηκεύτηκε')
        except Exception:
            print(traceback.print_exc())
            continue
    machine.prices_date = datetime.today().strftime("%d/%m/%Y")
    machine.save()
    return 'Η διαδικασία ολοκληρώθηκε'