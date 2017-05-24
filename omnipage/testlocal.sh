files=(*.png)

for i in "${files[@]}" 
	do 
	echo $i 
	cp -a $i ~/Desktop/table.png ~/Desktop/handwritten/alpha.png
	cp out.txt ~/Desktop/Output/$i.txt 
	done 


