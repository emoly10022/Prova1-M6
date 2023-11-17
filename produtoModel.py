from databaseController import DatabaseController

class ProdutoFinanceiroModel:
    def calcular_valor_projetado(self, id_usuario, id_produto):
        database_controller = DatabaseController()
        info_usuario = database_controller.obter_informacoes_usuario(id_usuario)
        info_produto = database_controller.obter_informacoes_produto(id_produto)
        valor_projetado = self.calculo_customizado(info_usuario, info_produto)

        return valor_projetado

    def calculo_customizado(self, info_usuario, info_produto):
        pass
