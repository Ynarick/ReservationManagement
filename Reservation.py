from tkinter import *
from tkinter import ttk,messagebox
from PIL import Image,ImageTk 
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import mysql.connector
from tkinter import filedialog
import tkinter as tk
from datetime import date




class reservation:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1540x800+0+0")
      

        # creation des conteneurs

        #point commun des pages
       
        def infoclient():

            def ajoutclient():
                a1=NumCliChamp.get()
                a2=NomChamp.get()
                a3=adresseChamp.get()
                a4=TelChamp.get()
                if  not a1 or not a2 or not a3 or not a4:
                     messagebox.showerror("Erreur","Veuillez remplir tous les champs")
                else:
                    mysqldb=mysql.connector.connect(host="localhost",user="root",password="",database="gestion")
                    mycursor=mysqldb.cursor()
                    sql="INSERT INTO clients (numclient,nomclient,adresseclient,telhotel)VALUES(%s,%s,%s,%s)"
                    valu=(a1,a2,a3,a4)
                    mycursor.execute(sql,valu)
                    mysqldb.commit()
                    messagebox.showinfo("success","le client est bien ajoute.....")
                    mysqldb.close()
            def modifierclient():
                a1=NumCliChamp.get()
                a2=NomChamp.get()
                a3=adresseChamp.get()
                a4=TelChamp.get()
                mysqldb=mysql.connector.connect(host="localhost",user="root",password="",database="gestion")
                mycursor=mysqldb.cursor()
                sql="update clients set numclient=%s,nomclient=%s,adresseclient=%s,telhotel=%s where numclient=%s "
                valu=(a1,a2,a3,a4,a1)
                mycursor.execute(sql,valu)
                mysqldb.commit()
                messagebox.showinfo("succès","modification avec succès.....")
                mysqldb.close()
            def supprimerclient():
                a1=NumCliChamp.get()
                var=messagebox.askyesno("Attention","êtes vous sur de vouloir supprimer.....")
                if var > 0:
                
                    mysqldb=mysql.connector.connect(host="localhost",user="root",password="",database="gestion")
                    mycursor=mysqldb.cursor()
                    sql="DELETE  FROM  clients WHERE  numclient=%s"
                    valu=(a1,)
                    mycursor.execute(sql,valu)
                    treeclient.delete(treeclient.selection())
                    mysqldb.commit()
                    messagebox.showinfo("Succès","suppression avec succes.....")
                    mysqldb.close()
            def voir():
                
                mysqldb=mysql.connector.connect(host="localhost",user="root",password="",database="gestion")
                mycursor=mysqldb.cursor()
                mycursor.execute("SELECT * FROM clients")
                var=mycursor.fetchall()
                for i,(numclient,nomclient,adresseclient,telhotel) in enumerate(var,start=1):
                        treeclient.insert("",END,values=(numclient,nomclient,adresseclient,telhotel))
                mysqldb.close()
            def affichage(event):
                    a1=NumCliChamp.delete(0,END)
                    a2=NomChamp.delete(0,END)
                    a3=adresseChamp.delete(0,END)
                    a4=TelChamp.delete(0,END)
                    # champsoldeactclient.delete(0,END)
                    affect=treeclient.selection()[0]
                    select=treeclient.set(affect)
                    NumCliChamp.insert(0, select['1'])
                    NomChamp.insert(0, select['2'])
                    adresseChamp.insert(0, select['3'])
                    TelChamp.insert(0, select['4'])
            #fonction ajouter date
            def ajouterdate():
                 d1=firstdateChamp.get()
                 if not d1:
                      messagebox.showerror("Attention","Veuillez remplir le champ date")
                 mysqldb=mysql.connector.connect(host="localhost",user="root",password="",database="gestion")
                 mycursor=mysqldb.cursor()
                 var="INSERT INTO calendriers(firstdate) VALUES(%s)"
                 valu=(d1,)
                 mycursor.execute(var,valu)
                 mysqldb.commit()
                 messagebox.showinfo("succès","Ajout date avec succès...")
                 mysqldb.close()
            #afficher le contenu de la base de données
            def voire():
                
                mysqldb=mysql.connector.connect(host="localhost",user="root",password="",database="gestion")
                mycursor=mysqldb.cursor()
                mycursor.execute("SELECT * FROM calendriers")
                var=mycursor.fetchall()
                for i,(firstdate) in enumerate(var,start=1):
                        treedate.insert("",END,values=(firstdate))
                mysqldb.close()
            def affichages(event):
                    d1=firstdateChamp.delete(0,END)
                    
                    affect=treedate.selection()[0]
                    select=treedate.set(affect)
                    firstdateChamp.insert(0, select['1'])
            def supprimerDate():
                 d1=firstdateChamp.get()
                 var=messagebox.askyesno("Attention","êtes vous sûr de vouloir supprimer")
                 if var > 0:
                    mysqldb=mysql.connector.connect(host="localhost",user="root",password="",database="gestion")
                    mycursor=mysqldb.cursor()
                    sql="DELETE  FROM  calendriers WHERE  firstdate=%s"
                    valu=(d1,)
                    mycursor.execute(sql,valu)
                    treedate.delete(treedate.selection())
                    mysqldb.commit()
            def modifierDate():
                d1=firstdateChamp.get()
                
                mysqldb=mysql.connector.connect(host="localhost",user="root",password="",database="gestion")
                mycursor=mysqldb.cursor()
                sql="update calendriers set firstdate=%s where firstdate=%s "
                valu=(d1,d1)
                mycursor.execute(sql,valu)
                mysqldb.commit()
                messagebox.showinfo("succès","modification avec succès.....")
                mysqldb.close()          
                 
                    

                 

            div=Frame(self.root,bd=2,relief=RIDGE,bg="red")
            div.place(x=175,y=75,width=1210,height=350)
            divgauche=LabelFrame(div,text="Information sur le client",bg="white",font=("Times new roman",12,"bold"))
            divgauche.place(x=0,y=0,width=800,height=350)
            divdroite=LabelFrame(div,bd=2,font=("Times new roman",12,"bold"),relief=RIDGE,padx=10,bg="gray")
            divdroite.place(x=800,y=0,width=640,height=350)
            divbouton=Frame(self.root,bd=2,relief=RIDGE,height=48,bg="#2F4F4F")
            divbouton.place(x=175,y=425,width=1440,height=60)
            divtreeclient=Frame(self.root,bg="gray")
            divtreeclient.place(x=175,y=485,width=1440,height=350)
           

            #creation de la contenu de la div gauche
            NumCli=Label(divgauche,font=("Lucida Calligraphy",12,"bold"),text="Numero du client: ",padx=4,pady=8,bg="white")
            NumCli.grid(row=0,column=0)
            NumCliChamp=Entry(divgauche,width=30)
            NumCliChamp.grid(row=0,column=1)
            Nom=Label(divgauche,font=("Lucida Calligraphy",12,"bold"),text="Nom: ",padx=4,pady=8,bg="white")
            Nom.grid(row=1,column=0)
            NomChamp=Entry(divgauche,width=30)
            NomChamp.grid(row=1,column=1)
            adresse=Label(divgauche,font=("Lucida Calligraphy",12,"bold"),text="Adresse: ",padx=4,pady=8,bg="white")
            adresse.grid(row=2,column=0)
            adresseChamp=Entry(divgauche,width=30)
            adresseChamp.grid(row=2,column=1)
            Tel=Label(divgauche,font=("Lucida Calligraphy",12,"bold"),text="Tel Hotel: ",padx=4,pady=8,bg="white")
            Tel.grid(row=3,column=0)
            TelChamp=Entry(divgauche,width=30)
            TelChamp.grid(row=3,column=1)
            #creation de la contenu de la div droite

            firstdate=Label(divdroite,font=("Lucida Calligraphy",10,"bold"),text="Date disponible: ",padx=4,pady=8,bg="gray")
            firstdate.place(x=0,y=5)
            firstdateChamp=Entry(divdroite,width=25)
            firstdateChamp.place(x=140,y=10,height=25)

            #CRUD date depart
            
            ajoutercdate=Button(divdroite,text="Ajouter Date",width=15,padx=0,pady=7,font=("Lucida Calligraphy",12,"bold"),bg="#D2691E",fg="black",relief=GROOVE,command=ajouterdate)
            ajoutercdate.place(x=0,y=130)
            modifierdate=Button(divdroite,text="Modifier Date",width=15,padx=0,pady=7,font=("Lucida Calligraphy",12,"bold"),bg="#D2691E",fg="black",relief=GROOVE,command=modifierDate)
            modifierdate.place(x=0,y=185)
            supprimerdate=Button(divdroite,text="Supprimer Date",width=15,padx=0,pady=7,font=("Lucida Calligraphy",12,"bold"),bg="#D2691E",fg="black",relief=GROOVE,command=supprimerDate)
            supprimerdate.place(x=0,y=240)

            








            #titre
          

            #creation de treeview

            treeclient=ttk.Treeview(divtreeclient,columns=(1,2,3,4),show="headings")
            treeclient.place(x=0,y=0,height=350)
            treeclient.bind("<ButtonRelease>",affichage)
            treeclient.heading(1,text="Numero Client",anchor="center")
            treeclient.heading(2,text="Nom",anchor="center")
            treeclient.heading(3,text="Adresse",anchor="center")
            treeclient.heading(4,text="Tel Hotel",anchor="center")

            treeclient.column(1,width=200,anchor="center")
            treeclient.column(2,width=200,anchor="center")
            treeclient.column(3,width=200,anchor="center")
            treeclient.column(4,width=200,anchor="center")

            treedate=ttk.Treeview(divtreeclient,columns=(1),show="headings")
            treedate.place(x=800,y=0,width=405,height=350)
            treedate.bind("<ButtonRelease>",affichages)
            treedate.heading(1,text="Date Disponibles",anchor="center")
            treedate.column(1,width=200)


            #table date
            
             

            #Bouton CRUD client
            ajouterclient=Button(divbouton,text="Ajouter Client",width=15,padx=0,pady=7,font=("Lucida Calligraphy",12,"bold"),bg="#D2691E",fg="black",relief=GROOVE,command=ajoutclient)
            ajouterclient.place(x=200,y=5)
            modifierClient=Button(divbouton,text="Modifier Client",width=15,padx=0,pady=7,font=("Lucida Calligraphy",12,"bold"),bg="#D2691E",fg="black",relief=GROOVE,command=modifierclient)
            modifierClient.place(x=500,y=5)
            supprimerClient=Button(divbouton,text="Supprimer Client",width=15,padx=0,pady=7,font=("Lucida Calligraphy",12,"bold"),bg="#D2691E",fg="black",relief=GROOVE,command=supprimerclient)
            supprimerClient.place(x=800,y=5)


            pointcommun()
            img=Image.open(r"vaika.jpg")
            img=img.resize((140,160))
            self.photoimg=ImageTk.PhotoImage(img)
            self.btn1=Label(self.root,image=self.photoimg,cursor="hand2")
            self.btn1.place(x=17,y=8,width=140,height=160)
            voir()
            voire()

    ##############################################  A PROPOS DE VEHICULE ###########################################


        def infovehicule():
            def ajoutvehicule():
                a1=NumVehChamp.get()
                a2=NbrplaceChamp.get()
                a3=NbrplacedispChamp.get()
                a2=int(a2)
                a3=int(a3)

                if not a1 or not a2 or not a3:
                    messagebox.showerror("Erreur","Veuillez remplir tous les champs")
                if a2<a3:
                   messagebox.showerror("info","verifier bien votre information")
                if a2<0 and a3<0:
                     messagebox.showerror("Erreur","Veuillliez taper nombre positif")
                else:
                   mysqldb=mysql.connector.connect(host="localhost",user="root",password="",database="gestion")
                   mycursor=mysqldb.cursor()
                   sql="INSERT INTO vehicules (numvehicule,nbrplace,nbrplacedispo)VALUES(%s,%s,%s)"
                   valu=(a1,a2,a3)
                   mycursor.execute(sql,valu)
                   mysqldb.commit()
                   messagebox.showinfo("success","le vehicule est bien ajoute.....")
                   mysqldb.close()
            def modifiervehicule():
                a1=NumVehChamp.get()
                a2=NbrplaceChamp.get()
                a3=NbrplacedispChamp.get()
                mysqldb=mysql.connector.connect(host="localhost",user="root",password="",database="gestion")
                mycursor=mysqldb.cursor()
                sql="UPDATE vehicules SET numvehicule=%s,nbrplace=%s,nbrplacedispo=%s where numvehicule=%s "
                valu=(a1,a2,a3,a1)
                mycursor.execute(sql,valu)
                mysqldb.commit()
                messagebox.showinfo("success","modification avec succès.....")
                mysqldb.close()


            def supprimervehicule():
                a1=NumVehChamp.get()
                var=messagebox.askyesno("Attention","êtes vous sur de vouloir supprimer..?")
                if var > 0:
                
                    mysqldb=mysql.connector.connect(host="localhost",user="root",password="",database="gestion")
                    mycursor=mysqldb.cursor()
                    sql="DELETE  FROM  vehicules WHERE  numvehicule=%s"
                    valu=(a1,)
                    mycursor.execute(sql,valu)
                    treev.delete(treev.selection())
                    mysqldb.commit()
                    messagebox.showinfo("Succès","suppression avec succes.....")
                    mysqldb.close()


            def voir():
                
                mysqldb=mysql.connector.connect(host="localhost",user="root",password="",database="gestion")
                mycursor=mysqldb.cursor()
                mycursor.execute("SELECT * FROM vehicules")
                var=mycursor.fetchall()
                for i,(numvehicule,nbrplace,nbrplacedispo) in enumerate(var,start=1):
                        treev.insert("",END,values=(numvehicule,nbrplace,nbrplacedispo))
                mysqldb.close()
            def affichage(event):
                    a1=NumVehChamp.delete(0,END)
                    a2=NbrplaceChamp.delete(0,END)
                    a3=NbrplacedispChamp.delete(0,END)
                    affect=treev.selection()[0]
                    select=treev.set(affect)
                    NumVehChamp.insert(0, select['1'])
                    NbrplaceChamp.insert(0, select['2'])
                    NbrplacedispChamp.insert(0, select['3'])
                          

                

           
            div=Frame(self.root,bd=2,relief=RIDGE,bg="red")
            div.place(x=175,y=75,width=1210,height=350)
            divgauche=LabelFrame(div,text="Information vehicule",bg="white",font=("Times new roman",12,"bold"))
            divgauche.place(x=0,y=0,width=800,height=350)
            divdroite=LabelFrame(div,bd=2,font=("Times new roman",12,"bold"),relief=RIDGE,padx=10,bg="#333333")
            divdroite.place(x=800,y=0,width=600,height=350)
            divbouton=Frame(self.root,bd=2,relief=RIDGE,height=48,bg="#2F4F4F")
            divbouton.place(x=175,y=425,width=1440,height=60)
            divtreeclient=Frame(self.root,bg="gray")
            divtreeclient.place(x=175,y=485,width=1210,height=300)

            #creation de la contenu de la div gauche
            NumVeh=Label(divgauche,font=("Lucida Calligraphy",12,"bold"),text="Numero vehicule: ",padx=4,pady=8,bg="white")
            NumVeh.grid(row=0,column=0)
            NumVehChamp=Entry(divgauche,width=30)
            NumVehChamp.grid(row=0,column=1)
            Nbrplace=Label(divgauche,font=("Lucida Calligraphy",12,"bold"),text="Nombre de place ",padx=4,pady=8,bg="white")
            Nbrplace.grid(row=1,column=0)
            NbrplaceChamp=Entry(divgauche,width=30)
            NbrplaceChamp.grid(row=1,column=1)
            Nbrplacedisp=Label(divgauche,font=("Lucida Calligraphy",12,"bold"),text="Nombre de place disponible: ",padx=4,pady=8,bg="white")
            Nbrplacedisp.grid(row=2,column=0)
            NbrplacedispChamp=Entry(divgauche,width=30)
            NbrplacedispChamp.grid(row=2,column=1)
            


            #creation de treeview

            treev=ttk.Treeview(divtreeclient,columns=(1,2,3),show="headings")
            treev.place(x=0,y=0)
            treev.heading(1,text="Numero vehicule",anchor="center")
            treev.heading(2,text="Nombre de place",anchor="center")
            treev.heading(3,text="Nombre de place disponible",anchor="center")
            treev.bind("<ButtonRelease>",affichage)
            

            treev.column(1,width=200)
            treev.column(2,width=200)
            treev.column(3,width=200)
            

            #Bouton CRUD vehicule
            ajoutervehicule=Button(divbouton,text="Ajouter vehicule",width=15,padx=0,pady=7,font=("Lucida Calligraphy",12,"bold"),bg="#D2691E",fg="black",relief=GROOVE,command=ajoutvehicule)
            ajoutervehicule.place(x=200,y=5)
            #modifier vehicule
            modifierVehicule=Button(divbouton,text="Modifier vehicule",width=15,padx=0,pady=7,font=("Lucida Calligraphy",12,"bold"),bg="#D2691E",fg="black",relief=GROOVE,command=modifiervehicule)
            modifierVehicule.place(x=500,y=5)
            #supprimer vehicule
            supprimerVehicule=Button(divbouton,text="Supprimer vehicule",width=15,padx=0,pady=7,font=("Lucida Calligraphy",12,"bold"),bg="#D2691E",fg="black",relief=GROOVE,command=supprimervehicule)
            supprimerVehicule.place(x=800,y=5)



            pointcommun()
            img=Image.open(r"vaika.jpg")
            img=img.resize((140,160))
            self.photoimg=ImageTk.PhotoImage(img)
            self.btn1=Label(self.root,image=self.photoimg,cursor="hand2")
            self.btn1.place(x=17,y=8,width=140,height=160)
            voir()
        
    ###################################################### A PROPOS DE RESERVATION ###############################################          

        def inforeserver():
           


            def ajoutreserver():
                a1=NumResChamp.get()
                a2=datedepartChamp.get()
                a3=dateresChamp.get()
                a4=nbrpersChamp.get()
                a5=NumcliChamp.get()
                a6=NumVehChamp.get()
                
                if not a1 or not a2 or not a3 or not a4 or not a5 or not a6:
                     messagebox.showerror("Attention","Veuillez remplir tous les champ")
                a4=int(a4)
                if a4<0:
                    messagebox.showerror("Erreur","Verifier bien votre nombre personne")
                # a5= int(a5)
                # a4=int(a4)
                
                # mysqldb=mysql.connector.connect(host="localhost",user="root",password="",database="gestion")
                # mycursor=mysqldb.cursor()
                # mycursor.execute("select numclient from clients where numclient=%s ",(a5,))
                # var=mycursor.fetchone()
                # if var[0]!= a5 :
                #     messagebox.showerror("Erreur","le numero du client n' existe pas")
                    
                
                # mysqldb=mysql.connector.connect(host="localhost",user="root",password="",database="gestion")
                # mycursor=mysqldb.cursor()
                # mycursor.execute("select numvehicule from vehicules WHERE numvehicule=%s",(a6,))
                # var1=mycursor.fetchone()
                # if var1[0]!=a6 :
                #      messagebox.showerror("Erreur","le numero de vehicule n' existe pas")
                
                # mysqldb=mysql.connector.connect(host="localhost",user="root",password="",database="gestion")
                # mycursor=mysqldb.cursor()
                # mycursor.execute("select firstdate from calendriers WHERE firstdate=%s",(a2,))
                # var2=mycursor.fetchone()
                # if var2[0]==a2 :
                #      messagebox.showerror("Erreur","Ce date n'existe pas dans la date disponible")
                
               
               
                else:

                    mysqldb=mysql.connector.connect(host="localhost",user="root",password="",database="gestion")
                    mycursor=mysqldb.cursor()
                    
                    sql="INSERT INTO reservers (numres,datedepart,datere,nbrpersonne,numcli,numveh)VALUES(%s,%s,%s,%s,%s,%s)"
                    valu=(a1,a2,a3,a4,a5,a6)
                    mycursor.execute(sql,valu)
                    vehicule=("update vehicules set nbrplacedispo=nbrplacedispo-%s where numvehicule=%s")
                    val=(a4,a6)
                    mycursor.execute(vehicule,val)
                    mysqldb.commit()
                    messagebox.showinfo("succès","Ajout de reservation avec succès...")
                    mysqldb.close()


            def modifierreserver():
                a1=NumResChamp.get()
                a2=datedepartChamp.get()
                a3=dateresChamp.get()
                a4=nbrpersChamp.get()
                a5=NumcliChamp.get()
                a6=NumVehChamp.get()
                mysqldb=mysql.connector.connect(host="localhost",user="root",password="",database="gestion")
                mycursor=mysqldb.cursor()
                sql="update reservers set numres=%s,datedepart=%s,datere=%s,nbrpersonne=%s,numcli=%s,numveh=%s where numres=%s "
                valu=(a1,a2,a3,a4,a5,a6,a1)
                mycursor.execute(sql,valu)
                mysqldb.commit()
                messagebox.showinfo("success","modification avec successs.....")
                mysqldb.close()


            def supprimerreserver():
                a1=NumResChamp.get()
                a2=datedepartChamp.get()
                a3=dateresChamp.get()
                a4=nbrpersChamp.get()
                a5=NumcliChamp.get()
                a6=NumVehChamp.get()
                if not a1 or not a2 or  not a3 or not a4 or not a5:
                     messagebox.showerror("Erreur","Veuillez selectionner  l'element à supprimer")
                else:
                     var=messagebox.askyesno("Attention","êtes vous sûr de vouloir supprimer.....")
                     if var > 0:
                
                         mysqldb=mysql.connector.connect(host="localhost",user="root",password="",database="gestion")
                         mycursor=mysqldb.cursor()
                         sql="DELETE  FROM  reservers WHERE  numres=%s"
                         valu=(a1,)
                         mycursor.execute(sql,valu)
                         treeRes.delete(treeRes.selection())
                         vehicule=("update vehicules set nbrplacedispo=nbrplacedispo+%s where numvehicule=%s")
                         val=(a4,a6)
                         mycursor.execute(vehicule,val)
                         mysqldb.commit()
                         messagebox.showinfo("succès","suppression avec succes.....")
                         mysqldb.close()


            def voir():
                
                mysqldb=mysql.connector.connect(host="localhost",user="root",password="",database="gestion")
                mycursor=mysqldb.cursor()
                mycursor.execute("SELECT * FROM reservers")
                var=mycursor.fetchall()
                for i,(numres,datedepart,datere,nbrpersonne,numcli,numveh) in enumerate(var,start=1):
                        treeRes.insert("",END,values=(numres,datedepart,datere,nbrpersonne,numcli,numveh))
                mysqldb.close()
            def affichage(event):

                a1=NumResChamp.delete(0,END)
                a2=datedepartChamp.delete(0,END)
                a3=dateresChamp.delete(0,END)
                a4=nbrpersChamp.delete(0,END)
                a5=NumcliChamp.delete(0,END)
                a6=NumVehChamp.delete(0,END)
                affect=treeRes.selection()[0]
                select=treeRes.set(affect)
                NumResChamp.insert(0, select['1'])
                datedepartChamp.insert(0, select['2'])
                dateresChamp.insert(0, select['3'])
                nbrpersChamp.insert(0, select['4'])
                NumcliChamp.insert(0, select['5'])
                NumVehChamp.insert(0, select['6'])
                    # champsoldeactclient.insert(0, select['4'])



             #fonction élaborer facture       
            def elaborer_facture():
                # Obtenir l'élément sélectionné dans le tableau
                selected_item = treeRes.selection()
                if selected_item:
                   item = treeRes.item(selected_item)
                   values = item['values']
        
                # Récupérer les valeurs des colonnes sélectionnées
                   numres = values[0]
                   datedepart = values[1]
                   dateres = values[2]
                   nbrpers = values[3]
                   numcli = values[4]
                   numveh = values[5]


                   # Demander à l'utilisateur de choisir l'emplacement du dossier
                   dossier = filedialog.askdirectory()
        
                   if dossier:
            # Générer le PDF de la facture dans le dossier choisi
                    chemin_fichier = dossier + "/facture.pdf"
                    c = canvas.Canvas(chemin_fichier, pagesize=A4)
                    c.setFont("Helvetica", 12)
                    c.drawString(100, 750, "Facture")
                    c.drawString(100, 700, f"N° Reservation : {numres}")
                    c.drawString(100, 650, f"Date Départ : {datedepart}")
                    c.drawString(100, 600, f"Date Réservation : {dateres}")
                    c.drawString(100, 550, f"Nombre Personne : {nbrpers}")
                    c.drawString(100, 500, f"N° Client: {numcli}")
                    c.drawString(100, 450, f"N° Véhicule : {numveh}")
                    c.save()
                   
               
            def afficher_etat_places():
                     
                    mysqldb=mysql.connector.connect(host="localhost",user="root",password="",database="gestion")
                    mycursor=mysqldb.cursor()
                    query = """SELECT V.numvehicule, V.nbrplacedispo, V.nbrplace FROM vehicules V WHERE V.numvehicule IN (SELECT R.numveh FROM reservers R WHERE R.datedepart IN (SELECT  R2.datedepart FROM reservers R2))"""
                    mycursor.execute(query)
                    result = mycursor.fetchall()
                    mycursor.close()

                    places = []
                    for row in result:
                        places.append(f"Véhicule N°: {row[0]} \n- Places disponibles : {row[1]} \n- Nombres des Places : {row[2]}\n\n")
    
                        if places:
                            resultat.config(text="\n".join(places))
                        else:
                            resultat.config(text="Aucun véhicule ne part à cette date.")














           
            div=Frame(self.root,bd=2,relief=RIDGE,bg="white")
            div.place(x=175,y=75,width=1440,height=350)
            divgauche=LabelFrame(div,text="Information réservation",bg="white",font=("Times new roman",12,"bold"))
            divgauche.place(x=0,y=0,width=600,height=350)
            divdroite=LabelFrame(div,bd=2,font=("Times new roman",12,"bold"),relief=RIDGE,padx=10,bg="#333333")
            divdroite.place(x=600,y=0,width=400,height=350)
            # divlist=Frame(divdroite,bd=2,font=("Times new roman",12,"bold"),relief=RIDGE,padx=10,bg="#333333")
            # divlist.place(x=0,y=5,width=200,height=345)
            # divrecherche=Frame(divdroite,bd=2,font=("Times new roman",12,"bold"),relief=RIDGE,padx=10,bg="#333333")
            # divrecherche.place(x=0,y=5,width=200,height=345)

            divbouton=Frame(self.root,bd=2,relief=RIDGE,height=48,bg="#2F4F4F")
            divbouton.place(x=175,y=425,width=1440,height=60)
            divtreeclient=Frame(self.root,bg="gray")
            divtreeclient.place(x=175,y=485,width=1400,height=300)
            divreser=Frame(divtreeclient,bg="gray")
            divreser.place(x=0,y=0,width=1200,height=300)

            #creation de la contenu de la div gauche
            NumRes=Label(divgauche,font=("Lucida Calligraphy",12,"bold"),text="Numero reservation: ",padx=4,pady=8,bg="white")
            NumRes.grid(row=0,column=0)
            NumResChamp=Entry(divgauche,width=30)
            NumResChamp.grid(row=0,column=1)

            mysqldb=mysql.connector.connect(host="localhost",user="root",password="",database="gestion")
            mycursor=mysqldb.cursor()
            mycursor.execute("select firstdate from calendriers")
            donnes=mycursor.fetchall()
            donnes=[row[0] for row in donnes]
            mycursor.close()
            mysqldb.close()

            datedepart=Label(divgauche,font=("Lucida Calligraphy",12,"bold"),text="Date de depart ",padx=4,pady=8,bg="white")
            datedepart.grid(row=1,column=0)
            datedepartChamp=ttk.Combobox(divgauche,font=("Arial",11))
            datedepartChamp['values']=donnes
            datedepartChamp.grid(row=1,column=1)




            dateres=Label(divgauche,font=("Lucida Calligraphy",12,"bold"),text="Date de reservation: ",padx=4,pady=8,bg="white")
            dateres.grid(row=2,column=0)
            dateresChamp=Entry(divgauche,width=30)
            dateresChamp.grid(row=2,column=1)

            nbrpers=Label(divgauche,font=("Lucida Calligraphy",12,"bold"),text="Nombre de personnes",padx=4,pady=8,bg="white")
            nbrpers.grid(row=3,column=0)
            nbrpersChamp=Entry(divgauche,width=30)
            nbrpersChamp.grid(row=3,column=1)


            mysqldb=mysql.connector.connect(host="localhost",user="root",password="",database="gestion")
            mycursor=mysqldb.cursor()
            mycursor.execute("select numclient from clients ")
            donnes=mycursor.fetchall()
            donnes=[row[0] for row in donnes]
            mycursor.close()
            mysqldb.close()

            Numcli=Label(divgauche,font=("Lucida Calligraphy",12,"bold"),text="Numero Client ",padx=4,pady=8,bg="white")
            Numcli.grid(row=4,column=0)
            NumcliChamp=ttk.Combobox(divgauche,font=("Arial",11))
            NumcliChamp['values']=donnes
            NumcliChamp.grid(row=4,column=1)

            # NumcliChamp=Entry(divgauche,width=30)
            # NumcliChamp.grid(row=4,column=1)

            NumVeh=Label(divgauche,font=("Lucida Calligraphy",12,"bold"),text="Numero Vehicule: ",padx=4,pady=8,bg="white")
            NumVeh.grid(row=5,column=0)
            # NumVehChamp=Entry(divgauche,width=30)
            # NumVehChamp.grid(row=5,column=1)

            mysqldb=mysql.connector.connect(host="localhost",user="root",password="",database="gestion")
            mycursor=mysqldb.cursor()
            mycursor.execute("select numvehicule from vehicules ")
            donnes=mycursor.fetchall()
            donnes=[row[0] for row in donnes]
            mycursor.close()
            mysqldb.close()


            NumVehChamp=ttk.Combobox(divgauche,font=("Arial",11))
            NumVehChamp['values']=donnes
            NumVehChamp.grid(row=5,column=1)


            
            
           



            

            #creation de treeview
            scroll_x=ttk.Scrollbar(divreser,orient=HORIZONTAL)
            scroll_y=ttk.Scrollbar(divreser,orient=VERTICAL)
            treeRes=ttk.Treeview(divreser,columns=(1,2,3,4,5,6),show="headings")
            scroll_x.pack(side=BOTTOM,fill=X)
            scroll_y.pack(side=RIGHT,fill=Y)

            scroll_x=ttk.Scrollbar(command=treeRes.xview)
            scroll_y=ttk.Scrollbar(command=treeRes.yview)

            treeRes.place(x=0,y=0)
            treeRes.heading(1,text="Numero reservation ",anchor="center")
            treeRes.heading(2,text="Date de depart",anchor="center")
            treeRes.heading(3,text="Date de reservation",anchor="center")
            treeRes.heading(4,text="Nombre de personnes",anchor="center")
            treeRes.heading(5,text="Numero Client",anchor="center")
            treeRes.heading(6,text="Numero Vehicule",anchor="center")
            treeRes.bind("<ButtonRelease>",affichage)
            # treeclient.heading(4,text="Tel Hotel",anchor="center")

            treeRes.column(1,width=100)
            treeRes.column(2,width=100)
            treeRes.column(3,width=100)
            treeRes.column(4,width=100)
            treeRes.column(5,width=100)
            treeRes.column(6,width=100)
            # treeclient.column(4,width=200)
            treeRes.pack(fill=BOTH,expand=1)

            resultat = Label(divdroite, text="")
            resultat.place(x=5,y=10)


            #recherche 
            # searchpar=Label(divrecherche,text="Rechercher par",font=("Nigerian",12,"bold"),bg="red",fg="black",padx=2,pady=6)
            # searchpar.grid(row=0,column=0)
            # choi=ttk.Combobox(divrecherche,textvariable=self.recherche,state="readonly",font=("ARIAL",13,"bold"))
            # choi["values"]=("Numero de compte","Nom")
            # choi.grid(row=0,column=1)
            # choi.current(0)


            

            #Bouton CRUD reservation
            
            #Ajouter de réservation
            ajouter_button = Button(divbouton,text="Ajouter Réservation",font=("Lucida Calligraphy",10),bg="#D2691E",fg="black",relief=GROOVE,command=ajoutreserver)
            ajouter_button.place(x=0,y=5,width=200,height=45)


            #Annuler de réservation
            supprimer_button = Button(divbouton,text="Annuler réservation",font=("Lucida Calligraphy",10),bg="#D2691E",fg="black",relief=GROOVE,command=supprimerreserver)
            supprimer_button.place(x=256,y=5,width=200,height=45)


            #Modifier la réservation
            modifier_button = Button(divbouton,text="Modifier réservation",font=("Lucida Calligraphy",10),bg="#D2691E",fg="black",relief=GROOVE,command=modifierreserver)
            modifier_button.place(x=512,y=5,width=200,height=45)
            #liste d'etat de place
            liste_button = Button(divbouton,text="Lister etat Places",font=("Lucida Calligraphy",10),bg="#D2691E",fg="black",relief=GROOVE,command=afficher_etat_places)
            liste_button.place(x=900,y=5,width=200,height=45)

            #Elaborer de facture
            facture_button = Button(divbouton,text="Élaborer Facture",font=("Lucida Calligraphy",10),bg="#D2691E",fg="black",relief=GROOVE,command=elaborer_facture)
            facture_button.place(x=1145,y=5,width=200,height=45)

            
            # scroll=ttk.Scrollbar(divdroite,orient=VERTICAL)
            # scroll.pack(side=RIGHT,fill=Y)
            # scroll=ttk.Scrollbar(command=resultat.yview)
            # resultat.pack(fill=Y,expand=1)

            pointcommun()
            voir()
            def images():
                        img=Image.open(r"vaika.jpg")
                        img=img.resize((140,160))
                        self.photoimg=ImageTk.PhotoImage(img)
                        self.btn1=Label(self.root,image=self.photoimg,cursor="hand2")
                        self.btn1.place(x=17,y=8,width=140,height=160)
            images()
                

        def pointcommun():

            diventete=Frame(self.root,bd=2,relief=RIDGE,width=1540,height=75,bg="#2F4F4F")
            diventete.place(x=0,y=0)
            titre=Label(diventete,text="Gestion de Réservation",font=("Times new roman",40,"bold"),bg="#2F4F4F")
            titre.place(x=550,height=50)
            divmarge=Frame(self.root,bd=2,relief=RIDGE,width=175,height=1540,bg="#2F4F4F")
            divmarge.place(x=0,y=0)
            client=Button(divmarge,text="Client",width=14,height=2,bg="#660000",font=("Harlow Solid Italic",14),bd=0,fg="white",command=infoclient)
            client.place(x=0,y=260)
            reserver=Button(divmarge,text="reserver",width=14,height=2,bg="#660000",font=("Harlow Solid Italic",14),bd=0,fg="white",command=inforeserver)
            reserver.place(x=0,y=325)
            vehicule=Button(divmarge,text="vehicule",width=14,height=2,bg="#660000",font=("Harlow Solid Italic",14),bd=0,fg="white",command=infovehicule)
            vehicule.place(x=0,y=390)
            
        infoclient()

root=Tk()
ob=reservation(root)
root.mainloop()

