import numpy as np
from faultLocalizationGenRank import gen_rank

# Tarantula (Method 1)
def tarantula(method,faultyLine,outputFile,Ncf, Nuf, Ncs, Nus):
    suspiciousness = ((Ncs/(Ncs+Nus))/ (Ncs/(Ncs+Nus))+ (Ncf/(Ncf+Nuf)))
    gen_rank(method,faultyLine,outputFile,suspiciousness)

# Dstar，star is assigned to 2 (Method 2)
def dstar(method,faultyLine,outputFile,Ncf, Nuf, Ncs, Nus):
    suspiciousness = (Ncf ** 2 / (Ncs + Nuf))
    gen_rank(method,faultyLine,outputFile,suspiciousness)


# Ochiai (Method 3)
def ochiai(method,faultyLine,outputFile,Ncf, Nuf, Ncs, Nus):
    div = (Ncf + Nuf) * (Ncf + Ncs)
    #print("div",div)
    #div = 0 if div < 0 else div
    suspiciousness = (Ncf / np.sqrt(div))
    gen_rank(method,faultyLine,outputFile,suspiciousness)


# Barinel (Method 4)
def barinel(method,faultyLine,outputFile,Ncf, Nuf, Ncs, Nus):
    suspiciousness = (1 - Ncs / (Ncs + Ncf))
    gen_rank(method,faultyLine,outputFile,suspiciousness)


# ER1 (Method 5)
def ER1(method,faultyLine,outputFile,Ncf, Nuf, Ncs, Nus):
    suspiciousness = (Ncf * (1 + Ncs / (2 * Ncs + Ncf)))
    gen_rank(method,faultyLine,outputFile,suspiciousness)


# ER5 (Method 6)
def ER5(method,faultyLine,outputFile,Ncf, Nuf, Ncs, Nus):
    suspiciousness = (Ncf * (Ncf + Nuf + Ncs + Nus))
    gen_rank(method,faultyLine,outputFile,suspiciousness)


# GP02 (Method 7)
def GP02(method,faultyLine,outputFile,Ncf, Nuf, Ncs, Nus):
    #Nus = 0 if Nus < 0 else Nus
    #Ncs = 0 if Ncs < 0 else Ncs
    suspiciousness = (2 * (Ncf + np.sqrt(Nus)) + np.sqrt(Ncs))
    gen_rank(method,faultyLine,outputFile,suspiciousness)


# GP03 (Method 8)
def GP03(method,faultyLine,outputFile,Ncf, Nuf, Ncs, Nus):
    #Ncs = 0 if Ncs < 0 else Ncs
    suspiciousness = (np.sqrt(np.abs(Ncf * Ncf - np.sqrt(Ncs))))
    gen_rank(method,faultyLine,outputFile,suspiciousness)


# GP19 (Method 9)
def GP19(method,faultyLine,outputFile,Ncf, Nuf, Ncs, Nus):
    suspiciousness = (Ncf * np.sqrt(np.abs(Ncs - Ncf + Nuf - Nus)))
    gen_rank(method,faultyLine,outputFile,suspiciousness)


# Jaccard (Method 10)
def Jaccard(method,faultyLine,outputFile,Ncf, Nuf, Ncs, Nus):
    suspiciousness = (Ncf / (Nuf + Ncs + Nus))
    gen_rank(method,faultyLine,outputFile,suspiciousness)

# Op2 (Method 11)
def Op2(method,faultyLine,outputFile,Ncf, Nuf, Ncs, Nus):
    suspiciousness = (Ncf - Ncs / (Ncs + Nus + 1))
    gen_rank(method,faultyLine,outputFile,suspiciousness)

# FTFL (Method 12)
def FTFL(method,faultyLine,outputFile, Ncs, Ncf, Nus, Nuf, logInfo, N, Nf, Ns):
    suspiciousness=np.zeros(len(Ncs))
    Nc = Ncs + Ncf
    Nu = Nus + Nuf

    print(len(Ncs))
    for i in range(0,len(Ncs)):
        try:
            n_cs = int(Ncs[i])
            n_cf = int(Ncf[i])
            n_uf = int(Nuf[i])
            n_us = int(Nus[i])
            n_c = int(Nc[i])
            n_u = int(Nu[i])
            m_w = 0
            chi_w_num = 0
            chi_w_den = 0
            chi_w = 0

            #print(n_c,n_u)
            # factor 1 computation
            if Nc[i] == N:                
                factor1= logInfo[n_c-1] 
            else:              
                factor1= logInfo[n_c-1] + logInfo[n_u-1]

            # factor 2 computation
            if Nc[i] == N: 
                n_us = 1
                n_uf = 1
            if n_uf == 0:
                n_uf = 1
            if n_cs == 0:
                n_cs == 1
            factor2 = logInfo[n_cs-1]+logInfo[n_cf-1]+logInfo[n_us-1]+logInfo[n_uf-1]

            m_w = float(factor1)-float(factor2)
            if Nf != 0:
                chi_w_num= float(n_cf)/Nf
            if Ns != 0:
                chi_w_den= float(n_cs)/Ns
            if chi_w_den != 0:
                chi_w= float(chi_w_num)/chi_w_den
            if chi_w>1:
                suspiciousness[i] = m_w
            elif chi_w == 1:
                suspiciousness[i] = 0
            else:
                suspiciousness[i] = -m_w

        except ZeroDivisionError:
            suspiciousness[i]=0
    #print(suspiciousness)
    gen_rank(method,faultyLine,outputFile,suspiciousness)

