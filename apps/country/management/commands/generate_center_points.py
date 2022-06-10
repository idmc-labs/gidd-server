from django.core.management.base import BaseCommand
from apps.country.models import Country
from shapely import geometry


class Command(BaseCommand):
    help = 'Generate center points of country'

    def handle(self, *args, **options):
        countries = Country.objects.all()
        for country in countries:
            box = country.bounding_box
            if box:
                # [-179.999989, -18.28799, 179.999989, -16.020882]
                p1 = geometry.Point(box[0], box[1])
                p2 = geometry.Point(box[2], box[3])
                p3 = geometry.Point(box[0], box[3])
                p4 = geometry.Point(box[2], box[1])

                pointList = [p1, p2, p3, p4]
                poly = geometry.Polygon([i for i in pointList])
                center_point = list(geometry.mapping(poly.centroid)['coordinates'])
                country.center_point = center_point
                country.save()
        print('Updated center points')
