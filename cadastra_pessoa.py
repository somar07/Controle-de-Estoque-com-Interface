
# cadastra cliente
class Pessoa:

	'''
	class Pessoa()
	---------------
	Responsavel por conter as informações das pessoas que
	serão cadastradas no sistema como, funcionários e clientes.
	
	Paramentros
	-----------
	nome -> string
	cpf -> string
	
	'''
	
	__slots__ = ['_nome', '_cpf'] 
	
	def __init__(self, nome, cpf):
		
		self._nome = nome		
		self._cpf = cpf		
		
	@property
	def nome(self):
		return self._nome

	@property
	def cpf(self):
		return self._cpf
	

class Funcionario(Pessoa):

	'''
	class Funcionario()
	-------------------
	Responsavel por receber os dados dos funciários que serão
	cadastrados no sistema.

	Paramentros
	-----------
	Pessoa -> Pessoa()
	nome -> Pessoa()
	cpf -> Pessoa()

	Atributos
	----------
	salario -> float
	
	'''

	__slots__ = ['_nome', '_cpf', '_salario'] 
		
	def __init__(self, nome, cpf, salario):
		super().__init__(nome, cpf)
		self._salario = salario

	@property
	def salario(self):
		return self._salario


	@salario.setter
	def salario(self, salario):
		self._salario = salario
	

# cadastra cliente
class Cadastra_pessoa(object):

	__slots__ = ['_lista_pessoas']

	def __init__(self):
		self._lista_pessoas = []

	@property
	def lista_pessoas(self):
		return self._lista_pessoas
	

	def cadastra(self, pessoa):
		existe = self.busca(pessoa.cpf)
		if(existe == None):
			self._lista_pessoas.append(pessoa)
			return True
		
		else:
			return False

	def busca(self, cpf):
		for pessoa in self._lista_pessoas:
			if(pessoa.cpf == cpf):
				return pessoa

		return None

class Cadastra_funcionario(Cadastra_pessoa):

	def __init__(self):
		super().__init__()

