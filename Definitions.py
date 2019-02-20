
import numpy as np


def find_nearest(array,value):
    idx = (np.abs(array-value)).argmin()
    return array[idx]


######################################## #################### #################### #################### 
####  Magboltz array indexing for the iput file 
###       [0    , 1    ,2    , 3   , 4     , 5     , 6   , 7    , 8   , 9    , 10  ,     11  , 12    ,  13 , 14 ]
###Vals = [XePer, ArPer, Temp, Pres, Efield, Zdrift, Zerr, Tdiff, Terr, Ldiff, Lerr, LdiffTPC,LerrTPC, Mele, Merr]
###                  11    , 12    ,    13   ,    14  ,  15 , 16 ]
###              LdiffTPC  ,LerrTPC, TdiffTCP, TerrTPC, Mele, Merr]
############################ #################### #################### #################### ####################
#################### 
####################  Below is the Magboltz importing function for the velocity and both diffusion in both set of units
####################





def MB_V(data,x):
    Vz = data[x][:,5]
    P  = data[x][:,3]/760
    E  = data[x][:,4]
    xe = str(data[x][0][0])
    ar = str(data[x][0][1])
    lab = xe+'%Xe '+ar+'%He'
    X = E/P
    Y = Vz
    Yer =Vz*data[x][:,6]/100
    drop = np.where(Y == 0)[0]
    X = np.delete(X,drop)
    Y = np.delete(Y,drop)
    Yer=np.delete(Yer,drop)
    SORT = X.argsort()
    X = X[SORT]
    Y = Y[SORT]
    Yer = Yer[SORT]
    
    Xnew = X#np.linspace(0, 300, 10000)
    Ynew = Y#np.interp(Xnew, X, Y)
    return Xnew,Ynew,Yer,lab


def MB_DLtpc(data,x):
    Vz = data[x][:,11]
    P  = data[x][:,3]/760
    E  = data[x][:,4]
    xe = str(data[x][0][0])
    ar = str(data[x][0][1])
    lab = xe+'%Xe '+ar+'%He'
    X = E/P
    Y = Vz*np.sqrt(P)
    Yer =Vz*data[x][:,12]/100
    drop = np.where(Y == 0)[0]
    X = np.delete(X,drop)
    Y = np.delete(Y,drop)
    Yer=np.delete(Yer,drop)
    SORT = X.argsort()
    X = X[SORT]
    Y = Y[SORT]
    Yer = Yer[SORT]

    Xnew = X#np.linspace(0, 300, 1000)
    Ynew = Y#np.interp(Xnew, X, Y)
    return Xnew,Ynew,Yer,lab

def MB_DTtpc(data,x):
    Vz = data[x][:,13]
    P  = data[x][:,3]/760
    E  = data[x][:,4]
    xe = str(data[x][0][0])
    ar = str(data[x][0][1])
    lab = xe+'%Xe '+ar+'%He'
    X = E/P
    Y = Vz*np.sqrt(P)
    Yer =Vz*data[x][:,14]/100
    drop = np.where(Y == 0)[0]
    X = np.delete(X,drop)
    Y = np.delete(Y,drop)
    Yer=np.delete(Yer,drop)
    SORT = X.argsort()
    X = X[SORT]
    Y = Y[SORT]
    Yer = Yer[SORT]

    Xnew = X#np.linspace(0, 300, 1000)
    Ynew = Y#np.interp(Xnew, X, Y)
    return Xnew,Ynew,Yer,lab


def MB_DL(data,x):
    Vz = data[x][:,9]
    P  = data[x][:,3]/760
    E  = data[x][:,4]
    xe = str(data[x][0][0])
    ar = str(data[x][0][1])
    lab = xe+'%Xe '+ar+'%He'
    X = E/P
    Y = Vz*P
    Yer =Vz*data[x][:,10]/100
    drop = np.where(Y == 0)[0]
    X = np.delete(X,drop)
    Y = np.delete(Y,drop)
    Yer=np.delete(Yer,drop)
    SORT = X.argsort()
    X = X[SORT]
    Y = Y[SORT]
    Yer = Yer[SORT]

    Xnew = X#np.linspace(0, 300, 1000)
    Ynew = Y#np.interp(Xnew, X, Y)
    return Xnew,Ynew,Yer,lab

