def metercode ():
  noerror = 0
  while noerror == 0 :
    try:
      meter = int (input ('Enter 1 for Centieter/Kilogram\nEnter 2 for Inch/Pound\n'))
      if meter == 1: noerror = 1
      if meter == 2: noerror = 1
    except: continue
  return meter

meter = metercode ()
if meter == 1: numset = ['Centimeter', 'Kilogram', 10000]
if meter == 2: numset = ['Inch', 'Pound', 703]

bmi = 0

while bmi == 0:
  try:
    para1 = float (input ( ' Please enter your height in %s\n' %numset[0]))
    para2 = float (input ( ' Please enter your weigth in %s\n' %numset[1]))
    numset [0] = para1
    numset [1] = para2
    bmi = numset [1] * numset [2] / (numset [0]**2)
    print ('Your BMI is: ', bmi)
  except: 
    print ('error')
    metercode()
    
if bmi < 18.5: print ('Underweight')
elif bmi < 23: print ('Healthy')
elif bmi < 25: print ('Overweight')
elif bmi < 30: print ('Moderately Obese')
elif bmi < 35: print ('Severly Obese')
else: print ('Very Severly Obese')

from time import sleep
sleep(10)