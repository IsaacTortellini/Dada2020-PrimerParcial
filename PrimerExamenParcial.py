#Reyes Sánchez Daniel Isaac
# Primer Examen Parcial Diseño y Analisis de Algoritmos        
a=[1,2,3,4,5,6]
b=[9,12,3,0,1,4]
c=[10,11,3]
conta=1
n=3
for i in range(n):
    conta=i
    if conta==0:
     n=2
     print("Los numeros pertenecientes al arreglo ",a)
     print("que son divisibles entre ",n)
     print ("Son los siguientes:")
     for i in range(len(a)):
             if a[i]%n==0 and a[i]>0:
                 print ("",a[i])
    else:
        if conta==1:
         n=3
         print("Los numeros pertenecientes al arreglo ",b)
         print("que son divisibles entre ",n)
         print ("Son los siguientes:")
         for i in range(len(b)):
                 if b[i]%n==0 and b[i]>0:
                     print ("",b[i])
        else:
            if conta==2:
             n=1
             print("Los numeros pertenecientes al arreglo ",c)
             print("que son divisibles entre ",n)
             print ("Son los siguientes:")
             for i in range(len(c)):
                       if c[i]%n==0 and c[i]>0:
                          print ("",c[i]) 


   


           




