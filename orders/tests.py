from django.test import TestCase

# Create your tests here.
class OrderModeltests(TestCase):
    def test_calculated_total(self):
        burger=MenuItem.objects.create(name="Burger",price=Decimal("5.00"))
        fries=MenuItem.objects.create(name="Fries",price=Decimal("2.50"))
        order=Order.objects.create(customer_name="john Deo")
        OrderItem.objects.create(order=order,menu_item=burger,quantity=2,price=burger.price)
        OrderItem.objects.create(order=order,menu_item=fries,quantity=3,price=fries.price)
        self.assertEqual(order.calculate_total(),Decimal("17.50"))



class CancelOrderAPITests(APITestCase):
    def setup(self):
        self.user=User.objects.create_user(username="testuser",password="password123")
        self.client.login(username="testuser",password="pass1234")
        self.oredr=Order.objects.create(customer_name="test user")

    def test_cancel_oredr_success(self):
        response=self.client.delete(f"/oredrs/{self.oredr.id}/cancel/")
        self.oredr.refresh_from_db()
        self.asserEqual(response.status_code,status.HTTP_200_OK)
        self.asserEqual(self.order.status,"CANCELLED")

    def test_cancel_order_already_cancelled(self):
        self.order.status='CANCELLED'
        self.order.save()
        response=self.client.delete("f/order/{self.order.id}/cancel/")



class OrderTotalTest(TestCase):
    def setUp(self):
        self.user=User.objects.craete(username="testuser")
    def test_oredr_with_items_and_discount(self):
        oredr=Order.objects.create(customer=self.user,customer_name="Test User")
        orderitem.objects.create(order=order,menu_item="pizza",price=Decimal("10.00"),quantity=2)
        Orderitem.objects.create(order=order,menu_item="pasta",price=Decimal("5.00"),quantity=1,discount_percent=10)

        self.asserEqual(order.calculate_total(),Deimal("23.50"))