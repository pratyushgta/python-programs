import pandas as pd

mydataset = {
    'cars': ["BMW", "Volvo", "Ford"],
    'passings': [3, 7, 2]
}
myvar = pd.DataFrame(mydataset)

print(myvar)

a = [1, 7, 2]
myvar = pd.Series(a,index=["x","y","z"])
print(myvar["y"])


data = {
    "Calories":[420,380,390],
    "duration":[50,40,45]
}
myvar = pd.DataFrame(data)
print(myvar)


pd.options.display.max_rows = 9999
df = pd.read_csv("C:/Users/praty/Desktop/StudentsPerformance.csv")
print(df)


###########
import pandas as pd

df = pd.read_csv("C:/Users/praty/Desktop/StudentsPerformance.csv")
print(df.to_string()) #print whole dataset

###########