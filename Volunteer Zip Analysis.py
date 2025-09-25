import pandas as pd

import os

#Exercise 1

# Reads ‘volunteers.csv’ and saves it as a data frame with a variable name of your choice.

path = r"###" #Enter your path here
os.chdir(path)

Volunteers = pd.read_csv('volunteer.csv')

# Renames the columns “Phone1” and “Phone2” to “Daytime phone” and “Evening phone,” respectively.

Volunteers.rename(columns ={'phone1':'Daytime phone'},inplace = True)
Volunteers.rename(columns ={'phone2':'Evening phone'},inplace = True)

# Prints out just the First Name, Last Name, and Daytime phone number for the first 20 records in the data frame.

print(Volunteers[['firstname','lastname','Daytime phone']][:20])

# Prepares counts of how many times each zip code appears in this data, and saves these counts as a new dataframe.

ZipCounts = Volunteers['zip5'].value_counts()

print(ZipCounts)

# Writes the zipcode counts data frame to a new CSV called “zip5_counts.csv“

ZipCounts.to_csv('zip5_counts.csv')

#Bonus: Have your script perform one other PANDAS operation of your choice (e.g. rearrange something, calculate something), and add comments to explain what you did. 

UniqueZips = len(ZipCounts) #Count unique zip codes

print('Number of Unique Zip Codes:',UniqueZips) #Reports unique zip codes
