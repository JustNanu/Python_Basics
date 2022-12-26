
#reading the csv file
data = pd.read_csv("C:\\Users\\2204a\\Downloads\\iris_csv.csv")

#displaying up the top rows of the dataset with their columns
data.head()

#Displaying the number of rows randomly. 
data.sample(12)

#Displaying the number of columns and names of the columns. 
data.columns

#Displaying the shape of the dataset.
data.shape

print(data)

#Displaying only specific columns.
  
specific_data=data[["petallength","class"]]
#data[["column_name1","column_name2","column_name3"]]
  
#now we will print the first 10 columns of the specific_data dataframe.
print(specific_data.head(10))

#Calculating sum, mean and mode of a particular column
sum_data = data["sepallength"].sum()
mean_data = data["sepallength"].mean()
median_data = data["sepallength"].median()
  
print("Sum:",sum_data, "\nMean:", mean_data, "\nMedian:",median_data)

# Extracting minimum and maximum from a column.
min_data=data["sepallength"].min()
max_data=data["sepallength"].max()
  
print("Minimum:",min_data, "\nMaximum:", max_data)
