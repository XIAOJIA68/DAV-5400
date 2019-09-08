#!/usr/bin/env python
# coding: utf-8

# In[49]:


import csv 
# be sure to update the path below to reflect your own environment!! 
# also be sure that the code is properly indented after you paste it! 
 
with open('E:/Analytics Programming/cars-sample35.txt') as csvfile:
    readCSV = csv.reader(csvfile)     
    for row in readCSV:
        # print each row as read by the csv.reader function         
        print(row) 


# In[56]:


with open('E:/Analytics Programming/cars-sample35.txt') as csvfile:
    readCSV = csv.reader(csvfile)
    #convert readCSV to a list
    readCSV = list(readCSV)
    print(readCSV)


# In[105]:


# extract these seven attributes from each line of the list and create seven distinct lists
Price = [each_row[0] for each_row in readCSV]
Maintenance_cost = [each_row[1] for each_row in readCSV]
Number_of_doors = [each_row[2] for each_row in readCSV]
Number_of_passenger = [each_row[3] for each_row in readCSV]
Luggage_capacity  = [each_row[4] for each_row in readCSV]
Safety_rating  = [each_row[5] for each_row in readCSV]
Classification_of_vehicle  = [each_row[6] for each_row in readCSV]


# In[150]:


#create an empty list
med_index = []
#search very value in Price
for value in range(len(Price)):
    #extract value in Price equaling to 'med'
    if str(Price[value]) =='med':
        #add value to empty list
        med_index.append(value)       
print(med_index)


# In[132]:


new_passengers = []
for value in range(len(Price)):
    if str(Price[value]) =='med':
        new_passengers.append(Number_of_passenger[value])
print(new_passengers)


# In[135]:


index_automobile = []
for i in range(len(Price)):
    #using 'and' to meet two requirements at the same time
    if Price[i] == "high" and Maintenance_cost != "low":
        index_automobile.append(i)
print(index_automobile)


# In[138]:


index_auto = []
for i in range(len(Price)):
    if Number_of_doors[i] == '2' and Luggage_capacity[i] == 'big':
        index_auto.append(i)
print(index_auto)


# In[149]:


integer_door = []
for i in range(len(Number_of_doors)):
    if Number_of_doors[i] == '5more':
        #extract str '5' from the '5more'
        Number_of_doors[i] = Number_of_doors[i][0]
    #convert all the values in Number_of_doors to int
    integer_door.append(int(Number_of_doors[i]))
print(integer_door)

#findidng the average of integer_door.
average = sum(integer_door) / len(integer_door)
print(average)

