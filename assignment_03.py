#Q.1- Create a list with user defined inputs.
#>Answer 1
list1=[]
n=int(input("Enter how much integers you want in list\n"))
print("Enter elements")
for i in range(n):
    a=int(input())
    list1.append(a)
print(list1)

#Q.2 Add ['google','apple',''facebook','microsoft','tesla'] to above created list
#>Answer 2
list2=['google','apple','facebook','microsoft','tesla']
list1.extend(list2)
print(list1)

#Question 3
#Answer 3
list3=[1,1,2,3,6,4,6,3,6,4,6,5,6,3,6,6,2,3,3]
print(list3.count(6))


#Q.4 Create a list with numbers and sort it in ascending order.
#>Answer 4
list4 = [90,82,45,100,902,707,245]
list4.sort()
print(list2)

#Q.5 Merge two 1-d arrays A and B into single array C in ascending order.
#>Answer 5
x=[1,3,9,-11,7,8,104]
y=[6,4,25,3,46,56,353,213]
z=[121,34,51]
x.sort() 
y.sort() 
z.sort() 
x.extend(y)
y.extend(x) 
z.sort() 
print(z)

#Q.6 - Count even and odd numbers in that list.
#>Answer 6
odd=[]
even=[]
for d in z:
    if d%2==0:
        even.append(d)
    else:
        odd.append(d)

print ("even numbers are ",len(even))

#Q.7 Reverse a tuple in python
#>Answer 7
tuple = (1,2,3,4,5)
print(tuple[::-1])
print ("odd numbers are ",len(odd))

#Tuples
#Q.8 To find largest and smallest element of tuple
#>Answer 8
tup = (100,112,50,30,115,110,20)
print("Maximum vaue of tuple is: ",max(tup))
print("Minimum vallue of tuple is: ",min(tup))

#Strings
#Q.9 Convert string into uppercase
#>Answer 9
str = input("Enter any string in lowercase:  ")
print("Lowercase: ",str)
print("Uppercase: ",str.upper())

#Q.10  Print true if string contains all numeric characters
#>Answer 10
str1 = input("Enter string: ")
print(str1.isdigit())

#Q.11 Replace the word "World" with your name in the string "Hello World"
#>Answer 11
string = "Hello World"
print(string.replace('World','SAURAV'))
