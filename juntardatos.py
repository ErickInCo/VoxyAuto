n=184
archi1=open("resultados.txt","w", encoding="utf-8")
for x in range(1,n+1):
    nombrearchivo="RESULTADOS\RESPUESTA_SAT_RFC ("+str(x)+").txt"
    print(nombrearchivo)
    f = open(nombrearchivo)
    datos=f.readlines()
    f.close()
    for y in datos:
        if y.find("facturas") >=0:
            archi1.write(y)
archi1.close()
        