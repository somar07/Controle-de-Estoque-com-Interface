
class Vendas():

    def __init__(self, lista_produtos):
        self._lista_produtos = lista_produtos
        self._total = 0
      

    @property
    def lista_produtos(self):
        return self._total
    
    @lista_produtos.setter
    def lista_produtos(self, lista_produtos):
        self._lista_produtos = lista_produtos

    @property
    def total(self):
	    return self._total
    
    @total.setter
    def total(self, total):
	    self._total = total
    
    def add_produto(self, produto, qtd):

        if(produto.quantidade >= qtd):
            
            self.total += (qtd * produto.valor)
        
            
            return True
        
        else:
            return False
