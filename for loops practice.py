#Lists and for loops


stones = ['black', 'white','brown']
for x in stones:
    print(x)

flowers = ['rose', 'lotus']
for x in flowers:
    print(x)



numbers = [2,4,6, 8, 9]
squares=[]
for x in numbers:
    square= x**2
    squares.append(square)
    print(squares)


scores = [4,5,6]
squares =[]
for x in scores:
    square= x**3
    squares.append(square)
    print(squares)


scores =[4,5,6,7,8,9]
copy_of_scores = []
for x in scores:
    copy=x
    copy_of_scores.append(copy)
    print(copy_of_scores)
    print(scores)


scores = [4, 6, 7,8,9,10]
newscores = []
triplescores=[]
fourthyear_scores=[]
for x in scores:
    new=x+50
    triple=x*3
    quad=x*4
    newscores.append(triple)
    newscores.append(new)
    fourthyear_scores.append(quad)
    print(newscores)
    print(triplescores)
    print(fourthyear_scores)

for i in range(1, 6,3 ):

    print(i)




aces=['apple', 'orange','Mango']
for loop in aces:

    print(loop)

for loop in range(1,9,3):

    print(loop)

Juniors=[]

for grades in Juniors:
    grades=input('Please enter English grade ')
    print(grades)


names =[]
for i in range(1):
    name=input('please enter your name: ')
    age=input('plese enter your age: ')
    sex=input('please enter your sex: ')
    religion=input('please enter your religion: ')
    names.append(name)
    names.append(age)
    names.append(sex)
    names.append(religion)
    print('Entered values are: ',names)








