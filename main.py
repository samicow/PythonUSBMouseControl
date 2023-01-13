
import serial
import threading
import win32api, win32con
import time
#import time

#counting = False


# def stopWatchHandler():
#     global couting
#     day = 0
#     hour = 0
#     min = 0
#     sec = 0
#     print("D - H - M - S")
#     while(True):
#         time.sleep(1)
#         if(counting == True):
#
#                 if sec == 59:
#                     sec=-1
#                     min=min+1
#
#                 sec=sec+1
#                 if min == 60:
#                     min = 0
#                     hour = hour +1
#                 if hour == 24:
#                     hour = 0
#                     day = day + 1
#                 print(day,"-", hour,"-", min, "-",sec)

mouseX= 500
mouseY= 500

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)
click(10,10)

def receiveHandler():
   global counting;
   global mouseX, mouseY
   while(True):  #fazendo leitura
    response = ser.readline()         #RECEBE WELC; set = porta
    #print("thread\r\n")
    if len(response) > 0:
         strResponse = response.decode('utf-8');
         strResponse = strResponse[3:]
         ACC = strResponse.split(",")
         ACCX = ACC[0]
         ACCX = int(ACCX[3:])

         ACCY = ACC[1]
         ACCY = int(ACCY[3:])

         ACCZ = ACC[2]
         ACCZ = int(ACCZ[3:])

         print(ACCX)

         if ACCX > 400:
            mouseX = mouseX + 10
         elif ACCX < -400:
            mouseX = mouseX - 10

         if ACCY > 400:
            mouseY = mouseY + 10
         elif ACCY < -400:
            mouseY = mouseY - 10
         # for s in ACC:
         #     s = s[1:]
         #     print(s)

        # if(strResponse == "XXEA\r\n"):
        #     counting = not counting;
        # print("response = {}".format(strResponse));

#def txHandler():
 #   ser.write(b'hi');  # ENVIA HI

def controlTheMouse():
    counter = 1000
    while(counter > 0):
        win32api.SetCursorPos((mouseX,mouseY))
        counter = counter -1
        time.sleep(0.01);
        print("mouse released and stopped")




ser = serial.Serial('COM43', baudrate=115200,  timeout= 2) #name,
print(ser.name)  # COM43 check which port was really used
print("teste\r\n")

ser.write(b'hi')  #ENVIA HI

t= threading.Thread(target=receiveHandler)
t1 = threading.Thread(target=controlTheMouse)
t.start();
#t2= threading.Thread(target=stopWatchHandler)

#print("teste2\r\n")
#t2= threading.Thread(target=txHandler())

#t.join();


#t2.start();
#counting= False;
#print("press the button to start the stopwatch\r\n")

t1.start();



ser.write(b'hi')
