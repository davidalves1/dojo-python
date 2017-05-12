# -*- coding: utf-8 -*-

#import bank
from bank import Client
from bank import Account

pedro = Client('Pedro', 30)
maria = Client('Maria da Penha', 22)
marcos = Client('Marcos', 26)

print("---- Clientes ----\n")

for client in [pedro, maria, marcos]:
	print("Nome: %s | Idade: %s" % (client.name, client.age))

acc1 = Account([pedro], 1, 1500)
acc2 = Account([marcos, maria], 2, 2400)

print('\n---- Saldo inicial ----\n')
acc1.summary()
acc2.summary()

print('\n---- Movimentação ----\n')
acc1.take_money(120)
acc1.take_money(25)
acc2.deposit_money(300)
acc2.take_money(1000)
acc2.take_money(1500)
acc2.take_money(1500)

print('\n---- Extratos ----')
acc1.extract()
acc2.extract()