'''BASIC XS
print:print
let:set var
'''
import os
print()

def reconize(t):
	#a function to reconize types:
	#	string
	#	int
	#	func(func return)
	ty=None
	if t[0]=='\'' or t[len(t)-1]=='\'':
		ty='str'
	else:
		try:
			int(t)
			ty='int'
		except ValueError:
			ty=t[0]
		
	return ty
	
def pront(s):
	#special print
	if s!=None:
		print(s)

def do(n):
	if type(n)==int:
		return n
	else:
		return n[0]
		
def sort_dict(d):
	l=[]
	for i in d:
		l.append(i)
	l.sort()
	r={}
	for i in l:
		r[i]=d[i]
	return r
	
def plus(n):
	for i in range(len(n)):
		n[i]=int(n[i])
	return sum(n)

def exe(n):
	run(SEQC[int(do(n))])
	if SEQC[int(do(n))].split(' ')[0]=='goto':
		return SEQC[int(do(n))].split(' ')[1]
	else:
		return 'False'
	
def lst():
	for i in SEQC:
		ro=str(i)+' '
		for e in SEQC[i]:
			ro+=e+' '
		print(ro)
		
def prnt(s):
	ro=''
	for i in s:
		ro+=i+' '
	print(ro)
	
def rn():
	i=0
	error=False
	while not error:
		try:
			e=exe(i)
			if e!='False':
				i=(int(e)-1)
			i+=1
		except KeyError:
			l=[]
			for i in SEQC:
				l.append(i)
			if i>max(l):
				error=True
			else:
				i+=1
				
def let(n):
	VARS[n[0]]=n[1]

def goto(n):
	pass

CMDS={'prnt':prnt, 'exec':exe, 'list':lst, 'plus':plus, 'run':rn, 'goto':goto, 'let':let}
SEQC={}
VARS={}

def run(cmd):
	#run a command by the CMDS dictionary
	cmd=cmd.split(' ')
	try:
		return CMDS[cmd[0]](cmd[1:len(cmd)])
	except IndexError:
		return CMDS[cmd[0]]()
	except TypeError:
		return CMDS[cmd[0]]()
		
while True:
	#main loop
	e=input('>>')
	r=e.split(' ')
	try:
		kaka=''
		for i in r[1:len(r)]:
			kaka+=i+' '
		SEQC[int(r[0])]=kaka
		SEQC=sort_dict(SEQC)
	except ValueError:
		pront(run(e))
	except IndexError:
		pront(run(e))
