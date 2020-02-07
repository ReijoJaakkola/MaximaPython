import RunMaxima

counter = 1

vocabulary = []
freevariables = []
assumptions = []
deduction = []

line = str(input('Enter vocabulary: '))
vocabulary = line.split()
for symbol in vocabulary:
	line = str(input(f'Enter the free variables of {symbol}: '))
	freevariables.append(line.split())
freevariablesForMaxima = '['
for i in range(len(vocabulary)):
	if i > 0:
		freevariablesForMaxima += ','
	text = '["' + vocabulary[i] + '",{'
	for j in range(len(freevariables[i])):
		if j > 0:
			text += ','
		text += '"' + freevariables[i][j] + '"'
	text += '}]'
	freevariablesForMaxima += text
freevariablesForMaxima += ']'
print(freevariablesForMaxima)

line = str(input('Enter assumptions: '))
assumptions = line.split()

assumptionsForMaxima = '['
for i in range(len(assumptions)):
	if i > 0:
		assumptionsForMaxima += ','
	assumptionsForMaxima += '"' + assumptions[i].replace(' ','') + '"'
assumptionsForMaxima += ']'

while True:
	line = str(input(f'{counter}: '))
	if line == "QED":
		break
	deduction.append(line)
	counter += 1
print()

deductionForMaxima = '['
for i in range(len(deduction)):
	if i > 0:
		deductionForMaxima += ','
	deductionForMaxima += '"' + deduction[i].replace(' ','') + '"'
deductionForMaxima += ']'

#maximaCode = ['load("C:/Users/reijo/OneDrive/STACK-MAXIMA-FO/FO_ND.mac")$']
maximaCode = ['load("C:/Users/rj421611/Desktop/GitHub/STACK-MAXIMA-FO/FO_ND.mac")$']
maximaCode.append(f'FREEVARIABLES:{freevariablesForMaxima}$')

maximaCode.append(f'deduction:{deductionForMaxima}$')
maximaCode.append(f'inferenceVerifier(1,{assumptionsForMaxima},[],deduction);')

outputRows = RunMaxima.runMaximaCode(maximaCode)

for output in outputRows:
	output = output.split(',')
	if len(output) != 3:
		print('Maxima error occured.')
	elif output[1] == '0':
		print('Proof is correct!')
	else:
		print(f'There was a mistake in the line {output[2][:len(output[2])-1]}')