import RunMaxima

maximaCode = ['load("C:/Users/reijo/OneDrive/STACK-MAXIMA-FO/RELATIONAL_ALGEBRAS.mac")$']

maximaCode.append('P: [1,{[0],[1]}]$')
maximaCode.append('R1: [2,{[0,0],[1,1]}]$')
maximaCode.append('R2: [2,{[0,1],[1,0]}]$')

print('Cartesian product:\n')

maximaCode.append('T: cartesianProduct(R1,P);')
maximaCode.append('T: cartesianProduct(R2,P);')
maximaCode.append('T: cartesianProduct(P,R1);')
maximaCode.append('T: cartesianProduct(P,R2);')
maximaCode.append('T: cartesianProduct(R1,R2);')
maximaCode.append('T: cartesianProduct(R2,R1);')

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