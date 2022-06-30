import sys
import math
from tkinter import *

######################################################################################################################################
######################################################################################################################################


# colors link sire: https://www.tcl.tk/man/tcl8.5/TkCmd/colors.html
"""
 We also need a small exponent say e :
But e Must be

An integer.
Not be a factor of n.
1 < e < Φ(n) [Φ(n) is discussed below],
Let us now consider it to be equal to 3.
"""

FONT = "Helvetica 16"
FONT2 = "Helvetica 12"
FONT_BOLD = "Helvetica 11 bold"
Background = "#336d92"

img = "bigstock-Internet-Security.ico"

######################################################################################################################################
######################################################################################################################################


class RSA:
    def __init__(self):
        self.win = Tk()
        self._setup_main_window()


######################################################################################################################################
######################################################################################################################################




    def char_to_decimal(self, x):
        try:
            if str(x):
                """
                the following code will cast each letter to an 8-bit character,
                and THEN concatenate. this is how standard ASCII encoding works
                """
                new_x = 0
                for i in range(len(x)):
                    new_x += ord(x[i])*2**(8 * (len(x) - i - 1))
                self.showText(f"\ndecimal: {new_x}")
                return new_x
        except:
            self.showText("\nERROR: char_to_decimal")



######################################################################################################################################
######################################################################################################################################


    def check_prime(self, x):
        #try:
        if x > 1:
           for i in range(2, x):
               if (x % i) == 0:
                   self.showText(f"\n{x} is not a prime number")
                   self.showText(f"\n{i} times {x//i} is {x}")
                   self.showText("\n\n"+"#"*112+"\n\n")
                   return False
                   #sys.exit()
                   break
           else:
               self.showText(f"\n{x} is a prime number")
               return True
        else:
           self.showText(f"\n{x} is not a prime number")
           self.showText("\n\n"+"#"*112+"\n\n")
           return False
           #sys.exit()
        #except:
        #    self.showText("\nERROR: check_prime")
        #    self.showText("\n\n"+"#"*112+"\n\n")


######################################################################################################################################
######################################################################################################################################


    def int_number(self, x):
        x = int(x)
        return x



######################################################################################################################################
######################################################################################################################################


    def check_input(self):
        p_input = self.p.get()
        q_input = self.q.get()
        e_input = self.e.get()

        try:
            if p_input != q_input:
                if (p_input.isdigit() and q_input.isdigit() and e_input.isdigit()):
                    p_input = self.int_number(p_input)
                    q_input = self.int_number(q_input)
                    e_input = self.int_number(e_input)
                    self.check_prime(p_input)
                    self.check_prime(q_input)
                    self.check_prime(e_input)
                    #e_input = self.e_value()

                elif (not p_input.isdigit() and not q_input.isdigit() and not e_input.isdigit()):
                    p_input = self.char_to_decimal(p_input)
                    q_input = self.char_to_decimal(q_input)
                    e_input = self.char_to_decimal(e_input)
                    self.check_prime(p_input)
                    self.check_prime(q_input)
                    self.check_prime(e_input)
                    #e_input = self.e_value()

                elif (p_input.isdigit() and not q_input.isdigit() and not e_input.isdigit()):
                    p_input = self.int_number(p_input)
                    q_input = self.char_to_decimal(q_input)
                    e_input = self.char_to_decimal(e_input)
                    self.check_prime(p_input)
                    self.check_prime(q_input)
                    self.check_prime(e_input)
                    #e_input = self.e_value()


                elif (not p_input.isdigit() and not q_input.isdigit() and e_input.isdigit()):
                    p_input = self.char_to_decimal(p_input)
                    q_input = self.char_to_decimal(q_input)
                    e_input = self.int_number(e_input)
                    self.check_prime(p_input)
                    self.check_prime(q_input)
                    self.check_prime(e_input)
                    #e_input = self.e_value()

                elif (p_input.isdigit() and q_input.isdigit() and not e_input.isdigit()):
                    p_input = self.int_number(p_input)
                    q_input = self.int_number(q_input)
                    e_input = self.char_to_decimal(e_input)
                    self.check_prime(p_input)
                    self.check_prime(q_input)
                    self.check_prime(e_input)
                    #e_input = self.e_value()

                elif (p_input.isdigit() and not q_input.isdigit() and e_input.isdigit()):
                    p_input = self.int_number(p_input)
                    q_input = self.char_to_decimal(q_input)
                    e_input = self.int_number(e_input)
                    self.check_prime(p_input)
                    self.check_prime(q_input)
                    self.check_prime(e_input)
                    #e_input = self.e_value()

                elif (not p_input.isdigit() and q_input.isdigit() and e_input.isdigit()):
                    p_input = self.char_to_decimal(p_input)
                    q_input = self.int_number(q_input)
                    e_input = self.int_number(e_input)
                    self.check_prime(p_input)
                    self.check_prime(q_input)
                    self.check_prime(e_input)
                    #e_input = self.e_value()

                elif (not p_input.isdigit() and q_input.isdigit() and not e_input.isdigit()):
                    p_input = self.char_to_decimal(p_input)
                    q_input = self.int_number(q_input)
                    e_input = self.char_to_decimal(e_input)
                    self.check_prime(p_input)
                    self.check_prime(q_input)
                    self.check_prime(e_input)
                    #e_input = self.e_value()

                else:
                    self.showText("\n\aPlease enter 3 prime numbers and try again :)")
                    self.showText("\n\n"+"#"*112+"\n\n")
                    #sys.exit()
            self.p_input = p_input
            self.q_input = q_input
            self.e_input = e_input

            return self.p_input, self.q_input, self.e_input

        except:
            self.showText("\n\aPlease check that p and q are different prime numbers.:)")
            self.showText("\n\n"+"#"*112+"\n\n")




