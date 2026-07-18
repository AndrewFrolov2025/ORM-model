import csv
from datetime import datetime

from django.core.management.base import BaseCommand
from django.utils.text import slugify

from phones.models import Phone

class Command(BaseCommand):
    help = 'Import phones from csv file'

    def handle(self, *args, **options):
        file_path = 'phones.csv'

        with open(file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=';')

            for row in reader:
                phone_id = int(row['id'])
                name = row['name']
                price = int(row['price'])
                image = row['image']

                release_date = datetime.strptime(
                    row['release_date'],
                    '%Y-%m-%d'
                ).date()

                lte_exists = row['lte_exists'].lower() in [
                    'true',
                    '1',
                    'yes',
                    'да'
                ]

                Phone.objects.update_or_create(
                    id=phone_id,
                    defaults={
                        'name': name,
                        'price': price,
                        'image': image,
                        'release_date': release_date,
                        'lte_exists': lte_exists,
                        'slug': slugify(name),
                    }
                )

        self.stdout.write(
            self.style.SUCCESS('Phones successfully imported')
        )