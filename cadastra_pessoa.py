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