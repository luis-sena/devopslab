# -*- coding: utf-8 -*-
from app import app
import unittest

class Test(unittest.TestCase):
    def setUp(self):
        # cria uma instância do unittest, precisa do nome "setUp"
        self.app = app.test_client()

        # envia uma requisicao GET para a URL
        self.result = self.app.get('/')

        # envia uma requisicao GET para a URL
        self.result_soma = self.app.get('/soma?num1=10&num2=10')

    def test_requisicao(self):
        # compara o status da requisicao (precisa ser igual a 200)
        self.assertEqual(self.result.status_code, 200)

    def test_conteudo(self):
        # verifica o retorno do conteudo da pagina
        self.assertEqual(self.result.data.decode('utf-8'), "Hello World")

    def test_soma(self):
        # verifica o retorno da soma de 10 + 10 = 20
        self.assertEqual(self.result_soma.data.decode('utf-8'), "Sua soma de 10+10=20")
