# name=input('Enter The Name');
# print('My name is'+name);

# first_name=input("Enter The first name");
# print('My First Name is '+first_name);

# middle_name=input("Enter The Middle Name ");
# print('My Middle Name is'+middle_name);

# Full_name=input("Enter The Full Name");
# print("My Full Name is "+Full_name);

##Controls Structure
'''
1.Seqential Control
2.Selection Control
3.Iterative Control
'''

##Sequential Control
var_1=int(input('Enter a integer value'));
if var_1<10:
    print('Values is less than 10');
else:
    print('Value is greater than 10');


##Multiway Selection



##This Program to check the student got  passing marks or not
var=0;
while var<10:
    var=var+1;
    print('I am working as a software Enginner')

marks=int(input("Enter Your marks in  mathematics"));
if marks>=35:
    print("You got passing grades");
    print("Thank You");
elif marks==100:
    print('You have got Perfect Score')
else :
    print("Sorry you got failling grade");
    print("Thank You");

##=>nested if
name="Abu Al Shahriar Rifat";
clg="University Of Sharda";
marks=56;
if clg=='University of Sharda':
    if name=='Abu Al Shahriar Rifat': print('My Name is'+name+'And My Universityn name is '+clg);
##=>elif header
x=20
y=45
z=64
if x>y and x>z:print(x);
elif y>x and y>z:print(y);
else:print(z);
##Iterative Control

##for loope Statement
##1
i=1
for i in range(1,6):
    print(i,'I am a Software Enginner at Google');
##2
for letter in "python":
    print("character is",letter);
##3
for letter in [10,20,30,40,50]:
    print(letter);
    
rifat=[10,20,30,40,50,60,70,80,90];
for index in rifat:
    print(index);
##4
for letter in [10,20,30,40]:
    if letter >=25:
        print(letter,"is greater than 25");
    else:
        print(letter," is less than 25");
##while loope Statement
##example-1
count=1
while count <=5:
    print(count);
    count=count+1
print("Good Bye");

##Infinite loope
# while count<=6:
#     print(count);

##This is the example for break statement

##break
count=0;
while count<5:
    if count==3:
        break;
    else:
        print(count);
        count=count+1;
print('Thank You');


##break
for letter in "Abu Al Shahriar Rifat":
    if letter=='S':
        break;
    else:
        print(letter);
print(letter);


##Continue
stringIs="I am a Full stack web application Developer";
for i in stringIs:
    if i=='F':
        continue;
    else:
        print(i);
        print('Thank You');

var=10
while var>0:
    var=var-1
    if var==3:
        continue;
    print(var);
print('Thank You');


'''
List:
1.Mutable
2.Linear Data Structure 
3.Mixed Type Elements
4.Variable Length
5.Zero Based Indexing
'''
animals=[];
print(animals);
animals=['dog','cat','monkey'];
print(animals[0]);
print(animals[1]);
print(animals[2]);
list1=[10,20,30,4,'Rifat',54];
print(list1);
list2=[10,20,30,40,50,60];
list3=[[10,20,30],[40,50,60]];
print(list3[0])
print(list3[0][0]);

