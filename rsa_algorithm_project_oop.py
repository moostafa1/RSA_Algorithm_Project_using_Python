import math
import sys

"""
 We also need a small exponent say e :
But e Must be

An integer.
Not be a factor of n.
1 < e < Φ(n) [Φ(n) is discussed below],
Let us now consider it to be equal to 3.
"""

######################################################################################################################################
######################################################################################################################################


class RSA:
    def __init__(self):
        self.p = input("Enter Prime Number or a letter whose ascii is prime: ")
        self.q = input("Enter Prime Number or a letter whose ascii is prime: ")
        self.e = input("Enter Encryption key (1<e<n): ")
        self.p, self.q, self.e = self.check_input()
        self.message = input("Enter your message to be ciphered: ")


######################################################################################################################################
######################################################################################################################################




    def char_to_decimal(self, x):
        if str(x):
            """
            the following code will cast each letter to an 8-bit character,
            and THEN concatenate. this is how standard ASCII encoding works
            """
            new_x = 0
            for i in range(len(x)):
                new_x += ord(x[i])*2**(8 * (len(x) - i - 1))
        print("decimal: ", new_x)
        return new_x



######################################################################################################################################
######################################################################################################################################


    def check_prime(self, x):
        if x > 1:
           for i in range(2, x):
               if (x % i) == 0:
                   print(x, "is not a prime number")
                   print(i, "times", x//i, "is", x)
                   sys.exit()
                   break
           else:
               print(x, "is a prime number")
        else:
           print(x, "is not a prime number")
           sys.exit()


######################################################################################################################################
######################################################################################################################################


    def int_number(self, x):
        x = int(x)
        return x


######################################################################################################################################
######################################################################################################################################


    def e_value(self, e):
        n = self.p * self.q
        if e>1 and e<n and e!=self.p and e!=self.q:
            return e
        else:
            print("Please check that e value satisfy the conditions.")
            sys.exit()

######################################################################################################################################
######################################################################################################################################


    def check_input(self):
        #try:
        if (self.p.isdigit() and self.q.isdigit() and self.e.isdigit()):
            self.p = self.int_number(self.p)
            self.q = self.int_number(self.q)
            self.e = self.int_number(self.e)
            self.check_prime(self.p)
            self.check_prime(self.q)
            self.check_prime(self.e)
            self.e = self.e_value(self.e)

        elif (not self.p.isdigit() and not self.q.isdigit() and not self.e.isdigit()):
            self.p = self.char_to_decimal(self.p)
            self.q = self.char_to_decimal(self.q)
            self.e = self.char_to_decimal(self.e)
            self.check_prime(self.p)
            self.check_prime(self.q)
            self.check_prime(self.e)
            self.e = self.e_value(self.e)

        elif (self.p.isdigit() and not self.q.isdigit() and not self.e.isdigit()):
            self.p = self.int_number(self.p)
            self.q = self.char_to_decimal(self.q)
            self.e = self.char_to_decimal(self.e)
            self.check_prime(self.p)
            self.check_prime(self.q)
            self.check_prime(self.e)
            self.e = self.e_value(self.e)


        elif (not self.p.isdigit() and not self.q.isdigit() and self.e.isdigit()):
            self.p = self.char_to_decimal(self.p)
            self.q = self.char_to_decimal(self.q)
            self.e = self.int_number(self.e)
            self.check_prime(self.p)
            self.check_prime(self.q)
            self.check_prime(self.e)
            self.e = self.e_value(self.e)

        elif (self.p.isdigit() and self.q.isdigit() and not self.e.isdigit()):
            self.p = self.int_number(self.p)
            self.q = self.int_number(self.q)
            self.e = self.char_to_decimal(self.e)
            self.check_prime(self.p)
            self.check_prime(self.q)
            self.check_prime(self.e)
            self.e = self.e_value(self.e)

        elif (self.p.isdigit() and not self.q.isdigit() and self.e.isdigit()):
            self.p = self.int_number(self.p)
            self.q = self.char_to_decimal(self.q)
            self.e = self.int_number(self.e)
            self.check_prime(self.p)
            self.check_prime(self.q)
            self.check_prime(self.e)
            self.e = self.e_value(self.e)

        elif (not self.p.isdigit() and self.q.isdigit() and self.e.isdigit()):
            self.p = self.char_to_decimal(self.p)
            self.q = self.int_number(self.q)
            self.e = self.int_number(self.e)
            self.check_prime(self.p)
            self.check_prime(self.q)
            self.check_prime(self.e)
            self.e = self.e_value(self.e)

        elif (not self.p.isdigit() and self.q.isdigit() and not self.e.isdigit()):
            self.p = self.char_to_decimal(self.p)
            self.q = self.int_number(self.q)
            self.e = self.char_to_decimal(self.e)
            self.check_prime(self.p)
            self.check_prime(self.q)
            self.check_prime(self.e)
            self.e = self.e_value(self.e)


        #except:
        #    print("\n\aPlease enter 3 prime numbers and try again :)")
        #    sys.exit()
        return self.p, self.q, self.e


######################################################################################################################################
######################################################################################################################################


    def cipher_text(self, message):
        ord_message = [ord(i) for i in message]
        return ord_message


######################################################################################################################################
######################################################################################################################################


    def RSA(self):
        n = self.p * self.q
        Euler = (self.p-1) * (self.q-1)

        #encryption key
        e = self.e     #e--> encryption
        t = 0
        while(e < Euler):
            t = math.gcd(e, Euler)     #gcd --> returns greatest common divisor
            if (t == 1):
                break
            else:
                e += 1

        #decryption key
        dd = pow(e, -1)
        d = math.fmod(dd, Euler)    #d--> decryption

        #message = cipher_text("I'm 25 years old")
        message = self.cipher_text(self.message)  # 7543116

        encryption = []
        decryption = []
        ciphering = []
        for i in message:
            c = pow(i, e)    #c --> encrypted message
            m = pow(c, d)          #m --> decrypted message
            c = math.fmod(c, n)
            ciphering.append(int(c))
            m = math.fmod(m, n)
            m = round(m, 4)
            encryption.append(int(c))
            decryption.append(chr(int(m)))
        print("\nEncrypted message: ", encryption)
        print("decrypted message: ", decryption)
        m = ''.join(decryption)




        print("\nThe message we're ciphering is = ", ciphering)
        print("First prime number 'p' is = ", self.p)
        print("Second prime number 'q' is = ", self.q)
        print("n is = ", n)
        print("Euler is = ", Euler)
        print("private key: ", dd)
        print("encryption_key is = ", e)
        print("decryption_key is = ", d)
        print("decrypted_message is = ", m)


######################################################################################################################################
######################################################################################################################################


    #def model(self):
    #    self.p, self.q, self.e = self.check_input()
    #    self.RSA()


######################################################################################################################################
######################################################################################################################################


if __name__ == "__main__":
    rsa = RSA()
    rsa.RSA()
    #rsa.model()
