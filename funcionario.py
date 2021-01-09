
from pessoa import Pessoa

class Funcionario(Pessoa):

	_qtd_func = 0 # verificar quantidade de obj criados 
	
	def __init__(self):
		super().__init__()
		self._salario = 0
		Funcionario._qtd_func += 1

	@staticmethod
	def get_qtd_func():
		return Funcionario._qtd_func
	
	@property
	def salario(self):
		return self._salario

	@salario.setter
	def salario(self, salario):
		
		if(salario >= 0):
			self._salario = salario
		else:
			print("Salario Invalido\n")