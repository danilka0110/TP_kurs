from django.test import TestCase
from .models import Localities

class LocalitiesTestCase(TestCase):
    def setUp(self):
        self.Localities = Localities.objects.create(title="Краснодар", leader="Евгений Алексеевич Первышов", number_of_inhabitants="974319", budget="47360000000", spending="50230000000", deficit="123", img_link="https://sdelanounas.ru/i/a/w/1/f_aW1nLmdlbGlvcGhvdG8uY29tL2tyc25kci8wM19rcnNuZHIuanBnP19faWQ9MTQzNTc5.jpeg")
        self.Localities.save()

    def tearDown(self):
        self.Localities.delete()

    def test_update_localities_description(self):
        self.Localities.title = 'цфыы'
        self.Localities.save()
        self.assertEqual(self.Localities.description, 'цфыы')
