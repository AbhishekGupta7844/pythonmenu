import os
while True:
       
       print(" ______________________________________ " )
       print("Enter What You Want To Open : " , end= '')
       ch = input()
       print(ch)

       if ch == "chrome":
           os.system(r"start C:\Users\dell\AppData\Local\Google\Chrome\Application\chrome.exe")
           
       elif ch == "notepad":
            os.system("notepad")

       elif ch == "control pannel":
            os.system("control.exe")


       elif ch == "This PC":
            os.system('Start "" "%SystemRoot%\explorer.exe" /Select,"This PC"')

       elif ch == "Photos":
           os.system(r"start C:\Users\dell\Pictures\Screenshots")

      