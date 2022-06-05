import csv  # https://docs.python.org/3/library/csv.html
import pandas as pd 

# https://django-extensions.readthedocs.io/en/latest/runscript.html

# python3 manage.py runscript many_load

from unesco.models import Category, States, Region, Iso, Site


def run():
    csv_path = 'unesco/whc-sites-2018-clean.csv'
    df = pd.read_csv(csv_path)

    Category.objects.all().delete()
    States.objects.all().delete()
    Region.objects.all().delete()
    Iso.objects.all().delete()
    Site.objects.all().delete()

    for index, row in df.iterrows():
        site = {
            'name': row['name'],
            'description': row['description'],
            'justification': row['justification'],
            'year': row['year'],
            'longitude': row['longitude'],
            'latitude': row['latitude'],
            'area_hectares': row['area_hectares'],
            'category': Category.objects.get_or_create(name=row['category'])[0],
            'states': States.objects.get_or_create(name=row['states'])[0],
            'region': Region.objects.get_or_create(name=row['region'])[0],
            'iso': Iso.objects.get_or_create(name=row['iso'])[0],
        }
        site = Site(**site)
        site.save()
