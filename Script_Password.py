# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 20:22:45 2020

@author: PC H
"""
import random
import mysql.connector
from tabulate import tabulate



def generate():
    caracter = ["&","~","#","{","(","-","|","`","_","ç","^","à","@","°",")","]","+","=","}",">","<","^","¨","$","£","¤","ù","%","*","µ","?",".",";",":","!","§","1","2","3","4","5","6","6","7","8","9","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    mot_de_passe=""

    for i in range (30):
        choix=random.choice(caracter)
        mot_de_passe=mot_de_passe+choix

    return mot_de_passe


def connection():
    global connect, cursor    
    connect = mysql.connector.connect(host="localhost", user="root", password="", database="password_handler")
    cursor= connect.cursor()

    return connect, cursor


def show_data():
    connection()

    cursor.execute("SELECT idi, site, username, email, password  FROM info")

    myresult=cursor.fetchall()
    headers = ["Id", "Site", "Username", "Email", "Mot de passe"]
    print(tabulate(myresult, headers, tablefmt="psql"))



def insert_data(site, username, email, password):
    connection()

    sql = "INSERT INTO info (site, username, email, password) VALUES (%s, %s, %s, %s)"
    val = (site, username, email, password)
    cursor.execute(sql, val)

    connect.commit()

    print(cursor.rowcount, "Une ligne ajouté")
    print("\n")


def delete_data(idi):
    connection()

    sql = "DELETE FROM info WHERE idi="+idi
    cursor.execute(sql)
    connect.commit()

    print(cursor.rowcount, "Une ligne supprimée")
    print("\n")


#inititalisation
def menu():

    init=input("Voulez-vous: \n 1:Insérer des nouvelles données\n 2:Accéder à vos mot de passe\n 3:Effacer des données\n 4:Quitter\n")
    if init=="1":
        pw=input("Voulez-vous générer un mot de passe ? (o/n) : ")
        if pw=="o":
            site=input("Adresse site web : ")
            username=input("Nom d'utilisateur : ")
            email=input("Adresse email : ")
            password=generate()
            insert_data(site, username, email, password)
            menu()
        elif pw=="n":
            site=input("Adresse site web : ")
            username=input("Nom d'utilisateur : ")
            email=input("Adresse email : ")
            password=input("Mot de passe : ")
            insert_data(site, username, email, password)
            menu()
    elif init=="2":
        show_data()
        menu()
    elif init=="3":
        show_data()
        rm=input("Quel id voulez-vous supprimer ? : ")
        delete_data(rm)
        show_data()
        menu()
    elif init=="4":
        pass


menu()