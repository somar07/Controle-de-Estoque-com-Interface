import copy

class Vendas():

    def __init__(self, lista_produtos ):
        self._lista_produtos = lista_produtos
        self._lista_compras = []
        self._total = 0
      

    @property
    def lista_produtos(self):
        return self._total
    
    @lista_produtos.setter
    def lista_produtos(self, lista_produtos):
        self._lista_produtos = lista_produtos

    @property
    def lista_compras(self):
	    return self._lista_compras
    
    @lista_compras.setter
    def lista_compras(self, _lista_compras):
	    self._lista_compras = lista_compras

    @property
    def total(self):
	    return self._total
    
    @total.setter
    def total(self, total):
	    self._total = total
    
    def add_produto(self, produto, qtd):

        if(produto.quantidade >= qtd):

            prod_aux = copy.deepcopy(produto)

            existe = self.busca_compras(prod_aux.codigo)

            if(existe != None):
                indice = self.lista_compras.index(existe)
                self.lista_compras[indice].quantidade += qtd
            
            else:
                prod_aux.quantidade = qtd
                self.lista_compras.append(prod_aux)

            produto.quantidade -= qtd
           
            self.total += qtd * prod_aux.valor
        
            
            return True
        
        else:
            return False    

    def busca_compras(self, codigo):

        for prod in self.lista_compras:
            if(prod.codigo == codigo):
                return prod
        else:
            return None

