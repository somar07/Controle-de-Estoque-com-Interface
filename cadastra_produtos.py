class Produto:
	
	def __init__(self):
		self._codigo = 0
		self._nome = None
		self._valor = 0
		self._quantidade = 0


	@property
	def codigo(self):
		return self._codigo

	@property
	def nome(self):
		return self._nome

	@property
	def valor(self):
		return self._valor

	@valor.setter
	def valor(self, valor):
		if(valor >= 0):
			self._valor = valor
		
		else:
			print("Valor invalido\n")


	@property
	def quantidade(self):
		return self._quantidade

	
	@quantidade.setter
	def quantidade(self, quantidade):
		self._quantidade = quantidade



class Cadastra_produto(object):

	__slots__ = ['_lista_produtos']

	def __init__(self):
		self._lista_produtos = []

	@property
	def lista_produtos(self):
		return self._lista_produtos
	

	def cadastra(self, produto):
		existe = self.busca(produto.codigo)
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