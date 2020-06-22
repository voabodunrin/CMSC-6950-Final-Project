import argparse
import matplotlib.pyplot as plt
import numpy as np
import csv
import requests
import string

#example of command line entry->
#python q5_proj.py "Nova Scotia" "deaths" "20-03-2020"
#date MUST be in form "dd-mm-yyyy"


#calculates the doubling rate given arguments:
#province, specification of num. cases or deaths,  and a date (3 arguments)

#returns doubling rate- number of days that it will take to double # cases/deaths, given current rate of spread
#use data from 1 week before date to calc. doubling time


dt=2 #can change if desired-> currently 1 week dt for formula
orig_dt=dt #for later
#use argparse for command line program
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

#dictionary for days in each month
length_dict = { "01": 31,"02": 29,"03": 31,  "04": 30, "05": 31,"06": 30,"07": 31}

args.prov=args.prov.replace('-',' ') #reintroduce space


if args.typ=='cases':
    col_index=4 #case column
elif args.typ=='deaths':
    col_index=6 #death column
else:
    print("specify either 'cases' or 'deaths', right now is", args.typ)


P1="" #initialize
        
if int(args.t2[0:2])>=dt+1: #just subtract 7 to get a week before
    t1=str(int(args.t2[0:2])-dt).zfill(2)+args.t2[2:]
else:
    #use length of previous month to calculate 1 week before t2
    t1=str( length_dict.get(  (str(int(args.t2[3:5])-1)).zfill(2)     )  -(dt-int(args.t2[0:2])))+'-'+ str(int(args.t2[3:5])-1).zfill(2)+ args.t2[5:]


for row in data:
   # print(args.t2==row[3])
    if row[1]==args.prov and row[3]==args.t2:
      #  print("yes")
        P2=row[col_index]  #number cases/deaths corresponding to t_2 (inputted date)
       # print(P2)
    elif row[1]==args.prov and row[3]==t1:
        P1=row[col_index]  #number cases/deaths corresponding to t_1 (inputted date)

while (P1=="" or P1==P2) and dt<=30+orig_dt: #if P1 hasn't been assigned (no data for dt before t2)
    #note: if we are at the beginning of data, maybe no earlier data has been recorded. In this case, dt<=30 loop will stop this after ~a month before recorded data
    #if P1=P2, will be dividing by 0. Keep going back until P2>P1
    dt=dt+1 #larger dt
        #new t1- calc in similar manner
    if int(args.t2[0:2])>=dt+1:
        #reformulate t1
        t1=str(int(args.t2[0:2])-dt).zfill(2)+args.t2[2:]
    else:
        #note: lots of integer/string converting needed to evaluate dates
        #zfill will add leading zeros if necessary 
        t1=str( length_dict.get(  (str(int(args.t2[3:5])-1)).zfill(2)     )  -(dt-int(args.t2[0:2])))+'-'+ str(int(args.t2[3:5])-1).zfill(2)+ args.t2[5:]
        
    for row in data:
        if row[1]==args.prov and row[3]==t1:
            P1=row[col_index]  #number cases/deaths corresponding to t_2 (inputted date)
    #reruns if P1 hasnt been assigned

if P1!="" and P1!=P2 and float(P1)!=0: #cant calculate doubling time if P1=0
    doubling_rate=((dt)*np.log(2))/(np.log(float(P2)/float(P1))) #formula for doubling time
    print(args.prov,',',args.t2,',',doubling_rate)
#SO IF still no date 1 to go off of (no earlier recorded data for that province)-> no output
    
#print output -> will load into file for plotting 
#have a deaths file and case file (done in shell script)
