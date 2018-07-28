from sys import argv
script,textfile=argv
text=open(textfile,'w')
line1="My nane is Tu Ning."
line2="I am 34."
line3="I like teaching."
text.write(line1)
text.write("\n")
text.write(line2)
text.write("\n")
text.write(line3)
text.write("\n")
text.close()
