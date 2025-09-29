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