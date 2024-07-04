import os
os.system("cls")

while True:

    try:
        
        op=int(input("1.grabar  2.buscar  3.imprimir certificados  4.salir"))
        
    except:
        
        op=0

    if op ==1 :
        
        print("elegiste grabar")
        
        nombre=input("ingrese nombre")
        
        if nombre == "" :
            
            print("nombre invalido")
            
        else:
            print("nombre aceptado")
            
            apellido=input("ingrese apellido")
            
            if apellido == "" :
                
                print("apellido invalido")
                
            else:
                print("apellido aceptado")
                
                edad=int(input("ingrese edad"))
                
                if edad >=0 :
                    
                    print("edad aceptada")
                    
                    nifnum=int(input("ingrese numerales del nif sin guion(-) y sin caracteres finales"))
                    
                    if nifnum <8 and nifnum >8:
                        
                        print("nif invalido")
                    
                    else:
                        print("numerales aceptados")
                        
                        #se supone que aca seguia la validacion se me olvido como medir la longuitud de los caracteres y validar que terminara en sp 
                    
                else:
                    
                    print("edad invalida")
        
    elif op==2 :
        
        print("elegiste buscar")
        
        #solo implemente los digitos del nif ya que olvide como validarlos
     
        nif=input("ingrese nif")
        
        if nif==nifnum:
            print("nif invalido")
        else:
            print("nombre: ",nombre,"apellido: ",apellido,"edad: ",edad)
        
    elif op ==3 :
        
        print("elegiste imprimir certificados")
        
        print("esta opcion esta en mantenimiento")
        
        print("chamuyo nomas profe no llegue hasta aqui")
        
    else:
        
        
        print("adios")
        
        break
    