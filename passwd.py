#!/usr/bin/python
fich=open('/etc/passwd','r')
lines=fich.readlines()
fich.close();

for line in lines[:-1]: #Dejo fuera la ultima linea porque split me deja un \n al final
	slot=line.split(':')
	print slot[0] + ':' + slot[-1][:-1]

print "\nEn total hay " + str(len(lines)) + " usuarios"
