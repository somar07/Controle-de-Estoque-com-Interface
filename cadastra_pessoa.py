
# cadastra cliente
class Pessoa:

	'''
	class Pessoa()
	---------------
	Responsavel por receber as informações das pessoas que
	serão cadastradas no sistema como, funcionários e clientes.
	
	Atributos
	-----------
	nome -> string
	cpf -> string
	
	'''
	
	__slots__ = ['_condicao','_nome', '_cpf'] 
	
	def __init__(self, nome, cpf):
		self._condicao = None
		self._nome = nome		
		self._cpf = cpf

	@property
	def condicao(self):
		return self._condicao

	@condicao.setter
	def condicao(self,condicao):
		self._condicao = condicao
			
		
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

	__slots__ = ['_condicao','_nome', '_cpf', '_salario'] 
		
	def __init__(self, condicao, nome, cpf, salario):
		super().__init__(nome, cpf)
		self._condicao = condicao
		self._salario = salario
		

	@property
	def condicao(self):
		return self._condicao

	@property
	def salario(self):
		return self._salario


	@salario.setter
	def salario(self, salario):
		self._salario = salario
	

# cadastra cliente
class Cadastra_pessoa(object):

	'''
	class Cadastra_pessoa()
	-------------------------
	Responsavel pelo cadastro de pessoas no sistema.

	Atributos
	----------
	lista_pessoas -> list

	funções
	-------
	cadastra
	busca

	'''

	__slots__ = ['_lista_pessoas']

	def __init__(self):
		self._lista_pessoas = []

	@property
	def lista_pessoas(self):
		return self._lista_pessoas
	

	def cadastra(self, pessoa):
		'''
		Funcao cadastra
		---------------
		Adiciona pessoas cadastradas a uma lista, se a pessoa
		já estiver na lista a função retorna false e o cadastro não é
		realizado.

		Paramentros
		------------
		pessoa -> Pessoa
		
		'''
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
	'''
	class Cadastra_funcionario()
	Realiza o cadastro dos funcionários em lista diferente das dos clientes.
	'''

	def __init__(self):
		super().__init__()

