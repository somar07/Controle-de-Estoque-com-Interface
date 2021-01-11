class Vendas():

    def __init__(self, lista_produtos):
        self._lista_produtos = lista_produtos
        self._lista_vendas = []
      

    @property
    def lista_produtos(self):
        return self._lista_vendas
    
    @lista_produtos.setter
    def lista_produtos(self, lista_produtos):
        self._lista_produtos = lista_produtos

    @property
    def lista_vendas(self):
	    return self._lista_vendas
    
    @lista_vendas.setter
    def lista_vendas(self, lista_vendas):
	    self._lista_vendas = lista_vendas
    
    def add_produto(self, produto, qtd):

        if(produto.quantidade >= qtd):
            # atualiza a lista cadastra produdo

            aux_prod = produto
            
            existe = self.busca(aux_prod.codigo)

            if(existe !=  None):
                indice = self.lista_vendas.index(existe)
                self.lista_vendas[indice].quantidade += qtd
                self.updateListProd(produto, qtd)              
           
            else:
                aux_prod.quantidade = qtd
                self.lista_vendas.append(aux_prod)
                self.updateListProd(produto, qtd)
            return True
        
        else:
            return False

    def busca(self, codigo):
        for prod in self.lista_vendas:
            if(prod.codigo == codigo):
                return prod
        
        return None
   
    def updateListProd(self, produto, qtd):
        indice = self.lista_produtos.index(produto)

        self.lista_produtos[indice].quantidade -= qtd

