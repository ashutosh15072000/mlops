import pandas as pd
import os

## Create a simple DataFreme with columns name
data={'Name':['ashu',"ram","shyam"],
      "Age":[25,20,15],
      "City":["Lcuknow","Delhi","Punjab"]
      }

df = pd.DataFrame(data)
# ## Adding new row to df for v2
# new_row_loc = {"Name":'v2', "Age":30, "City":'Lucknow'}
# df.loc[len(df.index)]=new_row_loc

# ## Adding new row to df for v3
# new_row_loc = {"Name":'v3', "Age":35, "City":'Lucknow'}
# df.loc[len(df.index)]=new_row_loc

## Ensure the ""data"" directerory exists at the root level
data_dir="DVC/data"
os.makedirs(data_dir,exist_ok=True)
## Define the file Path
file_path=os.path.join(data_dir,"sample_data.csv")

## Save the dataframe to a csv file including columns name
df.to_csv(file_path,index=False)
print(f"csv file saved to {file_path}")