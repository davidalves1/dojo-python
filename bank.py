class Client:
	def __init__(self, name, age):
		self.name = name
		self.age = age

class Account:
	def __init__(self, clients, number, balance = 0):
		self.clients = clients
		self.number = number
		self.balance = balance
		self.operations = []

	def summary(self):
		print("CC: %s | Saldo: R$%10.2f" % (self.number, self.balance))

	def take_money(self, value):
		if self.balance >= value:
			self.balance -= value
			self.operations.append(['Saque', value])
		else:
			print("Valor indisponivel para saque")

	def deposit_money(self, value):
		self.balance += value
		self.operations.append(['Deposito', value])

	def extract(self):
		print('Extrato da CC: %s' % self.number)
		
		for op in self.operations:
			print("%s: R$%10.2f" % (op[0], op[1]))
		
		print("Saldo: R$%10.2f" % self.balance)

