f = open ("cp.txt", encoding='utf-8')
cp =f.readlines()
f.close()
f = open("nuevainfo.txt", encoding="utf-8")
datos=f.readlines()
f.close()

archivodeN= open("nombresdearchivos.txt","w")
id=0
for x in cp:
    nombre=x[0:5]+"cp.txt"
    archivodeN.write(nombre+"\n")
    archi1=open(nombre,"w", encoding="utf-8") 
    for y in datos:
        datos2=y.split("|")
        cadena=datos2[0]+"|"+datos2[1]+"|"+datos2[2]+"|"+str(x[0:5])+"\n"
        archi1.write(cadena)
    archi1.close()
archivodeN.close()

