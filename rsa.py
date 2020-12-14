# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 12:16:54 2020

@author: Wilfredo Mendivil
@CECS478 - lab3 -RSA
"""

def main():

    p = int(input("Enter a value for P(Prime number): "))
    q = int(input("Enter a value for Q(Prime number): "))
    e= int(input("Enter a value that is a relative prime to p &q:"))
    
    originalText= input("enter a message: ")
    #e =  65537                                                                 #standard for e to nearly always be the same value prime to p-1 * q-1
    n = p*q                                                                    #RSA Mod
    phi= (p-1)*(q-1)                                                           #phi
    
    #originalText ='hello'
    originalText.lower()
    print("original message is" , originalText)                                #print original message
    print("message as number is " , letterNumber(originalText))                #print the original converted to ascii
    
    
    #message to encrypt
    M =  letterNumber(originalText)                                            #message  changed to number  values
    
    #encrypt message
    encryptMessage = encrypt(M,e,n)                                            #encrypt the numbers passed to encrypt function
    print("")                                                                  #space
    print("Encrypted message is: " ,encryptMessage)                             #print encrypted values 
    
    
    #decrypt block
    d = getBezoutCoeff(e,phi)                                                  #d retrieved by using bezout coefficient
    decryptedText =decrypt(encryptMessage,n,d)                                 #decrypt message passing private key , message and n
    print("")                                                                  #empty line
    print("Decrypted message is: ",decryptedText)                               #print statement
    print("Decrypted message is: ",numToLetter(decryptedText))                                          #print decrypted word
 
    
def letterNumber(text):                                                        #convert letters to numberical value
    letterToNum =[]                                                            #empty list
    for char in text:                                                          # itterate through string until it is done 
        number  = ord(char)                                                    #take in the ascii value of the lettter
        letterToNum.append(str(number))                                        #add converted value to list
    return letterToNum                                                         #return list
 

#takes in the message, a
def encrypt(text, exponent, nValue):                                           #encrypt method
    encryptedMessage = []                                                      #empty list
    for num in text:                                                           #itterate through the encrypted message
        encryptedMessage.append(pow(int(num),exponent) % nValue)               #change number to an encrypted value
    return encryptedMessage                                                    #return updated values                
    
#takes in private key, nValue, and message
def decrypt(message,n,privateKey):                                             #decrypt function                             
    decryptedMessage = []                                                      #empty list
    for value in message:                                                      #itterate through list
        decryptedMessage.append(pow(int(value),privateKey)%n)                  #add decrypted value to list
    return decryptedMessage                                                    #return list
    
#used to calculate the private key
def getBezoutCoeff(e,phi):
     s1, s0 = 0,1  #initialize s1, & s0
     t1, t0 = 1,0 #intialize t1,t0
     x = e #initialize x as p
     y = phi #initilize y as q     
     while y != 0: # while y is not equal to zero loop
         quotient = x//y   #quotient to help determine remainder
         x, y = y, x - quotient * y  #change value of x and y through loop to keep updating
         s0, s1 = s1, s0 - quotient * s1  #update value for s0 and s1 by swapping to auto update x=y,y=x
         t0, t1 = t1, t0 - quotient * t1  #update value for t0 and t1 by swapping to auto update x=y,y=x
     if(e>phi):
        while(t0<0):                                                           #makes sure that the coeff isnt a negative
             t0 += phi                                                         #increment until positive
        return t0                                                              #return private key
     else:
         while(s0<0):                                                          #make sure coef isnt negative
             s0 +=phi                                                          #increment until positive      
         return s0                                                             #return private key

def numToLetter(message):                                                      #convert back to number
    wordInText = ''                                                            #empty string
    for value in message:                                                      #itterate through list
        letter = chr(value)                                                    #add value to letter
        wordInText += letter                                                   #add letter to the word
    return wordInText                                                          #return word


  
main()