class Cadastra_produto(object):

	__slots__ = ['_lista_produtos']

	def __init__(self):
		self._lista_produtos = []

	@property
	def lista_produtos(self):
		return self._lista_produtos
	

	def cadastra(self, produto):
		existe = self.busca(produto.cpf)
		if(existe == None):
			self._lista_produtos.append(produto)
			return True
		
		else:
			return False

	def busca(self, codigo):
		for produto in self._lista_produtos:
			if(produto.codigo == codigo):
				return produto

		return None