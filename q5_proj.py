import argparse
import matplotlib.pyplot as plt
import numpy as np
import csv
import requests
import string
import datetime

#example of command line entry->
#python q5_proj.py "Nova-Scotia" "deaths" "20-03-2020"
#date MUST be in form "dd-mm-yyyy" and any spaces in province must be rpelaced with hyphens


#province, specification of num. cases or deaths,  and a date (3 arguments)

#returns doubling rate- number of days that it will take to double # cases/deaths, given current rate of spread
#province, specification of num. cases or deaths,  and a date (3 arguments)


#use argparse for command line program (3 inputs)
parser = argparse.ArgumentParser()
parser.add_argument("prov", help="province name",
                    type=str)
parser.add_argument("typ", help="either cases or deaths",
                    type=str)
parser.add_argument("t2", help="given date",
                    type=str) 
args = parser.parse_args()

#download data from url
csv_url = 'https://health-infobase.canada.ca/src/data/covidLive/covid19.csv'
req = requests.get(csv_url)
url_content = req.content
csv_file = open('covid19.csv', 'wb')
csv_file.write(url_content)
csv_file.close()
#put data into list
with open("covid19.csv","r") as file:
    data=list(csv.reader(file)) #noe refer to covid.csv as data

args.prov=args.prov.replace('-',' ') #reintroduce spaces

if args.typ=='cases':
    col_index=4 #case column
elif args.typ=='deaths':
    col_index=6 #death column
else:
    print("please specify either 'cases' or 'deaths', right now is", args.typ)

#initialize
P1="" 
P2=""
for row in data:
    if row[1]==args.prov and float(row[col_index])!=0.0:
        t1=row[3]
        P1=row[col_index]
        break  #returns date of first non zero case/death day & cases/deaths on that day

for row in data:
   # print(args.t2==row[3])
    if row[1]==args.prov and row[3]==args.t2:
      #  print("yes")
        P2=row[col_index]  #number cases/deaths corresponding to t_2 (inputted date)

if P1!="" and P2!="" and P1!=P2 and float(P1)!=0: #cant calculate doubling time in these cases (division by zero)
    #calculate difference between dates
    t2=datetime.datetime.strptime(args.t2, '%d-%m-%Y')
    t1=datetime.datetime.strptime(t1, '%d-%m-%Y')
    delta=t2-t1
    #return integer day difference
    dt=delta.days
    if float(P2)==0:
        doubling_rate=0
    else: 
        doubling_rate=((dt)*np.log(2))/(np.log(float(P2)/float(P1))) #formula for doubling time

    print(args.prov,',',args.t2,',',doubling_rate)
#SO if still no date 1 to go off of (no earlier recorded data for that province)-> no output
    
#print output -> will load into file for plotting 
#have a deaths file and case file (done in shell script)
