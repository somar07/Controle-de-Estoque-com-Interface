class Produto:
	'''
	class Produto()
	---------------
	Classe responsável por receber os dados dos produtos que serão cadastrados no sistema.

	Atributos
	----------
	codigo -> string
	nome -> string
	valor -> float
	quantidade -> int
	
	'''
	__slots__ = ['_condicao','_codigo', '_nome', '_valor', '_quantidade']
	
	def __init__(self, condicao, codigo, nome, valor, quantidade):
		self._condicao = condicao
		self._codigo = codigo
		self._nome = nome
		self._valor = valor
		self._quantidade = quantidade

	@property
	def condicao(self):
		return self._condicao
	
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

	'''
	class Cadastra_produto()
	-------------------------
	Responsavel por cadastrar os produtos no sistema.

	Atributos
	----------
	lista_produtos -> list

	funcoes
	-------
	cadastra
	busca
	rm_prod_zerado

	'''

	__slots__ = ['_lista_produtos']

	def __init__(self):
		self._lista_produtos = []

	@property
	def lista_produtos(self):
		return self._lista_produtos
	

	def cadastra(self, produto):
		'''
		funcao cadastra
		----------------
		Adiona os produtos cadastrados na lista_produtos,
		desde que nao tenha codigo repetido.

		Paramentros
		------------
		produto -> Produto

		'''
		existe = self.busca(produto.codigo)
		if(existe == None):
			self._lista_produtos.append(produto)
			return True
		
		else:
			return False

	def busca(self, codigo):
		'''
		Funcao busca
		-------------
		Responsavel por localizar um produto desejado, por meio do codigo.

		Paramentros
		-----------
		codigo -> Produto
		'''
		for produto in self._lista_produtos:
			if(produto.codigo == codigo):
				return produto

		return None

	def rm_prod_zerado(self):
		'''
		Funcao rm_prod_zerado
		---------------------
		Remove produtos que estejam com a quantidade zerada.
		'''
		for produto in self._lista_produtos:
			if(produto.quantidade == 0):
				self._lista_produtos.remove(produto)
