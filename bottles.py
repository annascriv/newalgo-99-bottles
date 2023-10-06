def bottle_song(num):
	#num = 99
	song = ''
	while num>0:
		song+=f'''{num} bottles of beer on the wall, {num} bottles of beer. Take one down and pass it around, {num-1} bottles of beer on the wall.'''
		num=num-1

		if num == 2:
			song+=f'''{num} bottles of beer on the wall, {num} bottles of beer. Take one down and pass it around, {num-1} bottle of beer on the wall.'''
			num=num-1
		elif num == 1:
			song+=f'''{num} bottle of beer on the wall, {num} bottle of beer. Take it down and pass it around, no bottles of beer on the wall. No more bottles of beer on the wall, no more bottles of beer. Go to the store and buy some more, no bottles of beer on the wall.'''
	
	return song

print(bottle_song(6))
