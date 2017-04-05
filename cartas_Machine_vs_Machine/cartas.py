# coding: utf-8

from random import randint

aleatori1=randint(1,13)
aleatori2=randint(1,13)

if aleatori1>10 :
	if aleatori1==11:
		print "máquina1 juega con : J"

	if aleatori1==12:
		print "máquina1 juega con : Q"
	
	if aleatori1==13:
		print "máquina1 juega con : K"
else:
	print "máquina1 juega con : ", aleatori1

if aleatori2>10 :
	if aleatori2==11:
		print "máquina2 juega con : J"

	if aleatori2==12:
		print "máquina2 juega con : Q"
	
	if aleatori2==13:
		print "máquina2 juega con : K"

else:
	print "máquina2 juega con : ", aleatori2

if aleatori1==aleatori2 :
		print "Empate"
else:
	if aleatori1>aleatori2 :
		print "Gana máquina1"
	else:
		print "Gana máquina2"
