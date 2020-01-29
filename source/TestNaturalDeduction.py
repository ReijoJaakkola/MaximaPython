import RunMaxima

# Create the input strings.
maximaCode = ['load("C:/Users/reijo/OneDrive/STACK-MAXIMA-FO/FO_ND.mac")$']
#maximaCode = ['load("C:/Users/rj421611/Desktop/GitHub/STACK-MAXIMA-FO/FO_ND.mac")$']

maximaCode.append('deduction:["OLA","DT1(A|B)"]$')
maximaCode.append('inferenceVerifier(1,["A"],[],deduction);')

maximaCode.append('deduction:["OL(A->C)","OL(B->C)","OL(A|B)","DE3C"]$')
maximaCode.append('inferenceVerifier(1,["(A->C)","(B->C)","(A|B)"],[],deduction);')

maximaCode.append('deduction:["OLA","OLB","KT1,2(A&B)"]$')
maximaCode.append('inferenceVerifier(1,["A","B"],[],deduction);')

maximaCode.append('deduction:["OL(A&B)","KE1A"]$')
maximaCode.append('inferenceVerifier(1,["(A&B)"],[],deduction);')

maximaCode.append('deduction:["OL(A|A)","<AOA>","DE1A"]$')
maximaCode.append('inferenceVerifier(1,["(A|A)"],[],deduction);')

maximaCode.append('deduction:["<AOA>","IT(A->A)"]$')
maximaCode.append('inferenceVerifier(1,[],[],deduction);')

maximaCode.append('deduction:["OLA","OL(A->B)","IE1,2B"]$')
maximaCode.append('inferenceVerifier(1,["A","(A->B)"],[],deduction);')

maximaCode.append('deduction:["OLA","<AO!A","REA","KT1,2(A&!A)>","NT!!A"]$')
maximaCode.append('inferenceVerifier(1,["A"],[],deduction);')

maximaCode.append('deduction:["OL!!A","NE1A"]$')
maximaCode.append('inferenceVerifier(1,["!!A"],[],deduction);')

maximaCode.append('deduction:["OL((A&B)|C)","<AO(A&B)","KE2A","KE2B","DT3(A|C)","DT4(B|C)","KT5,6((A|C)&(B|C))>","<AOC","DT8(A|C)","DT8(B|C)","KT9,10((A|C)&(B|C))>","DE1((A|C)&(B|C))"]$');
maximaCode.append('inferenceVerifier(1,["((A&B)|C)"],[],deduction);')

maximaCode.append('deduction:["OL(A|!B)","<AOA","<AO(!A&B)","KE3!A","REA","KT4,5(A&!A)>","NT!(!A&B)>","<AO!B","<AO(!A&B)","KE9B","RE!B","KT10,11(B&!B)>","NT!(!A&B)>","DE1!(!A&B)"]$')
maximaCode.append('inferenceVerifier(1,["(A|!B)"],[],deduction);')

maximaCode.append('FREEVARIABLES:[["R",{"y"}]]$')

maximaCode.append('deduction:["OLR","AT1AxR"]$')
maximaCode.append('inferenceVerifier(1,["R"],[],deduction);')

maximaCode.append('deduction:["OLAxR","AE1R"]$')
maximaCode.append('inferenceVerifier(1,["AxR"],[],deduction);')

maximaCode.append('FREEVARIABLES:[["P",{"y"}],["R",{"x","y"}]]$')

maximaCode.append('deduction:["OLAx(P(y)->R(x,y))","OLP(y)","AE1(P(y)->R(x,y))","IE2,3R(x,y)","AT4AxR(x,y)"]$')
maximaCode.append('inferenceVerifier(1,["Ax(P(y)->R(x,y))","P(y)"],[],deduction);')

maximaCode.append('deduction:["OL(P(y)&AxR(x,y))","KE1AxR(x,y)","AE2R(x,y)","KE1P(y)","KT3,4(P(y)&R(x,y))","AT5Ax(P(y)&R(x,y))"]$')
maximaCode.append('inferenceVerifier(1,["(P(y)&AxR(x,y))"],[],deduction);')

outputRows = RunMaxima.runMaximaCode(maximaCode)
for output in outputRows:
	print(output)

print('\nWe had 15 cases.')
print(f'We obtained results for {len(outputRows)} cases.')