######################################################################################################################################
######################################################################################################################################


######################################################################################################################################
######################################################################################################################################


    def cipher_text(self):
        message = self.encrypted_message.get()
        ord_message = [ord(i) for i in message]
        return ord_message


######################################################################################################################################
######################################################################################################################################


    def RSA(self):
        #self.n = self.p_input * self.q_input
        Euler = (self.p_input-1) * (self.q_input-1)

        #encryption key
        #e = self.e_input     #e--> encryption
        t = 0
        while(self.e_input < Euler):
            t = math.gcd(self.e_input, Euler)     #gcd --> returns greatest common divisor
            if (t == 1):
                break
            else:
                self.e_input += 1

        #decryption key
        dd = pow(self.e_input, -1)
        d = math.fmod(dd, Euler)    #d--> decryption

        #message = self.cipher_text("I'm 25 years old")
        #message = self.cipher_text()  # 7543116  "mostafa"

        encryption = []
        decryption = []
        ciphering = []
        for i in self.message:
            c = pow(i, self.e_input)    #c --> encrypted message
            m = pow(c, d)          #m --> decrypted message
            c = math.fmod(c, self.n)
            ciphering.append(int(c))
            m = math.fmod(m, self.n)
            m = round(m, 4)
            encryption.append(int(c))
            decryption.append(chr(int(m)))

        encryption_confusing = [str(x) for x in encryption]
        self.encrypted = encryption_confusing
        self.encryption_confusing = ''.join(encryption_confusing)
        self.decryption_confusing = ''.join(decryption)
        self.ciphering = ciphering

        self.showText(f"\n\nEncrypted message: {encryption_confusing}")
        self.showText(f"\nDecrypted message: {self.decryption_confusing}")
        m = ''.join(decryption)




        self.showText(f"\n\n\nThe message we're ciphering is = {ciphering}")
        self.showText(f"\nFirst prime number 'p' is = {self.p_input}")
        self.showText(f"\nSecond prime number 'q' is = {self.q_input}\n")
        self.showText(f"\nn is = {self.n}")
        self.showText(f"\nEuler is = {Euler}")
        self.showText(f"\nprivate key: {dd}\n")
        self.showText(f"\nencryption_key is = {self.e_input}")
        self.showText(f"\ndecryption_key is = {d}")
        self.showText(f"\ndecrypted_message is = {m}")
        self.showText("\n\n"+"#"*224+"\n\n")



######################################################################################################################################
######################################################################################################################################


    def satisfy_conditions(self):
        try:
            self.p_input, self.q_input, self.e_input = self.check_input()
            self.n = self.p_input * self.q_input

            p_prime = self.check_prime(self.p_input)
            q_prime = self.check_prime(self.q_input)
            e_prime = self.check_prime(self.e_input)

            if 1<self.e_input and self.e_input<self.n and self.e_input!=self.p_input and self.e_input!=self.q_input and p_prime and q_prime and e_prime:
                self.message = self.cipher_text()
                self._clear_boxes()
                self.RSA()
                return self.p_input, self.q_input, self.e_input, self.message
                #return self.e_input
            else:
                self.showText("\nPlease check that e value satisfy the conditions.")
                self.showText("\n\n"+"#"*112+"\n\n")
        except:
            self.showText("\nPlease check that you are following rules.")
            self.showText("\n\n"+"#"*112+"\n\n")


