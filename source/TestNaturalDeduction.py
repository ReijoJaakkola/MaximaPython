import RunMaxima

# Create the input strings.
maximaCode = ['load("C:/Users/reijo/OneDrive/STACK-MAXIMA-FO/FO_ND.mac")$']

maximaCode.append('deduction:["OLA","DT1(A|B)"]$')
maximaCode.append('inferenceVerifier(["A"],[],deduction);')

maximaCode.append('deduction:["OL(A->C)","OL(B->C)","OL(A|B)","DE3C"]$')
maximaCode.append('inferenceVerifier(["(A->C)","(B->C)","(A|B)"],[],deduction);')

maximaCode.append('deduction:["OLA","OLB","KT1,2(A&B)"]$')
maximaCode.append('inferenceVerifier(["A","B"],[],deduction);')

maximaCode.append('deduction:["OL(A&B)","KE1A"]$')
maximaCode.append('inferenceVerifier(["(A&B)"],[],deduction);')

# What the output is expected to be.
expectedOutput = [0, 0, 0, 0]

print(f'Output: {RunMaxima.runMaximaCode(maximaCode)}\n')
print(f'Expected output: {expectedOutput}\n')