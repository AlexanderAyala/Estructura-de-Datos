#!/usr/bin/env python
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
import csv
#import sys
#sys.setrecursionlimit(100)

carrera_arq = []
carrera_civil = []
carrera_anest = []
carrera_lic_soc = []
carrera_doc_medic = []
carrera_cie_jur = []
carrera_cie_ed = []
carrera_adm_emp = []
carrera_fisio = []
carrera_conta = []
carrera_ing_ind = []
carrera_lic_merca = []
carrera_lic_mat = []
carrera_prof_mat = []
carrera_lic_fran_ing = []
carrera_lic_quim_far = []
carrera_lic_bio = []
carrera_lic_psico = []
carrera_lic_lab_clin = []
carrera_prof_ed_basica = []
carrera_prof_cie_soc = []
carrera_ing_sis = []
carrera_lic_letras = []
carrera_esp_med_gine = []
carrera_ing_agro = []
carrera_prof_ed_parv = []
carrera_ing_meca = []
carrera_lic_fisica = []
carrera_prof_ingles = []
carrera_ing_elec = []
carrera_maest_admon_fin = []
carrera_lic_econo = []
carrera_lic_cie_quim = []
carrera_maest_profe_doce = []
carrera_maestr_salud = []
carrera_prof_bio = []
carrera_maestr_gest_amb = []
carrera_maestr_inv_social = []
carrera_prof_quim = []
carrera_lic_ed_parv = []
carrera_esp_med_pediat = []
carrera_prof_fisica = []


