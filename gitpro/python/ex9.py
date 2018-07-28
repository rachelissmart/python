from sys import argv
script,textfile1,textfile2=argv
text1=open(textfile1)
text2=open(textfile1,'a+')

text1_content=text1.read()
text2.write(text1_content)
text2.seek(0) #start from the beginning again

print text2.read()

