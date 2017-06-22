#!/bin/bash 

array2=( one two three ) 
echo ${array2[0]} 
echo ${array2[2]} 

read -a array4 
for i in "${array4[@]}" 
do 
echo $i 
done 


i=0
while read line
do
    array[ $i ]="$line"        
    (( i++ ))
done < <(ls -ls)

echo ${array[2]}

files=(*.sh)

for i in "${files[@]}" 
	do 
	echo $i 
	done 
