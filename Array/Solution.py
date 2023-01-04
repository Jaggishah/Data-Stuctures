# Let us say your expense for every month are listed below,
# January - 2200
# February - 2350
# March - 2600
# April - 2130
# May - 2190
a = [2200, 2350 , 2600 , 2130 ,2190]

# 1. In Feb, how many dollars you spent extra compare to January?
print(a[1]-a[0])

# 2. Find out your total expense in first quarter (first three months) of the year.
print(a[0]+a[1]+a[2])

# 3. Find out if you spent exactly 2000 dollars in any month
for i in a:
    if i == 2000:
        print(i , ": This is " , a.index(i) , "Element")
    if a.index(i) == len(a)-1 and i != 2000:
    
        print("Nothing")


# 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
a.append(1980)
print(a)

# 5. You returned an item that you bought in a month of April and
# got a refund of 200$. Make a correction to your monthly expense list
# based on this

print("April Cost Now :" , a[3]-200)