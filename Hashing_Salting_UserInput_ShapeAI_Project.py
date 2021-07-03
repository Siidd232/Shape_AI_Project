# -*- coding: utf-8 -*-
"""
Created on Sat Jul  3 23:38:05 2021

@author: Siddharth Sarraf
"""
#Importing the requuired Libraries
import hashlib
import uuid

salt = uuid.uuid4().hex #Fetching the salt 

user = str(input("Type the Message to be Encrypted: "))#Taking the Used Input 

Saltedmsg = salt+user #Adding the Salt to the message that needs to be encrypted

md5 =  hashlib.md5(Saltedmsg.encode('utf-8')).digest() #MD5 Hashing
sha256 = hashlib.sha256(Saltedmsg.encode('utf-8')).digest() #Shake 256 Hashing
sha512 = hashlib.sha512(Saltedmsg.encode('utf-8')).digest() #Shake 512 Hashing
sha1 = hashlib.sha1(Saltedmsg.encode('utf-8')).digest() #Sha1 Hashing

#Displaying the Output
print("Salted Message = ",Saltedmsg)
print("\n")
print("--------------------Salted Hashed Messages--------------------")
print("\n")
print("MD5 Salted Hashed Message is: ", md5)
print("\n")
print("Shake256 Salted Hashed Message is: ", sha256)
print("\n")
print("Shake512 Salted Hashed Message is: ", sha512)
print("\n")
print("SHA1 Salted Hashed Message is: ", sha1)
print("\n")
