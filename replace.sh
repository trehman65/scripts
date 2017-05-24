files=(*.csv)


for i in "${files[@]}" 
	do 
	echo $i 
	sed -ie 's/ITEM_1/CATALOG ITEM #/g' $i
	sed -ie 's/ITEM_2/MANUF CODE #/g' $i
	sed -ie 's/DESC_1/DESCRIPTION/g' $i
	sed -ie 's/DESC_2/CUSTOMER ITEM #/g' $i
	sed -ie 's/EXT PRICE/EXTENDED PRICE/g' $i
	
	done 

