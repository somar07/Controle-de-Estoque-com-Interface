class Produto:
	
	def __init__(self):
		self._codigo = 0
		self._nome = None
		self._valor = 0
		self._quantidade = 0


	@property
	def codigo(self):
		return self._codigo

	@codigo.setter
	def codigo(self, codigo):
		self._codigo = codigo


	@property
	def nome(self):
		return self._nome

	@nome.setter
	def nome(self, nome):
		self._nome = nome

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