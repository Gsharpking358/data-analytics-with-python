# --------------
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
#alignment = data["Alignment"].value_counts()
#plt.pie(alignment)
#plt.show()
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
super_best_names = ['Amazo', 'General Zod', 'Martian Manhunter', 'Stardust', 'Superboy-Prime', 'Superman']
print(super_best_names)



