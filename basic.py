# -*- coding: utf-8 -*-

a = 'Fizz'
print('a = %s' % a)

b = 'Buzz'
print('b = %s' % b)

a, b = b, a
print('a = %s, b = %s' % (a, b))

from random import randint

while randint(1, 10) != 5:
	print('Errou!')

print('Acertô mizeravi!')

arr = [0, '1', 'teste', 3.55, 42, 'bla'*3]

for i in [0, '1', 'teste', 3.55, 42, 'bla'*3]:
	print(i)

# forEach
for k, v in enumerate(arr):
	print('key: %d, value: %s' % (k, str(v)))

music = 'As luzes estão piscando, o jukebox tocando Amado Batista e o pau tá quebrando ...'
print(music)
# n <= text < m
print(music[:15])
print(music[15:30])

arr_music = music.split()
print(arr_music)

print('|'.join(arr_music))