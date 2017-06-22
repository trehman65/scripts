import sys 
import random

questions = open('nust.txt')
outfile = open('nustformatted.txt','w')
optlabel = ['a. ','b. ','c. ','d. ']
optindex = [0,1,2,3]
options=[]
answerkey = open("answerkey.txt",'w')


prevLine = ""
index=0

for line in questions:

	if (len(line)>1):
		
		if (line == prevLine):
			answerkey.write(str(index/5 +1) + " - "+ line)
			continue


		if(index%5==0):
			

			print line 

			random.shuffle(optindex)		
			
			if(index!=0):
				outfile.write("	"+optlabel[0]+options[optindex[0]])
				outfile.write("	"+optlabel[1]+options[optindex[1]])
				outfile.write("	"+optlabel[2]+options[optindex[2]])
				outfile.write("	"+optlabel[3]+options[optindex[3]])
				outfile.write('\n')

				
				options=[]

			outfile.write(str(index/5 + 1)+ " - " +line)

		else:
			options.append(line)

						


		prevLine = line
		index=index+1

