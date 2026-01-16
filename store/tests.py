from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from .models import Category, Product, Order


class CategoryProductModelTest(TestCase):
    def test_create_category_and_product(self):
        category = Category.objects.create(name="Livros")

        product = Product.objects.create(
            name="Harry Potter",
            price=59.90,
            category=category
        )

        self.assertEqual(Category.objects.count(), 1)
        self.assertEqual(Product.objects.count(), 1)
        self.assertEqual(product.category.name, "Livros")


class OrderModelTest(TestCase):
    def test_create_order(self):
        order = Order.objects.create()

        self.assertIsNotNone(order.id)
        self.assertEqual(Order.objects.count(), 1)
