def thomas(Alower,Amiddle,Aupper,b):
    """Alower is the row lower than the diagonal
    Amiddle is the diagonal
    Aupper is the row above the diagonal
    b is the vector you solve against
    returns the solution to Ax=b"""
    n,=np.shape(Amiddle)
    for i in range(n-1):
        Alower[i]    = Alower[i]/Amiddle[i]
        Amiddle[i+1]-= Aupper[i]*Alower[i]
        b[i+1]      -= Alower[i]*b[i]
    x = b.copy()
    x[-1]/=Amiddle[-1]
    for i in range(n-2,-1,-1):
        x[i]-=Aupper[i]*x[i+1]
        x[i]/=Amiddle[i]
    return x