def MB_DT(data,x):
    Vz = data[x][:,7]
    P  = data[x][:,3]/760
    E  = data[x][:,4]
    xe = str(data[x][0][0])
    ar = str(data[x][0][1])
    lab = xe+'%Xe '+ar+'%He'
    X = E/P
    Y = Vz*P
    Yer =Vz*data[x][:,8]/100
    drop = np.where(Y == 0)[0]
    X = np.delete(X,drop)
    Y = np.delete(Y,drop)
    Yer=np.delete(Yer,drop)
    SORT = X.argsort()
    X = X[SORT]
    Y = Y[SORT]
    Yer = Yer[SORT]

    Xnew = X#np.linspace(0, 300, 1000)
    Ynew = Y#np.interp(Xnew, X, Y)
    return Xnew,Ynew,Yer,lab


def MB_eff_EleL(data,x):
    Vz = data[x][:,5]
    Dl = data[x][:,9]
    P  = data[x][:,3]/760
    E  = data[x][:,4]
    xe = str(data[x][0][0])
    ar = str(data[x][0][1])
    lab = xe+'%Xe '+ar+'%He'
    X = E/P
    mu = (Vz*1e5)/E
    Y = Dl/mu
    Yer =Vz*data[x][:,6]/100
    drop = np.where(Y == 0)[0]
    X = np.delete(X,drop)
    Y = np.delete(Y,drop)
    Yer=np.delete(Yer,drop)
    SORT = X.argsort()
    X = X[SORT]
    Y = Y[SORT]
    Yer = Yer[SORT]

    Xnew = X#np.linspace(0, 300, 1000)
    Ynew = Y#np.interp(Xnew, X, Y)
    return Xnew,Ynew,Yer,lab

######################################## #################### #################### ####################
######
######  Below is the definitons for the corrections of the drift and diffusion
######
######################################## #################### #################### #################### 

##  Corrects the drift for the time spent in the gold gap which is half the gap width
def CORRECTION_V(DT,Pres,Efid):
    P = Pres
    E = Efid
    gapwidth = .397/2
    d = 14.128 
    V = (d+gapwidth)/DT
    Pressures = P[E==300]
    CorrVals = gapwidth/V[E==300]
    CorrectionT = np.copy(P)
    for x in range(0,len(Pressures)):
        CorrectionT[CorrectionT==Pressures[x]] =CorrVals[x]
    dt_new = DT-CorrectionT
    return dt_new

## This is the correction to find the time spend in the
#  this is like the above but it has the full gap width and we want the corection time as t1
def CORRECTION_t1(DT,Pres,Efid):
    P = Pres
    E = Efid
    gapwidth = .397
    d = 14.128 
    V = (d+gapwidth)/DT
    Pressures = P[E==300]
    CorrVals = gapwidth/V[E==300]
    CorrectionT = np.copy(P)
    for x in range(0,len(Pressures)):
        CorrectionT[CorrectionT==Pressures[x]] =CorrVals[x]
    dt_gap  = CorrectionT
    return dt_gap

## This is to find the correction to sigma_squared
## done by taking the diffusion of the fill length and that time then
## correcting fot the diffusion in the gap which comes out as the correction
def CORRECTION_SIG(DT,Pres,Efid,Sigma):
    P = Pres
    E = Efid
    t1 = CORRECTION_t1(DT,P,E)
    gapwidth = .397
    d = 14.128 
    dfull = d+gapwidth
    # corrected time
    t2 = DT+0.5*t1
    # diffusion when the field and gold have same efield
    D300 = Sigma[E==300]*dfull**2/(2*(t2[E==300])**3)
    # use this case to correct each sigma 
    sigmaCorSquared = 2*t1[E==300]**3*D300/gapwidth**2
    # this just orders the array to match up with each pressure
    Pressures = P[E==300]
    CorrectionT = np.copy(P)
    for x in range(0,len(Pressures)):
        CorrectionT[CorrectionT==Pressures[x]] =sigmaCorSquared[x]
    sigma_squared_cor  = CorrectionT
    return sigma_squared_cor
