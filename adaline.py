# Title: Adaline model for only a pair of inputs and its targeted output
# Author: Md. Abdul Haq
# Date: 12th February,2020

# This is the Adaptive Linear element (Adaline) model which was proposed by Widrow heff in 1960.

# This code generates output with respect to only one case at a time i.e., "(x1,x2)" are the inputs which produce a
# targeted output "t".

# In this code if you want to assign your own weights then you can do it when the output window shows do you want to
# change weights.

# You can cross verify you weights to check if the new weights are satisfying the whole functional bi-polar table


global x1, x2, t, w1_old, w2_old, b, a, th_val, net_input, activation_function, y, w1_new, w2_new, b_new
x1 = int(input('Enter an element x1 : '))
x2 = int(input('Enter an elements x2: '))
t = int(input('Enter a targeted output : '))
user_input = input('Do you want to enter weights?(Y/N) ')
if user_input == "Y" or "y":
    b = int(input('Enter base b weight : '))
    w1_old = int(input('Assign first weight : '))
    w2_old = int(input('Assign second weight : '))
else:
    b = 0
    w1_old = 0
    w2_old = 0
th_val = int(input('Enter threshold value = '))

print('First input= ', x1)
print('Second input= ', x2)
print('Targeted output= ', t)
print('Assigned weights= ', b, w1_old, w2_old)
print('Threshold value= ', th_val)
x = x1*w1_old
y = x2*w2_old
net_input = b + x + y
print('net input =', net_input)
if net_input >= th_val:
    activation_function = 1  # f(net_input) = 1
else:
    activation_function = -1  # f(net_input) = -1

y = activation_function
print('Activation function =', y)
print('Checking if y=t')
if y == t:
    print(' Checked and no need to change/update weights')
else:
    print('Checked and need to change/update weights')
    a = int(input("Enter learning rate : "))
    m = t - net_input
    w1_new = w1_old + a * m * x1
    w2_new = w2_old + a * m * x2
    b_new = b + a * m
    print('New weights', b_new, w1_new, w2_new)

