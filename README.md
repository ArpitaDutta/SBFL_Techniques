# SBFL_Techniques
This repository contains codes for the important Spectrum based Fault Localization techniques.
Here are the selected SBFL techniques:
1. DStar
2. Tarantula
3. Ochiai
4. FTFL
5. Barinel
6. ER1
7. ER5
8. GP02
9. GP03
10. GP19
11. Jaccard
12. Op2


# Usage
``python3 faultLocalizationMain.py <statementCoverageFileName> <FaultyLineNumber> <SBFL_MethodName> <OutputFileName>``

Here, 1. ``<statementCoverageFileName>`` is the input statement coverage information file in csv format. Do not add the file extension.

## Format of the Input File
Each row represents the statement coverage information of a test case followed by the test case result.
Statement executed by the test case is respresented as 1 otherwise 0. Similarly, the pass test cases are represented with 0 and failed test cases are by 1 in the Result column.

Note: Only executable statements are considered.

An example input file is statementResult.csv avaiable in the repository.

2. ``<FaultyLineNumber>`` : Enter the line number of the faulty statement.
3. ``<SBFL_MethodName>`` : Mention the fault technique used to generate the rank of the statements. Use any one of the technique mention above between 1-12.
4. ``<OutputFileName>`` : Enter the output file. 


