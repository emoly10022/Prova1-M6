from produtoModel import ProdutoFinanceiroModel
from taxaFinanceiraAPI import TaxaFinanceiraAPI  

class APIController:
    def calcular_valor_projetado(self, usuario, id_produto):
        produto_model = ProdutoFinanceiroModel()
        valor_projetado = produto_model.calcular_valor_projetado(id_usuario, id_produto)
        return valor_projetado
