import serial.tools.list_ports
import cv2
import keyboard
import numpy as np
import  time
from pygame.midi import Output

#Read File
img = cv2.imread('Testcase7.png', cv2.IMREAD_COLOR)
img = cv2.resize(img, (100,50))
red = cv2.imread('RED.png', cv2.IMREAD_COLOR)
red = cv2.resize(red, (100,50))
Input = cv2.imread('Testcase7.png', cv2.IMREAD_COLOR)
Input = cv2.resize(Input, (300,200))

# Convert the image to gray-scale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Find the edges in the image using canny detector
edges = cv2.Canny(gray, 50, 200)

# Check port connect
ports = serial.tools.list_ports.comports()
serialInst = serial.Serial()
portsList = []

for onePort in ports:
    portsList.append(str(onePort))
    print(str(onePort))

#Find port
val = input("Select Port: COM")

for x in range(0,len(portsList)):
    if portsList[x].startswith("COM" + str(val)):
        portVar = "COM" + str(val)
        print(portVar)

# Set up for UART
serialInst.baudrate = 9600
serialInst.port = portVar
serialInst.open()

#global variable
mess= ""
count = 0;

#Read UART from STM32
def readSerial():
    bytesToRead = serialInst.inWaiting()
    if (bytesToRead > 0):
        global  count
        count= count + 1
        global mess
        mess = mess + serialInst.read(bytesToRead).decode("UTF-8")
        print("---Receiving Data from STM32---")
        # print(mess)
    if (count == 1):
        global Time_Start
        Time_Start =time.time()
    # Start HoughLine
    if ("=" in mess ):
        global Time_StartExcuseinSTM32
        Time_StartExcuseinSTM32=time.time()
        messReset()
    #End HoughLine
    if ("<" in mess ):
        global Time_FinishExcuseinSTM32
        Time_FinishExcuseinSTM32=time.time()
        print("Time Start fuction HoughTransform: ", time.ctime(Time_StartExcuseinSTM32))
        print("Time End function HoughTransForm: ", time.ctime(Time_FinishExcuseinSTM32))
        messReset()
        print("Time STM32 excuse HoughTransforn fuction:")
        print(Time_FinishExcuseinSTM32- Time_StartExcuseinSTM32- 0.005*2,"\n")
    # Start GetLine
    if ("%" in mess ):
        global Time_StartGetLineinSTM32
        Time_StartGetLineinSTM32=time.time()
        messReset()
    #End GetLine
    if (">" in mess ):
        global Time_FinishGetLineinSTM32
        Time_FinishGetLineinSTM32=time.time()
        print("Time Start function GetLine: ", time.ctime(Time_StartGetLineinSTM32))
        print("Time End function GetLine: ", time.ctime(Time_FinishGetLineinSTM32))
        messReset()
        print("Time STM32 excuse Getline():")
        print(Time_FinishGetLineinSTM32- Time_StartGetLineinSTM32- 0.005*2,"\n")
def messReset():
    global mess
    mess = ""
    global count
    count = 0
while True:
    readSerial()
    # end UART
    if("#" in mess):
        Time_End= time.time()
        mess = mess.replace("!", "")
        mess = mess.replace(" ", "")
        mess = mess.replace("#", "")
        mess = mess.replace(":", "")
        print("--------------DONE--------------")
        #Time
        print("Time Start Receive Data: ", time.ctime(Time_Start) )
        print("Time End Receive Data: ", time.ctime(Time_End) )
        print("Time UART data:")
        print(Time_End-Time_Start,"\n")
        break

# Output picture self:
for i in range(50):
    for j in range(100):
        if(mess[200*i + 2*j+1] == "0"):
            red[i][j] = 0;

Line_STM32 = cv2.addWeighted(img,0.8 ,red,1,1)
Line_STM32 = cv2.resize(Line_STM32, (300,200))
minLineLength = 10
maxLineGap = 5

# Linedection by OpenCV
Time_PythonStart = time.time()
lines = cv2.HoughLinesP(edges,1,np.pi/180,10,minLineLength=minLineLength,maxLineGap=maxLineGap)
for x in range(0, len(lines)):
    for x1,y1,x2,y2 in lines[x]:
        cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)
img = cv2.resize(img, (300,200))
Time_PythonEnd = time.time()


# Compare
Compare = np.concatenate((Input, Line_STM32, img), axis=1)
cv2.imshow("Compare Result Image", Compare)
k = cv2.waitKey(0)

print(Time_PythonStart)
print(Time_PythonEnd)
print("Time Python Start: ", time.ctime(Time_PythonStart))
print("Time Python End: ", time.ctime(Time_PythonEnd))
print("Time Python excute: ")
print(Time_PythonEnd - Time_PythonStart,"\n")
Time_python = Time_PythonEnd - Time_PythonStart
print("Time excuse in STM32: ")
TimeSTM32 = (Time_FinishExcuseinSTM32-Time_StartExcuseinSTM32)+(Time_FinishGetLineinSTM32- Time_StartGetLineinSTM32)
print(TimeSTM32,"\n")
print("Hieu nang he thong: Phan mem xu li tren Python nhanh hon phan cung: ")
print(TimeSTM32/Time_python)


cv2.destroyAllWindows()