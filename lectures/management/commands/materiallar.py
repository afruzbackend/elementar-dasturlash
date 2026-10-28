"""Asosiy darslikka qo'shimcha materiallarni qo'shadi (ro'yxat: lectures/fan.py, fayllar: data/materiallar/).

    python manage.py materiallar

Borlari (bir xil havola yoki fayl nomi) takrorlanmaydi.
"""
from django.conf import settings
from django.core.files import File
from django.core.management.base import BaseCommand, CommandError

from lectures import fan
from lectures.models import Course, Resource

FILES = settings.BASE_DIR / 'data' / 'materiallar'


class Command(BaseCommand):
    help = "Asosiy darslikka qo'shimcha materiallarni (havola va fayllar) qo'shadi (lectures/fan.py)."

    def handle(self, *args, **opts):
        course = Course.objects.get(slug=fan.SLUG)
        materials = Resource.objects.filter(course=course, kind='material')
        added = skipped = 0
        for n, title, src, note in fan.MATERIALS:
            topic = course.topics.get(number=n) if n else None
            is_url = src.startswith(('http://', 'https://'))
            exists = (materials.filter(url=src) if is_url else materials.filter(file__endswith=src)).exists()
            if exists:
                skipped += 1
                continue
            res = Resource(course=course, topic=topic, kind='material', title=title, note=note)
            if is_url:
                res.url = src
                res.save()
            else:
                path = FILES / src
                if not path.exists():
                    raise CommandError(f'Fayl topilmadi: {path}')
                with open(path, 'rb') as fh:
                    res.file.save(path.name, File(fh, name=path.name), save=True)
            added += 1
        self.stdout.write(self.style.SUCCESS(
            f'Jami {len(fan.MATERIALS)} ta material: qo‘shildi {added}, oldin bor edi {skipped}.'))
