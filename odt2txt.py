import sys, zipfile
myfile = zipfile.ZipFile("E:\\abhishek\\odfpy-master\\odfpy-master\\samples\\Bluff Crag.odt")
listoffiles = myfile.infolist()
for s in listoffiles:
    print(s.orig_filename)
    if(s.orig_filename=="content.xml"):
        print("found")
        f=open("odt2txt.txt","wb")
        text=myfile.read(s.orig_filename)
        print(type(text))
        f.write(text)
        f.close()

f=open("E:\\abhishek\\odfpy-master\\odfpy-master\\odt2txt.txt","r")
text=f.read()
getText=False
res=""
for i in range(0,len(text)):
    if(text[i]=='<'):
        getText=False
    elif(text[
        i]=='>'):
        getText=True
    if(getText==True and text[i]!='>'):
        res=res+text[i]
#print(res)
res2=""
getText=True
for i in range(0,len(res)):
    if(res[i]=='&'):
        getText=False
    elif(res[i]==';'):
        getText=True
    if(getText==True and res[i]!=';'):
        res2=res2+res[i]


print(res2)
res_file=open("E:\\python\\result.txt","w")
res_file.write(res2)
f.close()
res_file.close()