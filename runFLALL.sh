export statementCoverageFileName=$1
export FaultyLineNumber=$2
export SBFL_MethodName=$3
export OutputFileName=$4

eval "$(conda shell.bash hook)"
conda activate fl_all
python3 faultLocalizationMain.py $statementCoverageFileName $FaultyLineNumber $SBFL_MethodName $OutputFileName
