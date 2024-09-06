import sys
import pandas as pd
import numpy as np
import os.path

from faultLocalizationMethods import ER1, ER5, FTFL, GP02, GP03, GP19, Jaccard, Op2, barinel, dstar, ochiai, tarantula

def get_feature(coverage_mat, test_res):
    # Binary Coverage Matrix and Test Result vector
    # n_cf[i]: no. of failed test cases covered the statement i
    # n_uf[i]: no. of failed test cases not covered the statement i    
    # n_cs[i]: no. of pass test cases covered the statement i
    # n_us[i]: no. of pass test cases not covered the statement i

    n= len(test_res) # Total number of test cases present for this program
    n_f=np.count_nonzero(test_res) # Total number of failed test cases for this program
    n_s= n-n_f #Total number of passed test cases   

    coverage_mat = np.array(coverage_mat)
    test_res = np.array(test_res)
    n= len(test_res) # Total number of test cases present for this program
    n_f=np.count_nonzero(test_res) # Total number of failed test cases for this program
    n_s= n-n_f #Total number of passed test cases   
    # print(coverage_mat)
    # print(test_res)
    n_cs=np.zeros(len(coverage_mat[0]))

    n_cf=np.zeros(len(coverage_mat[0]))
    for i in range(0,len(coverage_mat[0])):
        for j in range(0,len(test_res)):
            #print (coverage_mat[j][i],test_res[j][0], "no")
            if coverage_mat[j][i] == 1 and test_res[j][0] == 0:
                n_cs[i]=n_cs[i]+1
            elif coverage_mat[j][i] == 1 and test_res[j][0] == 1:
                n_cf[i]=n_cf[i]+1
            
    n_us=n_s-n_cs
    n_uf=n_f-n_cf
    # print(n_cs)
    # print(n_cf)
    # print(n_us)
    # print(n_uf)
    return n_cs, n_cf, n_us, n_uf


def switch(method, faultyLine, outputFile, Ncf, Nuf, Ncs, Nus, logInfo, total_tc, total_failed_tc, total_pass_tc):
    if method == "Tarantula": # Tarantula (Method 1)
        tarantula(method, faultyLine, outputFile, Ncf, Nuf, Ncs, Nus)
    elif method == "DStar": # Dstar，star is assigned to 2 (Method 2)
        dstar(method,faultyLine,outputFile,Ncf, Nuf, Ncs, Nus)
    elif method == "Ochiai": # Ochiai (Method 3)
        ochiai(method,faultyLine,outputFile,Ncf, Nuf, Ncs, Nus)
    elif method == "Barinel": # Barinel (Method 4)
        barinel(method,faultyLine,outputFile,Ncf, Nuf, Ncs, Nus)
    elif method == "ER1":  # ER1 (Method 5)
        ER1(method,faultyLine,outputFile,Ncf, Nuf, Ncs, Nus)
    elif method == "ER5": # ER5 (Method 6)
        ER5(method,faultyLine,outputFile,Ncf, Nuf, Ncs, Nus)
    elif method == "GP02": # GP02 (Method 7)
        GP02(method,faultyLine,outputFile,Ncf, Nuf, Ncs, Nus)
    elif method == "GP03": # GP03 (Method 8)
        GP03(method,faultyLine,outputFile,Ncf, Nuf, Ncs, Nus)
    elif method == "GP19":  # GP19 (Method 9)
        GP19(method,faultyLine,outputFile,Ncf, Nuf, Ncs, Nus)
    elif method == "Jaccard": # Jaccard (Method 10)
        Jaccard(method,faultyLine,outputFile,Ncf, Nuf, Ncs, Nus)
    elif method == "Op2":  # Op2 (Method 11)
        Op2(method,faultyLine,outputFile,Ncf, Nuf, Ncs, Nus)
    elif method == "FTFL":
        FTFL(method, faultyLine, outputFile, Ncf, Nuf, Ncs, Nus, logInfo, total_tc, total_failed_tc, total_pass_tc)
    else:
        print("Method not found.\n")

def main():
    inputFile = sys.argv[1]
    faultyLine = sys.argv[2]
    method = sys.argv[3]
    outputFile = sys.argv[4]
    check_file = os.path.isfile(inputFile+str(".csv"))
    if check_file:
        df_train=pd.read_csv(inputFile+str(".csv"))
    else:
        print("Input File Not Found!!!")
        return
    df_train_log=pd.read_csv('logtableMod.csv')
    logInfo = np.array([df_train_log['AddedLogvalue']]).T
    resultVector = np.array([df_train['Result']]).T
    total_tc = len(resultVector) # Total number of test cases present for this program
    total_failed_tc = np.count_nonzero(resultVector) # Total number of failed test cases for this program
    total_pass_tc= total_tc-total_failed_tc #Total number of passed test cases 
    df_train.drop("Result", inplace=True, axis=1)   
    t_in = df_train.values.tolist()
    coverageInfo = np.array(t_in)
    Ncs, Ncf, Nus, Nuf = get_feature(coverageInfo, resultVector)
    switch(method, faultyLine, outputFile, Ncf, Nuf, Ncs, Nus, logInfo, total_tc, total_failed_tc, total_pass_tc)


if __name__ == "__main__":
    main()