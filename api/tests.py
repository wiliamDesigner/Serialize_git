from django.test import TestCase

# Create your tests here.
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Produto


class ProdutoTests(APITestCase):

    def test_listar_produtos(self):
    

        Produto.objects.create(nome="Teclado", preco=100.00)
        Produto.objects.create(nome="Mouse", preco=50.00)

     
        response = self.client.get("/api/produtos/")

    
        self.assertEqual(response.status_code, status.HTTP_200_OK)

       
        self.assertEqual(len(response.data), 2)

    def test_criar_produto(self):
        """
        Esse teste garante que o endpoint POST /api/produtos/
        cria um produto no banco e retorna status 201.
        """

        data = {
            "nome": "Monitor",
            "preco": "900.00"
        }

        response = self.client.post("/api/produtos/", data, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

       
        self.assertEqual(Produto.objects.count(), 1)

        self.assertEqual(Produto.objects.first().nome, "Monitor")
