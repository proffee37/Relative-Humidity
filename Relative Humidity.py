'''You are making a Relative Humidity Calculator! You will make modules and functions for each part of this Program.

Q: Make a Program named “YourName’s Weather Forecast”. It will show the user a welcome message. Then asks the User’s name. Then Addressing his name, your
program will ask the user about the region you stay in. Then it will ask for the temperature in degrees Celsius, and Dew Point in degrees Celsius. Make the
program such, so that the user can compare the Relative Humidity in as many regions as he/she wants. It will show the user, which region has the highest and the 
lowest Relative Humidity of all inputs. It also should show the sequence from low humidity to high humidity. If the user does not want to compare, he/she can
calculate RH for only one region. You can also make the program more user friendly, by taking input from any unit (Celsius or Fahrenheit). 

বাংলাঃ “YourName’s Weather Forecast” নামে একটি প্রোগ্রাম তৈরি করুন। এটি ব্যবহারকারীকে একটি স্বাগত বার্তা দেখাবে। তারপর ব্যবহারকারীর নাম জিজ্ঞাসা করুন। তারপর তার নাম সম্বোধন করে, 
আপনার প্রোগ্রাম ব্যবহারকারী যে অঞ্চলে থাকবেন সে সম্পর্কে জিজ্ঞাসা করবে। তারপর এটি ডিগ্রি সেলসিয়াসে তাপমাত্রা, ডিগ্রি সেলসিয়াসে শিশির বিন্দু জিজ্ঞাসা করবে। প্রোগ্রামটি এমনভাবে তৈরি করুন, যাতে ব্যবহারকারী যতগুলি অঞ্চল চান, আপেক্ষিক আর্দ্রতার তুলনা করতে পারেন। 
এটি ব্যবহারকারীকে দেখাবে, কোন অঞ্চলে সমস্ত ইনপুটগুলির মধ্যে সর্বোচ্চ এবং সর্বনিম্ন আপেক্ষিক আর্দ্রতা রয়েছে৷ এটি কম আর্দ্রতা থেকে উচ্চ আর্দ্রতা পর্যন্ত ক্রম দেখাতে সক্ষম হবে। ব্যবহারকারী যদি তুলনা করতে না চান, 
তবে তিনি শুধুমাত্র একটি অঞ্চলের জন্য RH গণনা করতে পারেন। আপনি যেকোন ইউনিট (সেলসিয়াস বা ফারেনহাইট) ইনপুট নিয়ে প্রোগ্রামটিকে আরও ব্যবহারকারী বান্ধব করে তুলতে পারেন।

The formula for Relative Humidity: Given as an attachment 

Hints to Use exp(): 

Python number method exp() returns exponential of x: e^x'''

# import necessary module
from datetime import datetime
import math
# Introductory message
print('Musfiqur’s Weather Forecast,', datetime.date(datetime.now()))
print('Welcome to today\'s weather forecast')
name=input('What is your name? ')
# Welcome message
print('Hello,', name, ', Hope you are feeling good!')
# Function for relative humidity calculation
def RH(T,D):
    humid = (math.exp(17.625*D/(243.04+D)))/(math.exp(17.625*T/(243.04+T)))
    rhumid= 100*humid
    return round(rhumid)
# Function for Temperature conversion from Fahrenheit to degree celsius
def converted(temp):
    C = 5/9 * (temp - 32)
    return(C)
# Creating list for storing user inputs
arealist = []
humiditylist = []
# initialization of some variables
n = 1
count = 1
# Loop for taking user input and relative humidity calculation
while n != 0:
    # user input of region
    if count == 1:
        region=input('Where are you from? ')
    else:
        region=input('What is the name of area, you want to know relative humidity? ')
    # user input of temperature & unit
    normT=int(input('What is the temperature in ' + region +' today: '))
    unit_1 = input('What is the unit of the temperature? Type C for Degree celsius and F for degree fahrenheit:')
    if unit_1 != 'F' and unit_1 != 'C':
        unit_1 = input('Please type, F/C!')
    dewT=int(input('What is the dew point temperature in ' + region +' today: '))
    unit_2 = input('What is the unit of the dew point temperature? Type C for Degree celsius and F for degree fahrenheit:')
    if unit_2 != 'F' and unit_2 != 'C':
        unit_2 = input('Please type, F/C!')
    # Checking whether temperature unit change is necessary
    if unit_1 == 'F':
        normT = converted(normT)
    if unit_2 == 'F':
        dewT = converted(dewT)  
    # Calculation of relative humidity
    relative = RH(normT,dewT)
    # Showing relative humidity of the region
    print('Relative Humidity of', region,':',relative)
    # Appending relative humidity in the list incase user is interested more than one area
    arealist.append(region)
    humiditylist.append(relative)
    # Asking question whether user want to know relative humidity of any other area
    Q=input('Do you want to know relative humidity of any other area, y/n ?')
    if Q != 'y' and Q != 'n':
        Q=input('Please type, y/n!')
    if Q == 'y':
        count += 1 
        continue
    else:
        break
# Creating list for sorting relative humidity of different regions
new_area = [] 
new_humidity = []
# Function for sorting relative humidity
def sorted(area,humidity,count):
    for i in range(count):
        minvalue = min(humidity)
        minposition = humidity.index(min(humidity))
        new_area.append(area[minposition])
        new_humidity.append(minvalue)
        area.remove(area[minposition])
        humidity.remove(minvalue)        
# Printing maximum, minimum and ascending order relative humidity and coresponding area       
if count != 1:
    maxposition= humiditylist.index(max(humiditylist))
    print('Maximum relative humidity: ', humiditylist[maxposition], '(', arealist[maxposition], ')')
    
    minposition= humiditylist.index(min(humiditylist))
    print('Minimum relative humidity: ', humiditylist[minposition], '(', arealist[minposition], ')')
    sorted(arealist,humiditylist,count)  
    print('The following list shows minimum to maximum relative humidity among the regions:')
    print(new_area,new_humidity)
# Concluding message
print('Thank you for using Musfiqur’s Weather Forecast ')





