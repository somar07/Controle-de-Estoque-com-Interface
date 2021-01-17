import copy
from cadastra_produtos import Cadastra_produto


class Vendas():

    '''
    class Vendas(), realiza dos vendas de produtos

    Parametros
    ----------
    lista_produtos -> Produto()

    Atributos 
    ---------
    lista_produtos -> Produto()
    lista_compras -> Produto()
    total -> float


    Funções
    -------
    add_produto
    busca_compras

    '''

    def __init__(self, lista_produtos ):
        self._lista_produtos = lista_produtos
        self._lista_compras = []
        self._total = 0
        self.add = Cadastra_produto()
      

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
	    self._lista_compras = _lista_compras

    @property
    def total(self):
	    return self._total
    
    @total.setter
    def total(self, total):
	    self._total = total
    
    def add_produto(self, produto, qtd):

        '''
        Função add_produto
        ------------------ 
        adiciona um produto na lista de compra de acordo com quantidade informada

        Parametros
        ----------
        produto -> Produto
        qtd -> int
        '''

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

        '''
        Função  busca_compras
        ----------------------
        Buca por um produto na lista_compras,

        Parametros
        ----------
        codigo -> str

        return
        None 
        produto()
       
        '''

        for prod in self.lista_compras:
            if(prod.codigo == codigo):
                return prod
        else:
            return None