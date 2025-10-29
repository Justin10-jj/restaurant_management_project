from django.test import TestCase

# Create your tests here.
class RestaurantInfoAPITest(APITestCase):
    def setUp(self):
        self.restaurant=Restaurant.objects.create(
            name='Test Restaurant',
            address='123 Tset st'
        )
    def test_get_restaurant_info(self):
        response=self.client.get('/api/restaurant-info/')
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertIn('name',response.data[0])
        self.assertIn('address',response.data[0])