######################################################################################################################################
######################################################################################################################################
######################################################################################################################################
######################################################################################################################################


    def _setup_main_window(self):
        # Create an instance of TKinter Window or frame
        self.win.title("RSA Algorithm")
        self.win.bind('<Escape>', lambda e: self.win.quit())

        # Set the size of the window
        w, h = 640, 480
        self.win.geometry(f"{w}x{h}")
        self.win.configure(bg=Background)
        self.win.resizable(width = False, height = False)

    ###############################################################################################################

        # notice
        note = Label(self.win, text="p, q and e must be prime numbers", font=FONT, bg=Background)
        note.place(relwidth=0.5, relheight=0.05, relx=0.25, rely=0.1)

    ###############################################################################################################

        # p input
        self.p = Entry(self.win, width=30) #, bg="black", fg="white", font=FONT2)
        self.p.place(relwidth=0.15, relheight=0.05, relx=0.23, rely=0.2)
        # Create Text Box Label
        self.p_label = Label(self.win, text="p", font=FONT, bg=Background)
        self.p_label.place(relwidth=0.05, relheight=0.05, relx=0.18, rely=0.2)
        #self.p.insert(0, "P")

    ###############################################################################################################

        # q input
        self.q = Entry(self.win, width=30) #, bg="black", fg="white", font=FONT2)
        self.q.place(relwidth=0.15, relheight=0.05, relx=0.65, rely=0.2)
        # Create Text Box Label
        self.q_label = Label(self.win, text="q", font=FONT, bg=Background)
        self.q_label.place(relwidth=0.05, relheight=0.05, relx=0.60, rely=0.2)

    ###############################################################################################################

        # e input
        self.e = Entry(self.win, width=30) #, bg="black", fg="white", font=FONT2)
        self.e.place(relwidth=0.15, relheight=0.07, relx=0.44, rely=0.3)
        # Create Text Box Label
        self.e_label = Label(self.win, text="e", font=FONT, bg=Background)
        self.e_label.place(relwidth=0.05, relheight=0.07, relx=0.39, rely=0.3)

    ###############################################################################################################

        # notice
        note = Label(self.win, text="Message", font=FONT, bg=Background)
        note.place(relwidth=0.3, relheight=0.05, relx=0.35, rely=0.42)

        # output screen
        # to enter your message
        self.encrypted_message = Entry(self.win, bg="white", fg="black", font=FONT2)
        self.encrypted_message.place(relwidth=0.6, relheight=0.05, relx=0.2, rely=0.47)
        self.encrypted_message.insert(0, "Enter message to encrypt:")
        self.encrypted_message.bind("<Button-1>", lambda e: self.entry_clear(self.encrypted_message))


    ###############################################################################################################

        # notice
        note = Label(self.win, text="Output Screen", font=FONT, bg=Background)
        note.place(relwidth=0.22, relheight=0.05, relx=0.39, rely=0.58)

        # encrypted_message & decryption
        # Create text widget and specify size.
        self.output = Text(self.win, bg="white", fg="black", font=FONT2)
        self.output.place(relwidth=0.8, relheight=0.35, relx=0.1, rely=0.63)
        self.output.configure(cursor="arrow")
        # scroll bar
        self.scrollbar = Scrollbar(self.output)
        self.scrollbar.place(relheight=1, relx=0.974)
        self.scrollbar.configure(command=self.output.yview)

    ###############################################################################################################

        # BUTTONS
        # Encrypt
        self.encrypt = Button(self.win, text="Encrypt", font=FONT_BOLD, bg="black", fg="white",
                            command=lambda:self.Encryption())
        self.encrypt.place(relwidth=0.1, relheight=0.11, relx=0.25, rely=0.52)

    ###############################################################################################################
        # decrypt
        self.decrypt = Button(self.win, text="Decrypt", font=FONT_BOLD, bg="black", fg="white",
                            command=lambda:self.Decryption())
        self.decrypt.place(relwidth=0.1, relheight=0.11, relx=0.65, rely=0.52)

    ###############################################################################################################

        # send button
        run_button = Button(self.win, text="Run", font=FONT_BOLD, fg="white", bg="black",
                            command=lambda: self.satisfy_conditions())
        run_button.place(relwidth=0.2, relheight=0.05, relx=0.4, rely=0.53)

######################################################################################################################################
######################################################################################################################################
######################################################################################################################################
######################################################################################################################################

    def Encryption(self):
        try:
            self.showText("\n\n"+"#"*112+"\n\n")
            self.showText(f"\nEncrypted message: {self.encrypted}")
            self.showText(f"\nEncrypted message ciphered: {self.encryption_confusing}")
            self.showText("\n\n"+"#"*112+"\n\n")
        except:
            self.showText("\n\nPlease run first")



    def Decryption(self):
        try:
            self.showText("\n\n"+"#"*112+"\n\n")
            self.showText(f"\nDecrypted message: {self.decryption_confusing}")
            self.showText("\n\n"+"#"*112+"\n\n")
        except:
            self.showText("\n\nPlease run first")



    def entry_clear(self, event):
        if event.get() == "Enter message to encrypt:":
            event.delete(0, END)




    def _on_enter_pressed(self, event):
        msg = self.p.get()
        self.p._insert_message(msg)


    def _clear_boxes(self):
        self.p.delete(0, END)    # to delete the entered message from the enterring tap
        self.q.delete(0, END)
        self.e.delete(0, END)
        self.encrypted_message.delete(0, END)
        #self.output.delete(0, END)
        #self.output.see(END)     # to make program scroll down automatically for the last message


    def showText(self, anyThing):
        self.output.insert(END, anyThing)
        self.output.see(END)     # to make program scroll down automatically for the last message


######################################################################################################################################
######################################################################################################################################


    def run(self):
        self.win.iconbitmap(img)
        self.win.mainloop()


######################################################################################################################################
######################################################################################################################################


    def model(self):
        #self.p_input, self.q_input, self.e_input = self.check_input()
        #self.RSA()
        self.run()


######################################################################################################################################
######################################################################################################################################



if __name__ == "__main__":
    rsa = RSA()
    rsa.model()