while True:
    print"Selecione una opcion"
    print"1- Mostrar cantidad de registros clasificados (Masculino / Femenino)"
    print"2- Consulta por Nombre o Apellido"
    print"3- Cantidad de estudiantes por Carrera"
    print"4- Mostrar cantidad de datos Erroneos"
    print"5- Agregar registros"
    print"6- Ordenar por Orden Alfabetico (Burbuja -- por columnas)"
    print"7- Ordenar por Orden Alfabetico usando Quicksort eligiendo columna"
    print"8- **** Ordenar por Orden Alfabetico usando HEAPSORT *****"
    print"9- **** Estadisticas (Estudiantes -- Sexo/Carreras --)****"
    print"10- Salir"
    
    numeral = int(raw_input("Seleccione una opcion: "))
    
    if numeral == 1:
        fh = open('C:\Users\user\Desktop\ESTRUCTURA DE DATOS\zborrowers_test.csv')
        columna_sex = csv.reader(fh, delimiter = ",")
        sexo_numF = []
        sexo_numM = []
        for line  in columna_sex:
            sexo = line[4]
            if sexo == "M":
                sexo_numM.append(sexo)
            elif sexo == "F":
                sexo_numF.append(sexo)
        fh.close()
        print "El numero de estudiantes de sexo Femenino es:  ",len(sexo_numF)
        print "El numero de estudiantes de sexo Masculino es: ",len(sexo_numM)
        nextt = raw_input("Presione ENTER para continuar.....")
        print "\n"
        
    
    elif numeral ==2:
        print "a)- Busqueda Lineal"
        print "b)- Busqueda Secuencial"
        opciones = raw_input("seleccione un algoritmo de busqueda: ")
        if opciones == 'a' or opciones=='A':
            fh = open('/home/user/Escritorio/borrowers_test.csv')
            columna_apel = csv.reader(fh, delimiter = ",")
            
            apel=raw_input("Ingrese apellido completo: ")
            apel_search = []
            apel_count = []
            for line  in columna_apel:
                apellido = line[0]
                apel_search.append(apellido)
                if apellido == apel:
                    apel_count.append(apellido)
            fh.close()
            
            L = apel_search
            x = apel
            def linearSearch(L,x):
                for e in L:
                    if e == x.upper() or e== x.lower():
                        return " Existe"
                return " No existe"
                #print linearSearch(L,x)
            contar = (len(apel_count))
            if contar == 0:
                print "\n","El apellido "+apel + linearSearch(L,x) + " y tiene",(len(apel_count)), "coincidencias", "\n"
                nexxt=raw_input("Presione ENTER para continuar.......")
            else:
                print "\n","El apellido "+apel + linearSearch(L,x) + " y tiene",(len(apel_count)-1), "coincidencias", "\n"
                nexxt=raw_input("Presione ENTER para continuar.......")
        
        elif opciones == 'b' or 'B':
            fh = open('/home/user/Escritorio/borrowers_test.csv')
            columna_apel = csv.reader(fh, delimiter = ",")
            
            apel=raw_input("Ingrese apellidos: ")
            apel_search = []
            apel_count = []
            for line  in columna_apel:
                apellido = line[0]
                apel_search.append(apellido)
                if apellido == apel:
                    apel_count.append(apellido)
        
            fh.close()

            lista = apel_search
            buscar = apel

            posicion = 0
            encontrado = False
            posicion_valor_buscar=0

            for posicion in range(len(lista)):
                if lista[posicion] == buscar.lower() or lista[posicion] == buscar.upper():
                    posicion_valor_buscar= posicion
		    encontrado = True
	        posicion = posicion+1

            contar = (len(apel_count))
            if encontrado==True:
                if contar == 0:
                    print "\n", 'Valor ' + buscar+ ' encontrado en poscicion ', posicion_valor_buscar , " con",(len(apel_count)), "coincidencias", "\n"
                else:
                    print "\n", 'Valor ' + buscar+ ' encontrado en poscicion ', posicion_valor_buscar , " con",(len(apel_count)-1), "coincidencias", "\n"
            else:
                print "\n", 'Valor no encontrado',"\n"
            nextt = raw_input("Presione ENTER para continuar.....")
        
    elif numeral ==3:
        print "\n", "Listado de Carreras y respectiva cantidad de Estudiantes"
        fh = open('/home/user/Escritorio/borrowers_test.csv')
        columna_carr = csv.reader(fh, delimiter = ",")
        
        for line  in columna_carr:
                carrera = line[6]

	        if carrera == "Arquitectura":
	            carrera_arq.append(carrera)
	        elif carrera == "INGENIERIA CIVIL":
	            carrera_civil.append(carrera)
	        elif carrera == "Licenciatura en Anestesiología e Inhaloterapia":
	            carrera_anest.append(carrera)
	        elif carrera == "Licenciatura en Sociología":
	            carrera_lic_soc.append(carrera)
	        elif carrera == "Doctorado en Medicina":
	            carrera_doc_medic.append(carrera)
	        elif carrera == "Licenciatura en Ciencias Jurídicas":
	            carrera_cie_jur.append(carrera)
	        elif carrera == "Licenciatura en Ciencias de la Educación en la Especialidad de Primero y Segundo Ciclo de Educación Básica":
	            carrera_cie_ed.append(carrera)
	        elif carrera == "LICENCIATURA EN ADMINISTRACION DE EMPRESAS":
	            carrera_adm_emp.append(carrera)
	        elif carrera == "Licenciatura en Fisioterapia y Terapia Ocupacional":
	            carrera_fisio.append(carrera)
	        elif carrera == "Licenciatura en  Contaduría Pública":
	            carrera_conta.append(carrera)
	        elif carrera == "Ingeniería Industrial":
	            carrera_ing_ind.append(carrera)
	        elif carrera == "Licenciatura en Mercadeo Internacional":
	            carrera_lic_merca.append(carrera)
	        elif carrera == "Licenciatura en Matemática":
	            carrera_lic_mat.append(carrera)
	        elif carrera == "Profesorado en Matemática para Tercer Ciclo de Educación Básica y Educación Media":
	            carrera_prof_mat.append(carrera)
	        elif carrera == "Licenciatura en Lenguas Modernas Especialidad en Francés e Inglés":
	            carrera_lic_fran_ing.append(carrera)
	        elif carrera == "Licenciatura en Química y Farmacia":
	            carrera_lic_quim_far.append(carrera)
	        elif carrera == "Licenciatura en Biología":
	            carrera_lic_bio.append(carrera)
	        elif carrera == "LICENCIATURA EN PSICOLOGIA":
	            carrera_lic_psico.append(carrera)
	        elif carrera == "Licenciatura en Laboratorio Clínico":
	            carrera_lic_lab_clin.append(carrera)
	        elif carrera == "Profesorado en Educación Básica para Primero y Segundo Ciclos":
	            carrera_prof_ed_basica.append(carrera)
	        elif carrera == "Profesorado en Ciencias Sociales para Tercer Ciclo de Educación Básica y Educación Media":
	            carrera_prof_cie_soc.append(carrera)
	        elif carrera == "Ingeniería de Sistemas Informáticos":
	            carrera_ing_sis.append(carrera)
	        elif carrera == "Licenciatura en Letras":
	            carrera_lic_letras.append(carrera)
	        elif carrera == "Especialidad Médica en Ginecología y Obstetricia":
	            carrera_esp_med_gine.append(carrera)
	        elif carrera == "Ingeniería Agronómica":
	            carrera_ing_agro.append(carrera)
	        elif carrera == "Profesorado en Educación Inicial y Parvularia":
	            carrera_prof_ed_parv.append(carrera)
	        elif carrera == "Ingeniería Mecánica":
	            carrera_ing_meca.append(carrera)
	        elif carrera == "Licenciatura en Física":
	            carrera_lic_fisica.append(carrera)
	        elif carrera == "Profesorado en Idioma Inglés para Tercer Ciclo de Educación Básica y Educación Media":
	            carrera_prof_ingles.append(carrera)
	        elif carrera == "Ingeniería Eléctrica":
	            carrera_ing_elec.append(carrera)
	        elif carrera == "Maestría en Administración Financiera":
	            carrera_maest_admon_fin.append(carrera)
	        elif carrera == "Licenciatura en Economía":
	            carrera_lic_econo.append(carrera)
	        elif carrera == "Licenciatura en Ciencias Químicas":
	            carrera_lic_cie_quim.append(carrera)
	        elif carrera == "Maestría en Profesionalización de la Docencia Superior":
	            carrera_maest_profe_doce.append(carrera)
	        elif carrera == "Maestría en Salud Pública":
	            carrera_maestr_salud.append(carrera)
	        elif carrera == "Profesorado en Biología para Tercer Ciclo de Educación Básica y Educación Media":
	            carrera_prof_bio.append(carrera)
	        elif carrera == "Maestría en Gestión Ambiental":
	            carrera_maestr_gest_amb.append(carrera)
	        elif carrera == "Maestría en Métodos y Técnicas de Investigación Social":
	            carrera_maestr_inv_social.append(carrera)
	        elif carrera == "Profesorado en Química para Tercer Ciclo de Educación Básica y Educación Media":
	            carrera_prof_quim.append(carrera)
	        elif carrera == "Licenciatura en Educación Inicial y Parvularia":
	            carrera_lic_ed_parv.append(carrera)
	        elif carrera == "Especialidad Médica en Medicina Pediátrica":
	            carrera_esp_med_pediat.append(carrera)
	        elif carrera == "Profesorado en Física para Tercer Ciclo de Educación Básica y Educación Media":
	            carrera_prof_fisica.append(carrera)
	fh.close()
	
        print "\n", "Numero de estudiantes para Arquitectura: ",(len(carrera_arq))
        print "Numero de estudiantes para Ingenieria Civil: ",(len(carrera_civil))
        print "Numero de estudiantes para Licenciatura en Anestesiologia e Inhaloterapia: ", (len(carrera_anest))
        print "Numero de estudiantes para Licenciatura en Sociologia: ", (len(carrera_lic_soc))
        print "Numero de estudiantes para Doctorado en Medicina: ",(len(carrera_doc_medic))
        print "Numero de estudiantes para Licenciatura en Ciencias Juridicas: ",(len(carrera_cie_jur))
        print "Numero de estudiantes para Licenciatura en Ciencias de la Educacion en la Especialidad de Primero y Segundo Ciclo de Educación Básica: ",(len(carrera_cie_ed))
        print "Numero de estudiantes para Licenciatura en Administracion de empresas: ",(len(carrera_adm_emp))
        print "Numero de estudiantes para Licenciatura en Fisioterapia y Terapia Ocupacional: ",(len(carrera_fisio))
        print "Numero de estudiantes para Licenciatura en Contaduria Publica: ",(len(carrera_conta))
        print "Numero de estudiantes para Ingenieria Industrial: ",(len(carrera_ing_ind))
        print "Numero de estudiantes para Licenciatura en Mercadeo Internacional: ",(len(carrera_lic_merca))
        print "Numero de estudiantes para Licenciatura en Matematica: ",(len(carrera_lic_mat))
        print "Numero de estudiantes para Profesorado en Matematica para Tercer Ciclo de Educacion Basica y Educacion Media: ",(len(carrera_prof_mat))
        print "Numero de estudiantes para Licenciatura en Lenguas Modernas Especialidad en Frances e Ingles:",(len(carrera_lic_fran_ing))
        print "Numero de estudiantes para Licenciatura en Quimica y Farmacia: ",(len(carrera_lic_quim_far))
        print "Numero de estudiantes para Licenciatura en Biologia: ",(len(carrera_lic_bio))
        print "Numero de estudiantes para Licenciatura en Psicologia: ",(len(carrera_lic_psico))
        print "Numero de estudiantes para Licenciatura en Laboratorio Clinico: ",(len(carrera_lic_lab_clin))
        print "Numero de estudiantes para Profesorado en Educación Basica para Primero y Segundo Ciclos",(len(carrera_prof_ed_basica))
        print "Numero de estudiantes para Profesorado en Ciencias Sociales para Tercer Ciclo de Educacion Basica y Educacion Media",(len(carrera_prof_cie_soc))
        print "Numero de estudiantes para Ingenieria de Sistemas informaticos: ",(len(carrera_ing_sis))
        print "Numero de estudiantes para Licenciatura en Letras: ",(len(carrera_lic_letras))
        print "Numero de estudiantes para Especialidad Medica en Ginecologia y Obstetricia: ",(len(carrera_esp_med_gine))
        print "Numero de estudiantes para Ingenieria Agronomica: ",(len(carrera_ing_agro))
        print "Numero de estudiantes para Profesorado en Educacion Inicial y Parvularia: ",(len(carrera_prof_ed_parv))
        print "Numero de estudiantes para Ingenieria Mecanica: ",(len(carrera_ing_meca))
        print "Numero de estudiantes para Licenciatura en Fisica: ",(len(carrera_lic_fisica))
        print "Numero de estudiantes para Profesorado en Idioma Ingles para Tercer Ciclo de Educacion Basica y Educacion Media: ",(len(carrera_prof_ingles))
        print "Numero de estudiantes para Ingenieria Electrica: ",(len(carrera_ing_elec))
        print "Numero de estudiantes para Maestria en Administracion Financiera: ",(len(carrera_maest_admon_fin))
        print "Numero de estudiantes para Licenciatura en Economia: ",(len(carrera_lic_econo))
        print "Numero de estudiantes para Licenciatura en Ciencias Quimicas: ",(len(carrera_lic_cie_quim))
        print "Numero de estudiantes para Maestria en Profesionalizacion de la Docencia Superior: ",(len(carrera_maest_profe_doce))
        print "Numero de estudiantes para Maestria en Salud Publica: ",(len(carrera_maestr_salud))
        print "Numero de estudiantes para Profesorado en Biologia para Tercer Ciclo de Educacion Basica y Educacion Media: ",(len(carrera_prof_bio))
        print "Numero de estudiantes para Maestria en Gestion Ambiental: ",(len(carrera_maestr_gest_amb))
        print "Numero de estudiantes para Maestria en Metodos y Tecnicas de Investigacion Social: ",(len(carrera_maestr_inv_social))
        print "Numero de estudiantes para Profesorado en Quimica para Tercer Ciclo de Educacion Basica y Educacion Media: ",(len(carrera_prof_quim))
        print "Numero de estudiantes para Licenciatura en Educacion Inicial y Parvularia: ",(len(carrera_lic_ed_parv))
        print "Numero de estudiantes para Especialidad Medica en Medicina Pediatrica: ",(len(carrera_esp_med_pediat))
        print "Numero de estudiantes para Profesorado en Fisica para Tercer Ciclo de Educacion Basica y Educacion Media: ",(len(carrera_prof_fisica))
        nexxt=raw_input("Presione ENTER para continuar.......")
        print "\n"
    
    elif numeral ==4:
        fa = open('/home/user/Escritorio/borrowers_test.csv')
        columna_null = csv.reader(fa, delimiter = ",")
        
        Apel_null = []
        for line  in columna_null:
            apellido = line[1]
            if apellido == "NULL":
                Apel_null.append(apellido)
        fa.close()    
        print "El numero de Datos Nulos o Erroneos es: ", len(Apel_null)
        nextt = raw_input("Presione ENTER para continuar.....")
        print "\n"
        
    elif numeral ==5:
        
        nombre = raw_input("ingrese nombre: ")
        apellido = raw_input("ingrese apellido: ")
        cod_cat = raw_input("ingrese codigo de categoria: ")
        reg_fecha = raw_input("ingrese fecha de registro: ")
        sexo=raw_input("ingrese su sexo: ")
        cod_carrera = raw_input("ingrese el codigo de la carrera: ")
        nom_carrera = raw_input("ingrese el nombre de la carrera: ")

        with open('/home/user/Escritorio/borrowers_test.csv','a') as csvfile:
            fieldnames = ['apallido', 'nombre', 'codigo_categoria', 'fecha_registro','sex', 'cod_carrera', 'nombre_carrera']				
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow({'apallido': apellido, 'nombre': nombre, 'codigo_categoria': cod_cat, 'fecha_registro':reg_fecha,'sex': sexo, 'cod_carrera': cod_carrera, 'nombre_carrera':nom_carrera})
        print "\n" 
        
    elif numeral ==6:
        fh = open('/home/user/Escritorio/borrowers_test.csv')
        columna_order = csv.reader(fh, delimiter = ",")
      
        print "\n", "Posicion --- Nombre Columna"
        print "   0     --- Apellido"
        print "   1     --- Nombre"
        print "   2     --- Codigo Categoria"
        print "   3     --- Fecha Registro"
        print "   4     --- Sexo"
        print "   5     --- Codigo Carrera"
        print "   6     --- Nombre Carrera"
                
        pos= int(raw_input("ingrese el numero de columna que desea ordenar: "))
        apel_search = []
        for line  in columna_order:
            apellido = line[pos]
            apel_search.append(apellido)
        
        fh.close()
        lista=apel_search

        def burbuja(lista,tam):
            for i in range(1,tam):
                for j in range(0,tam-i):
                    if(lista[j] > lista[j+1]):
                        k = lista[j+1]
                        lista[j+1] = lista[j]
                        lista[j] = k;
 
        def imprimeLista(lista,tam):
            for i in range(0,tam):
                print lista[i]
 
        burbuja(lista,len(lista))
        imprimeLista(lista,len(lista))
        nextt = raw_input("Presione ENTER para continuar.....")
        
    elif numeral ==7:
        
        fh = open('/home/user/Escritorio/borrowers_test.csv')
        columna_order_quick = csv.reader(fh, delimiter = ",")      
        print "\n", "Posicion --- Nombre Columna"
        print "   0     --- Apellido"
        print "   1     --- Nombre"
        print "   2     --- Codigo Categoria"
        print "   3     --- Fecha Registro"
        print "   4     --- Sexo"
        print "   5     --- Codigo Carrera"
        print "   6     --- Nombre Carrera"
                
        pos= int(raw_input("ingrese el numero de columna que desea ordenar: "))
                
        apel_search = []
        for line  in columna_order_quick:
            apellido = line[pos]
            apel_search.append(apellido)
        fh.close()
        """
        lista=apel_search
        def quicksort(lista,izquierda,derecha):
            i=izquierda
            j=derecha
            x=lista[(izquierda + derecha)/2]
 
            while( i <= j ):
                while lista[i]<x and j<=derecha:
                    i=i+1
                while x<lista[j] and j>izquierda:
                    j=j-1
                if i<=j:
                    aux = lista[i]; lista[i] = lista[j]; lista[j] = aux;
                    i=i+1;  j=j-1;
                if izquierda < j:
                    quicksort( lista, izquierda, j );
            if i < derecha:
                quicksort( lista, i, derecha );
 
        def imprimeLista(lista,tam):
            for i in range(0,tam):
                print lista[i],

        quicksort(lista,0,len(lista)-1)
        imprimeLista(lista,len(lista))
        nextt = raw_input("Presione ENTER para continuar.....")
        """
        def quickSort(lista):
            quickSortAssist(lista,0,len(lista)-1)

        def quickSortAssist(lista,primero,ultimo):
            if primero<ultimo:
                split = partic(lista,primero,ultimo)
                quickSortAssist(lista,primero,split-1)
                quickSortAssist(lista,split+1,ultimo)


        def partic(lista,primero,ultimo):
            pivote = lista[primero]
            izquierda = primero+1
            derecha = ultimo

            done = False
            while not done:
                
                while izquierda <= derecha and lista[izquierda] <= pivote:
                    izquierda = izquierda + 1

                while lista[derecha] >= pivote and derecha >= izquierda:
                    derecha = derecha -1

                if derecha < izquierda:
                    done = True
                else:
                    temp = lista[izquierda]
                    lista[izquierda] = lista[derecha]
                    lista[derecha] = temp

            temp = lista[primero]
            lista[primero] = lista[derecha]
            lista[derecha] = temp

            return derecha

        lista = apel_search
        quickSort(lista)
        print "\n".join(str(x) for x in lista)
        nextt = raw_input("Presione ENTER para continuar.....")

    elif numeral ==8:
        fh = open('/home/user/Escritorio/borrowers_test.csv')
        columna_order_heap = csv.reader(fh, delimiter = ",")
        
        print "\n", "Posicion --- Nombre Columna"
        print "   0     --- Apellido"
        print "   1     --- Nombre"
        print "   2     --- Codigo Categoria"
        print "   3     --- Fecha Registro"
        print "   4     --- Sexo"
        print "   5     --- Codigo Carrera"
        print "   6     --- Nombre Carrera"
                
        pos= int(raw_input("ingrese el numero de columna que desea ordenar: "))
        heap_search = []
        for line  in columna_order_heap:
            heap_sel = line[pos]
            heap_search.append(heap_sel)
            
        def HeapSort(A):
            def heapify(A):
                start = (len(A) - 2) / 2
                while start >= 0:
                    siftDown(A, start, len(A) - 1)
                    start -= 1

            def siftDown(A, start, end):
                root = start
                while root * 2 + 1 <= end:
                    child = root * 2 + 1
                    if child + 1 <= end and A[child] < A[child + 1]:
                        child += 1
                    if child <= end and A[root] < A[child]:
                        A[root], A[child] = A[child], A[root]
                        root = child
                    else:
                        return

            heapify(A)
            end = len(A) - 1
            while end > 0:
                A[end], A[0] = A[0], A[end]
                siftDown(A, 0, end - 1)
                end -= 1

        if __name__ == '__main__':
    
            T = heap_search 

            HeapSort(T)
            print "\n".join(str(x) for x in T)
            nextt = raw_input("Presione ENTER para continuar.....")

        
   
    elif numeral ==9:
        print "\n", "a- Estadisticas: Arq --> Conta"
        print "b- Estadisticas: Ind --> Prof Ed"
        print "c- Estadisticas: ProfCSoc --> MaeAd"
        print "d- Estadisticas: LicEc --> ProfFis"
        print "e- Estadisticas de Estudiantes por Sexo","\n"
        
        est = raw_input("Seleccione una opcion: ")
        
        if est == 'a':
            visitas=[1038,995,576,194,3249,1317,767,1236,593,875]
            print "\n","Preparando estadisticas........","\n"
            labels = 'Arq', 'IC', 'Anes', 'Soc', 'Med', 'Jur','CiEd','LicAdm','Fisio','Conta'
        
            colors = ['red','green','pink','purple', 'cyan','yellow','orange','brown','black','lightskyblue']
      
        
            plt.pie(visitas, labels=labels, colors=colors,
            autopct='%1.1f%%', shadow=True, startangle=90)
            plt.axis('equal')
            fig = plt.figure()
            ax = fig.gca()
            plt.show()
            nextt = raw_input("Presione ENTER para continuar.....")
            print "\n"

        elif est == 'b':
            N = 10
            print "\n","Preparando estadisticas........","\n"
            menMeans = (325,570,424,247,503,203,169,840,1025,133)
            menStd =  (8)
            ind = np.arange(N)  
            width = 0.35       
            fig, ax = plt.subplots()
            colors = ['red','green','pink','purple', 'cyan','yellow','orange','brown','black','lightskyblue']
            rects1 = ax.bar(ind, menMeans, width, color=colors, yerr=menStd)

            ax.set_ylabel('Resultados')
            ax.set_title('Estadisticas de Estudiantes de Ingenieria Industrial a Profesorado en Educacion Basica')
            ax.set_xticks(ind + width)
            ax.set_xticklabels(('Ind','LicMerc','LicMate','ProfMat','LicLeng','LQF','LBio','LPsi','LabC','ProfEd'))
        
            def autolabel(rects):
            
                for rect in rects:
                    height = rect.get_height()
                    ax.text(rect.get_x() + rect.get_width()/2., 1.05*height,
                            '%d' % int(height),
                            ha='center', va='bottom')
                
                
            autolabel(rects1)
            plt.show()
            nextt = raw_input("Presione ENTER para continuar.....")
            print "\n"
        
        elif est == 'c':
            visitas=[28,623,185,13,441,44,71,65,211,85,35]
            print "\n","Preparando estadisticas........","\n"
            labels ='ProfCsoc','IngS','LicLet','EsGin','InAg','ProfParv','IngMec','LicFi','ProfIng','IngEl','MaeAd'
        
            colors = ['red','green','pink','purple', 'cyan','yellow','orange','brown','black','lightskyblue','blue']
      
        
            plt.pie(visitas, labels=labels, colors=colors,
            autopct='%1.1f%%', shadow=True, startangle=90)
            plt.axis('equal')
            fig = plt.figure()
            ax = fig.gca()
            plt.show()
            nextt = raw_input("Presione ENTER para continuar.....")
            print "\n"
        
        elif est == 'd':
            N = 11
            print "\n","Preparando estadisticas........","\n"
            menMeans = (29,71,36,33,20,27,9,5,7,7,6)
            menStd =  (8)
            ind = np.arange(N)  
            width = 0.35       
            fig, ax = plt.subplots()
            colors = ['red','green','pink','purple', 'cyan','yellow','orange','brown','black','lightskyblue','blue']
            rects1 = ax.bar(ind, menMeans, width, color=colors, yerr=menStd)

            ax.set_ylabel('Resultados')
            ax.set_title('Estadisticas para estudiantes de Lic en economia a Profesorado en Fisica')
            ax.set_xticks(ind + width)
            ax.set_xticklabels(('LicEc','LicCiQ','MaDocS','MaSaP','PrBio','MaGeAmb','MaesMetIn','ProfQ','LicIParv','EspMed','ProfFis'))
        
            def autolabel(rects):
            
                for rect in rects:
                    height = rect.get_height()
                    ax.text(rect.get_x() + rect.get_width()/2., 1.05*height,
                            '%d' % int(height),
                            ha='center', va='bottom')
                
                
            autolabel(rects1)
            plt.show()
            nextt = raw_input("Presione ENTER para continuar.....")
            print "\n"
        
        elif est == 'e':
            visitas=[9078,7657]
            print "\n","Preparando estadisticas........","\n"
            labels ='Femenino','Masculino'
            colors = ['pink', 'lightskyblue']
            plt.pie(visitas, labels=labels, colors=colors,
            autopct='%1.1f%%', shadow=True, startangle=90)
            plt.axis('equal')
            fig = plt.figure()
            ax = fig.gca()
            plt.show()
            nextt = raw_input("Presione ENTER para continuar.....")
            print "\n"
        
    elif numeral ==10:
        break
