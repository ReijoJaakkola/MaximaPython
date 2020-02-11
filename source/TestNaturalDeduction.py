import RunMaxima

###########################################################################################################################################################################################
#                                                               VALID DEDUCTIONS                                                                                                          #
###########################################################################################################################################################################################

print('VALID DEDUCTIONS\n')

# Create the input strings.
#maximaCode = ['load("C:/Users/reijo/OneDrive/STACK-MAXIMA-FO/FO_ND.mac")$']
maximaCode = ['load("C:/Users/rj421611/Desktop/GitHub/STACK-MAXIMA-FO/FO_ND.mac")$']

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

maximaCode.append('deduction:["OLR","UT1UxR"]$')
maximaCode.append('inferenceVerifier(1,["R"],[],deduction);')

maximaCode.append('deduction:["OLUxR","UE1R"]$')
maximaCode.append('inferenceVerifier(1,["UxR"],[],deduction);')

maximaCode.append('FREEVARIABLES:[["P",{"y"}],["R",{"x","y"}]]$')

maximaCode.append('deduction:["OLUx(P(y)->R(x,y))","OLP(y)","UE1(P(y)->R(x,y))","IE2,3R(x,y)","UT4UxR(x,y)"]$')
maximaCode.append('inferenceVerifier(1,["Ux(P(y)->R(x,y))","P(y)"],[],deduction);')

maximaCode.append('deduction:["OL(P(y)&UxR(x,y))","KE1UxR(x,y)","UE2R(x,y)","KE1P(y)","KT3,4(P(y)&R(x,y))","UT5Ux(P(y)&R(x,y))"]$')
maximaCode.append('inferenceVerifier(1,["(P(y)&UxR(x,y))"],[],deduction);')

maximaCode.append('deduction:["OL(P|UxR)","<AOP","DT2(P|R)>","<AOUxR","UE4R","DT5(P|R)>","DE1(P|R)","UT7Ux(P|R)"]$')
maximaCode.append('inferenceVerifier(1,["(P|UxR)"],[],deduction);')

maximaCode.append('deduction:["OLR","ET1ExR"]$')
maximaCode.append('inferenceVerifier(1,["R"],[],deduction);')

maximaCode.append('FREEVARIABLES:[["R",{"x","y"}]]$')

maximaCode.append('deduction:["OLExEyR","<AOEyR","<AOR","ET3ExR","ET4EyExR>","EEEyExR>","EEEyExR"]$')
maximaCode.append('inferenceVerifier(1,["ExEyR"],[],deduction);')

maximaCode.append('FREEVARIABLES:[["P",{"x"}],["R",{"y"}]]$')

maximaCode.append('deduction:["OLUx(P&Q)","UE1(P&Q)","KE2P"]$')
maximaCode.append('inferenceVerifier(1,["Ux(P&Q)"],[],deduction);')

maximaCode.append('FREEVARIABLES:[["P",{"y"}],["R",{"x"}]]$')

maximaCode.append('deduction:["OLEy(R&P)","<AO(R&P)","KE2R","KE2P","ET4EyP","KT3,5(R&EyP)>","EE(R&EyP)"]$')
maximaCode.append('inferenceVerifier(1,["Ey(R&P)"],[],deduction);')

maximaCode.append('deduction:["OL(A&!A)","<AO!B","RE(A&!A)>","NT!!B","NE4B"]$')
maximaCode.append('inferenceVerifier(1,["(A&!A)"],[],deduction);')

maximaCode.append('deduction:["OL(A->B)","OL(B->A)","YT(A<->B)"]$')
maximaCode.append('inferenceVerifier(1,["(A->B)","(B->A)"],[],deduction);')

maximaCode.append('deduction:["OLA","OL(A<->B)","YE1,2B"]$')
maximaCode.append('inferenceVerifier(1,["A","(A<->B)"],[],deduction);')

outputRows = RunMaxima.runMaximaCode(maximaCode)
for output in outputRows:
	print(output)

print('\nWe had 23 cases.')
print(f'We obtained results for {len(outputRows)} cases.\n')

###########################################################################################################################################################################################
#                                                               INVALID DEDUCTIONS                                                                                                        #
###########################################################################################################################################################################################

print('\nINVALID DEDUCTIONS\n')

#maximaCode = ['load("C:/Users/reijo/OneDrive/STACK-MAXIMA-FO/FO_ND.mac")$']
maximaCode = ['load("C:/Users/rj421611/Desktop/GitHub/STACK-MAXIMA-FO/FO_ND.mac")$']

maximaCode.append('FREEVARIABLES:[["R",{"x","y"}]]$')

maximaCode.append('deduction:["OLUxEyR","UE1EyR","<AOR","UT3UxR","ET4EyUxR>","ETEyUxR"]$')
maximaCode.append('inferenceVerifier(1,["UxEyR"],[],deduction);')

outputRows = RunMaxima.runMaximaCode(maximaCode)
for output in outputRows:
	print(output)

print('\nWe had 1 cases.')
print(f'We obtained results for {len(outputRows)} cases.')
print()