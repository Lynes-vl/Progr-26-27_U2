def hora(s):
    fin=f"{s//3600}h"
    print(fin)

def minuto(s):
    fin=f"{(s%3600)//60}min"
    print(fin)

def segundosAtiempoExacto(s):
    fin=""
    if (s//3600)>0:
        fin=f"{s//3600}h "
    if ((s%3600)//60)>0:
        fin+=f"{(s%3600)//60}min "
    if ((s%3600)%60)>0:
        fin+=f"{(s%3600)%60}s"
    print(fin)

def segundosAtiempo(s):
    print(f"{s//3600}h {(s%3600)//60}min {(s%3600)%60}s")

segundosAtiempoExacto(int(input("Dame los s que pasar a h,min y s simples: ")))
segundosAtiempo(int(input("Dame los s que pasar a h,min y s con 0: ")))