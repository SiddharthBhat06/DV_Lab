import pandas as pd 
import numpy as np 
url="https://gist.githubusercontent.com/lisawilliams/a91ffcea96ac3af9500bbf6b92f1408e/raw/728e9b2e4fb0da2baa34e2da2a9d732d74b484ab/cereal.csv"
cer_off=pd.read_csv(url)
sumn_bfr=cer_off.describe().transpose()[["min","25%","50%","max"]]
print("Five number summary before treating missing values")
print(sumn_bfr)
num_col=cer_off.select_dtypes(include=["number"]).columns
for c in num_col:
    mean_val=cer_off[c][cer_off[c]!=-1].mean()
    cer_off[c]=cer_off[c].replace(-1,mean_val)
after_msng_val=cer_off.describe().transpose()[["min","25%","50%","max"]]
print("Five number summary after treating missing values")
print(after_msng_val)