# coding: utf-8
def series(R):
    Req=0
    for i in range(len(R)):
        Req+=R[i]
    return Req
def parallel(R):
    Req=0
    invReq=0
    for i in range(len(R)):
        invReq+=1./R[i]
    Req=1./invReq
    return Req
def voltsAcrossResistor(totalV,rArray,rIndex):
    rEq=series(rArray)
    return totalV*1.*rArray[rIndex]/rEq
def currentAcrossBranch(totalI,rArray,rIndex):
    rEq=parallel(rArray)
    return totalI*rEq/rArray[rIndex]
def toRPhasor(Amplitude,phase):
	return complex(Amplitude*cos(phase,Amplitude*sin(phase)))

def toPhasor(complexNum):
	return [sqrt(complexNum.real**2+complexNum.imag**2),atan(complexNum.imag/complexNum.real)]

def toPhasorDeg(complexNum):
	return [sqrt(complexNum.real**2+complexNum.imag**2),180/pi*atan(complexNum.imag/complexNum.real)]

print("""
parallel, series, voltsAcrossResistor, toPhasorDeg, toRPhasor, toPhasor and currentAcrossBranch functions imported""")
 
