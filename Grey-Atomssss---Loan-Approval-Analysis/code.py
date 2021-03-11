# --------------
# Importing header files
import numpy as np
import pandas as pd
from scipy.stats import mode 
 
import warnings
warnings.filterwarnings('ignore')


#Reading file
bank_data = pd.read_csv(path)

#Code starts here
#<-----> STEP - 1 <----->
categorical_var = bank_data.select_dtypes(include = "object")
print(categorical_var)
numerical_var = bank_data.select_dtypes(include = "number")
print(numerical_var)
print(categorical_var.shape)
numerical_var.shape

#<-----> STEP - 2 <----->
banks = bank_data.drop("Loan_ID",axis=1)
bank_data.isnull().sum()
bank_mode = bank_data.mode()
banks = banks.replace(to_replace=np.nan,value=bank_mode)
print(banks.isnull().sum().values.sum())

#<-----> STEP - 3 <----->
avg_loan_amount = pd.pivot_table(banks,index=["Gender","Married","Self_Employed"],values="LoanAmount",aggfunc="mean")
print(avg_loan_amount)

#<-----> STEP - 4 <----->
loan_approved_se = len(banks[(banks.Self_Employed == "Yes") & (banks.Loan_Status == "Y")])
loan_approved_nse = len(banks[(banks.Self_Employed == "No") & (banks.Loan_Status == "Y")])

percentage_se = loan_approved_se*100/614
print(percentage_se)
percentage_nse = loan_approved_nse*100/614
print(percentage_nse)

#<-----> STEP - 5 <----->
loan_term = banks["Loan_Amount_Term"].apply(lambda x:x/12)
banks["Loan_Amount_Term"] = loan_term

big_loan_term = len(banks[banks.Loan_Amount_Term > 25.0])
print(big_loan_term)

#<-----> STEP - 6 <----->
loan_groupby = banks.groupby("Loan_Status")[["ApplicantIncome","Credit_History"]]
mean_values = loan_groupby.agg("mean")
print(mean_values)






