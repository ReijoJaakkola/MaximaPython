import RunMaxima

maximaCode = ['load("C:/Users/reijo/OneDrive/STACK-MAXIMA-FO/RELATIONAL_ALGEBRAS.mac")$']

maximaCode.append('P: [1,{[0],[1]}]$')
maximaCode.append('R1: [2,{[0,0],[1,1]}]$')
maximaCode.append('R2: [2,{[0,1],[1,0]}]$')
maximaCode.append('vocabulary: {"P","R1","R2"}$')
maximaCode.append('interpretation: [["P",P],["R1",R1],["R2",R2]]$')

print('Cartesian product:\n')

maximaCode.append('T: cartesianProduct(R1,P);')
maximaCode.append('T: evaluateQuery("J[R1,P]",vocabulary,interpretation);')
maximaCode.append('T: cartesianProduct(R2,P);')
maximaCode.append('T: evaluateQuery("J[R2,P]",vocabulary,interpretation);')
maximaCode.append('T: cartesianProduct(P,R1);')
maximaCode.append('T: evaluateQuery("J[P,R1]",vocabulary,interpretation);')
maximaCode.append('T: cartesianProduct(P,R2);')
maximaCode.append('T: evaluateQuery("J[P,R2]",vocabulary,interpretation);')
maximaCode.append('T: cartesianProduct(R1,R2);')
maximaCode.append('T: evaluateQuery("J[R1,R2]",vocabulary,interpretation);')
maximaCode.append('T: cartesianProduct(R2,R1);')
maximaCode.append('T: evaluateQuery("J[R2,R1]",vocabulary,interpretation);')

outputRows = RunMaxima.runMaximaCode(maximaCode)
for output in outputRows:
	print(output)

print()

print('Union:\n')

maximaCode = ['load("C:/Users/reijo/OneDrive/STACK-MAXIMA-FO/RELATIONAL_ALGEBRAS.mac")$']

maximaCode.append('P: [1,{[0],[1]}]$')
maximaCode.append('R1: [2,{[0,0],[1,1]}]$')
maximaCode.append('R2: [2,{[0,1],[1,0]}]$')

maximaCode.append('T: arityDefinedUnion(R1,P);')
maximaCode.append('T: arityDefinedUnion(R2,P);')
maximaCode.append('T: arityDefinedUnion(P,R1);')
maximaCode.append('T: arityDefinedUnion(P,R2);')
maximaCode.append('T: arityDefinedUnion(R1,R2);')
maximaCode.append('T: arityDefinedUnion(R2,R1);')

outputRows = RunMaxima.runMaximaCode(maximaCode)
for output in outputRows:
	print(output)

print()

print('Intersection:\n')

maximaCode = ['load("C:/Users/reijo/OneDrive/STACK-MAXIMA-FO/RELATIONAL_ALGEBRAS.mac")$']

maximaCode.append('P: [1,{[0],[1]}]$')
maximaCode.append('R1: [2,{[0,0],[1,1]}]$')
maximaCode.append('R2: [2,{[0,1],[1,0]}]$')

maximaCode.append('T: arityDefinedIntersection(R1,P);')
maximaCode.append('T: arityDefinedIntersection(R2,P);')
maximaCode.append('T: arityDefinedIntersection(P,R1);')
maximaCode.append('T: arityDefinedIntersection(P,R2);')
maximaCode.append('T: arityDefinedIntersection(R1,R2);')
maximaCode.append('T: arityDefinedIntersection(R2,R1);')
outputRows = RunMaxima.runMaximaCode(maximaCode)
for output in outputRows:
	print(output)

print()

print('Choose:\n')

maximaCode = ['load("C:/Users/reijo/OneDrive/STACK-MAXIMA-FO/RELATIONAL_ALGEBRAS.mac")$']

maximaCode.append('P: [1,{[0],[1]}]$')
maximaCode.append('R1: [2,{[0,0],[1,1]}]$')
maximaCode.append('R2: [2,{[0,1],[1,0]}]$')

maximaCode.append('T: choose(1,1,P);')
maximaCode.append('T: choose(1,2,R1);')
maximaCode.append('T: choose(1,2,R2);')

outputRows = RunMaxima.runMaximaCode(maximaCode)
for output in outputRows:
	print(output)

print()

print('Select:\n')

maximaCode = ['load("C:/Users/reijo/OneDrive/STACK-MAXIMA-FO/RELATIONAL_ALGEBRAS.mac")$']

maximaCode.append('P: [1,{[0],[1]}]$')
maximaCode.append('R1: [2,{[0,0],[1,1]}]$')
maximaCode.append('R2: [2,{[0,1],[1,0]}]$')

maximaCode.append('T: select([1],P);')
maximaCode.append('T: select([1],R1);')
maximaCode.append('T: select([1],R2);')
maximaCode.append('T: select([1,1],R1);')
maximaCode.append('T: select([1,1],R2);')
maximaCode.append('T: select([2,1],R1);')
maximaCode.append('T: select([2,1],R2);')

outputRows = RunMaxima.runMaximaCode(maximaCode)
for output in outputRows:
	print(output)

print()