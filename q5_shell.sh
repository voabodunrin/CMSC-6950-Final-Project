#shell script runs the code q5_proj from the command line multiple times- loops over provinces and dates
#outputs results into .dat files

declare -a dates=( '01-03-2020' '03-03-2020' '05-03-2020' '07-03-2020' '09-03-2020' '11-03-2020' '13-03-2020''15-03-2020' '17-03-2020' '19-03-2020' '21-03-2020' '23-03-2020' '25-03-2020' '27-03-2020' '29-03-2020' '31-03-2020' '02-04-2020' '04-04-2020' '06-04-2020' '08-04-2020' '10-04-2020' '12-04-2020' '14-04-2020' '16-04-2020' '18-04-2020' '20-04-2020' '22-04-2020' '24-04-2020' '26-04-2020' '28-04-2020' '30-04-2020' '02-05-2020' '04-05-2020' '06-05-2020' '08-05-2020' '10-05-2020' '12-05-2020''14-05-2020' '16-05-2020' '18-05-2020' '20-05-2020' '22-05-2020' '24-05-2020' '26-05-2020' '28-05-2020' '30-05-2020' '01-06-2020' '03-06-2020' '05-06-2020' '07-06-2020' '09-06-2020' '11-06-2020' '13-06-2020' '15-06-2020' '17-06-2020' '19-06-2020' '21-06-2020')
declare -a provs=('Canada' 'Quebec' 'Ontario' 'Alberta' 'British-Columbia' 'Nova-Scotia' 'Saskatchewan' 'Manitoba' 'Newfoundland-and-Labrador' 'New-Brunswick' 'Prince-Edward-Island' 'Yukon' 'Northwest-Territories' 'Nunavut')

for i in "${provs[@]}"
do
for j in "${dates[@]}"
 
do
#run python file- output into .dat file 
python q5_proj.py $i 'cases' $j 
python q5_proj.py $i 'deaths' $j 
done
done 

