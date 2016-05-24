import sys
import textwrap

max_len = 28
src = ''
right = ''
left = ''
out = ''

if len(sys.argv) > 1:
    for arg in sys.argv[1:]:
        src +=arg + " "
else:
	print("Enter a text. Use <text> to make 3d\n")
	src = sys.stdin.readline()


#TODO adjust length of the text
wrappedList = textwrap.wrap(src, max_len)
lineCnt = max (len(x) for x in wrappedList)

#fill with remaining spaces
aux = []
for w in wrappedList:
	aux.append( w.ljust(lineCnt))

wrapped = '\n'.join(aux)
#print (wrapped + '\n\n\n')


#replace < > symobls
left = wrapped
right = wrapped
left = left.replace('<', ' ')
left = left.replace('>', '')

right = right.replace('<', '')
right = right.replace('>', ' ')


#concat the individual lines line of 28 + 2 sides
lLines = left.split('\n')
rLines = right.split('\n')

#TODO adjust length on left side.
for i in range( len(lLines)):
	out += '* ' + lLines[i][:lineCnt-1] + ' * ' + rLines[i][:lineCnt-1] +' *\n'

print ('\n\n' +out)

