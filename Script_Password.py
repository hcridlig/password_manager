# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 20:22:45 2020

@author: PC H
"""
import random
import mysql.connector



def generate():
    caracter = ["&","~","#","{","(","-","|","`","_","ç","^","à","@","°",")","]","+","=","}",">","<","^","¨","$","£","¤","ù","%","*","µ","?",".",";",":","!","§","1","2","3","4","5","6","6","7","8","9","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    mot_de_passe=""

    for i in range (30):
        choix=random.choice(caracter)
        mot_de_passe=mot_de_passe+choix

    return mot_de_passe



def show_data():
    connect = mysql.connector.connect(host="localhost", user="root", password="", database="password_handler")
    cursor= connect.cursor()

    cursor.execute("SELECT site, username, email, password  FROM info")

    myresult=cursor.fetchall()

    for x in myresult:
        print(x)


def insert_data(site, username, email, password):
    connect = mysql.connector.connect(host="localhost", user="root", password="", database="password_handler")
    cursor= connect.cursor()

    sql = "INSERT INTO info (site, username, email, password) VALUES (%s, %s, %s, %s)"
    val = (site, username,email,password)
    cursor.execute(sql, val)

    connect.commit()

    print(cursor.rowcount, "record inserted.")    



#inititalisation

init=input("Voulez-vous: \n 1:Insérer des nouvelles données\n 2:Accéder à vos mot de passe\n")
if init=="1":
    pw=input("Voulez-vous générer un mot de passe ? (o/n) : ")
    if pw=="o":
        site=input("Adresse site web : ")
        username=input("Nom d'utilisateur : ")
        email=input("Adresse email : ")
        password=generate()
        insert_data(site, username, email, password)
    elif pw=="n":
        site=input("Adresse site web : ")
        username=input("Nom d'utilisateur : ")
        email=input("Adresse email : ")
        password=input("Mot de passe : ")
        insert_data(site, username, email, password)
elif init=="2":
    show_data()