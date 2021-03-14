#Header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#Reading of the file
data=pd.read_csv(path)

# Code starts here
#<-----> PART-1 <----->
data.Gender.replace(to_replace="-", value="Agender")
gender = data["Gender"].value_counts()
gender.plot(kind="bar")
plt.show()

#<-----> PART-2 <----->
data.groupby(["Alignment"]).sum().plot(kind="pie",y="ID",figsize=(8,8),shadow=True)
print("------------------")

#<-----> PART-3 <----->
print("COMBAT VS STRENGTH")
pearso = data["Combat"].corr(data["Strength"],method="pearson");
print(pearso)
spearm = data["Combat"].corr(data["Strength"],method="spearman");
print(spearm)
print("------------------")
print("COMBAT VS INTELLIGENCE")
pears = data["Combat"].corr(data["Intelligence"],method="pearson");
print(pears)
spear = data["Combat"].corr(data["Intelligence"],method="spearman");
print(spear)
#print(pearson)
#<-----> PART-4 <----->
print("------------------")
total=data["Total"].quantile(0.99)
print(total)
print("------------------")
Tot = data[data["Total"] > 554.0500000000008]
#print(Tot)
super_best_names = Tot.Name.head(7)
print(super_best_names.tolist())
print("------------------")
