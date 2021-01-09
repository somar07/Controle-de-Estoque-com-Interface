class Pessoa: 
	
	__slots__ = ['_nome', '_cpf', '_endereco', '_data_nasc' ] 
	
	def __init__(self, nome, cpf, endereco, data_nasc):
		
		self._nome = nome		
		self._cpf = cpf		
		self._endereco = endereco		
		self._data_nasc = data_nasc

	@property
	def nome(self):
		return self._nome

	@nome.setter
	def nome(self, nome):
		self._nome = nome

	@property
	def cpf(self):
		return self._cpf
	
	
	@property
	def endereco(self):
		return self._endereco

	@endereco.setter
	def endereco(self, endereco):
		self._endereco = endereco

	@property
	def data_nasc(self):
		return self._data_nasc


class Funcionario(Pessoa):

	__slots__ = ['_nome', '_cpf', '_endereco', '_data_nasc', '_salario'] 
		
	def __init__(self, nome, cpf, endereco, data_nasc, salario):
		super().__init__(nome, cpf, endereco, data_nasc)
		self._salario = salario

