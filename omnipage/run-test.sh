files=(*.JPG)

for i in "${files[@]}" 
	do 
	
	echo $i 
	rm /home/ubuntu/Omni/table.png
	cp $i /home/ubuntu/Omni/table.png
	cd /home/ubuntu/Omni
	convert table.png -density 300 table.png
	./sample -x 49
	cp out.txt /home/ubuntu/Omni/output/$i.txt
	
	cd /home/ubuntu/Omni/dataA
	
	done 


