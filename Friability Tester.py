# import satements and object creation
import serial
import serial.tools.list_ports
import tkinter
from tkinter import *
from tkinter import messagebox
root = Tk()
root.geometry('800x800')
root.title("Friability Tester")

#data 
serials = {}
s = IntVar()

def connectToSerial():
    print(serials)
    for k, v in serials.items():
        if v == s.get():
            global connectPort 
            connectPort = k
            print(connectPort)
            connectBTN.configure(bg='green', text='CONNECTED')
            

def getH(isLeft):
    if isLeft:
        if not hours_left.get():
            return ''
        if len(hours_left.get()) == 1:
            return '0' + hours_left.get()
        return hours_left.get()
    else:
        if not hours_right.get():
            return ''
        if len(hours_right.get()) == 1:
            return '0' + hours_right.get()
        return hours_right.get()


def getM(isLeft):
    if isLeft:
        if not mins_left.get():
            return ''
        if len(mins_left.get()) == 1:
            return '0' + mins_left.get()
        return mins_left.get()
    else:
        if not mins_right.get():
            return ''
        if len(mins_right.get()) == 1:
            return '0' + mins_right.get()
        return mins_right.get()


def getS(isLeft):
    if isLeft:
        if not secs_left.get():
            return ''
        if len(secs_left.get()) == 1:
            return '0' + secs_left.get()
        return secs_left.get()
    else:
        if not secs_right.get():
            return ''
        if len(secs_right.get()) == 1:
            return '0' + secs_right.get()
        return secs_right.get()


def getRev(isLeft):
    if isLeft:
        if not revs_left.get():
            return ''
        if len(revs_left.get()) == 1:
            return '00' + revs_left.get()
        if len(revs_left.get()) == 2:
            return '0' + revs_left.get()
        return revs_left.get()
    else:
        if not revs_right.get():
            return ''
        if len(revs_right.get()) == 1:
            return '00' + revs_right.get()
        if len(revs_right.get()) == 1:
            return '0' + revs_right.get()
        return revs_right.get()


def getRpm(isLeft):
    if isLeft:
        if not rpm_left.get():
            return ''
        if len(rpm_left.get()) == 1:
            return '00' + rpm_left.get()
        if len(rpm_left.get()) == 2:
            return '0' + rpm_left.get()
        return rpm_left.get()
    else:
        if not rpm_right.get():
            return ''
        if len(rpm_right.get()) == 1:
            return '00' + rpm_right.get()
        if len(rpm_right.get()) == 2:
            return '0' + rpm_right.get()
        return rpm_right.get()


def get_ports():

    ports = serial.tools.list_ports.comports()
    return ports


def selectSerial(foundPorts):
    numConnection = len(foundPorts)

    for i in range(0, numConnection):
        port = foundPorts[i]
        strPort = str(port)
        serials[strPort.split(' ')[0]] = i
        Radiobutton(root, text=strPort.split(' ')[2], padx=5, variable=s, value=i).place(x=100*(i+1), y=11)


def writeToSerial():
    # Generating data and Validating
    if drum.get() == 0 or inputType.get() == 0:
        print('Feilds empty!')
        return

    hLeft = getH(True)
    mLeft = getM(True)
    sLeft = getS(True)
    revLeft = getRev(True)
    rpmLeft = getRpm(True)
    hRight = getH(False)
    mRight = getM(False)
    sRight = getS(False)
    revRight = getRev(False)
    rpmRight = getRpm(False)

    if drum.get() == 1:
        if inputType.get() == 1:
            if not revs_left.get() or not hours_left.get() or not mins_left.get() or not secs_left.get():
                print('Feilds Empty!')
                return
            data = '1' + ',' + hLeft + ',' + mLeft + ',' + sLeft + ',' + revLeft + ',' + '000' + '\n'
        if inputType.get() == 2:
            if not rpm_left.get() or not hours_left.get() or not mins_left.get() or not secs_left.get():
                print('Feilds Empty!')
                return
            data = '1' + ',' + hLeft + ',' + mLeft + ',' + sLeft + ',' + '000' + ',' + rpmLeft + '\n'

    if drum.get() == 2:
        if inputType.get() == 1:
            if not revs_right.get() or not hours_right.get() or not mins_right.get() or not secs_right.get():
                print('Feilds Empty!')
                return
            data = '2' + ',' + hRight + ',' + mRight + ',' + sRight + ',' + revRight + ',' + '000' + '\n'
        if inputType.get() == 2:
            if not rpm_right.get() or not hours_right.get() or not mins_right.get() or not secs_right.get():
                print('Feilds Empty!')
                return
            data = '2' + ',' + hRight + ',' + mRight + ',' + sRight + ',' + '000' + ',' + rpmRight + '\n'

    if drum.get() == 3:
        if inputType.get() == 1:
            if not revs_right.get() or not hours_right.get() or not mins_right.get() or not secs_right.get() or not revs_left.get() or not hours_left.get() or not mins_left.get() or not secs_left.get():
                print('Feilds Empty!')
                return
            data = '2' + ',' + hRight + ',' + mRight + ',' + sRight + ',' + revRight + ',' + '000' + '\n' + '1' + ',' + hLeft + ',' + mLeft + ',' + sLeft + ',' + revLeft + ',' + '000' + '\n'
        if inputType.get() == 2:
            if not rpm_right.get() or not hours_right.get() or not mins_right.get() or not secs_right.get() or not rpm_left.get() or not hours_left.get() or not mins_left.get() or not secs_left.get():
                print('Feilds Empty!')
                return
            data = '2' + ',' + hRight + ',' + mRight + ',' + sRight + ',' + '000' + ',' + rpmRight + '\n' + '1' + ',' + hLeft + ',' + mLeft + ',' + sLeft + ',' + '000' + ',' + rpmLeft + '\n'


    if connectPort != 'None':
        ser = serial.Serial(connectPort, baudrate=9600)
        print('Connected to ' + ser.name)
        print(ser.is_open)
        print(data)
        print(ser.write(data.encode()))
        messagebox.showinfo('information', 'Data Sent')
        ser.close()

    else:
        print(connectPort)
        print('Connection Issue!')

    print('DONE')


def enableAll():
    if inputType.get() == 1:
        revs_right.configure(state="normal")
        revs_right.update()
        revs_left.configure(state="normal")
        revs_left.update()
        rpm_right.configure(state="disabled")
        rpm_right.update()
        rpm_left.configure(state="disabled")
        rpm_left.update()
    elif inputType.get() == 2:
        revs_right.configure(state="disabled")
        revs_right.update()
        revs_left.configure(state="disabled")
        revs_left.update()
        rpm_right.configure(state="normal")
        rpm_right.update()
        rpm_left.configure(state="normal")
        rpm_left.update()
    hours_right.configure(state="normal")
    hours_right.update()
    mins_right.configure(state="normal")
    mins_right.update()
    secs_right.configure(state="normal")
    secs_right.update()
    hours_left.configure(state="normal")
    hours_left.update()
    mins_left.configure(state="normal")
    mins_left.update()
    secs_left.configure(state="normal")
    secs_left.update()


def disbaleRight():
    if inputType.get() == 1:
        revs_right.configure(state="disabled")
        revs_right.update()
        revs_left.configure(state="normal")
        revs_left.update()
        rpm_right.configure(state="disabled")
        rpm_right.update()
        rpm_left.configure(state="disabled")
        rpm_left.update()
    elif inputType.get() == 2:
        revs_right.configure(state="disabled")
        revs_right.update()
        revs_left.configure(state="disabled")
        revs_left.update()
        rpm_right.configure(state="disabled")
        rpm_right.update()
        rpm_left.configure(state="normal")
        rpm_left.update()
    hours_right.configure(state="disabled")
    hours_right.update()
    mins_right.configure(state="disabled")
    mins_right.update()
    secs_right.configure(state="disabled")
    secs_right.update()
    hours_left.configure(state="normal")
    hours_left.update()
    mins_left.configure(state="normal")
    mins_left.update()
    secs_left.configure(state="normal")
    secs_left.update()


def disbaleLeft():
    if inputType.get() == 1:
        revs_right.configure(state="normal")
        revs_right.update()
        revs_left.configure(state="disabled")
        revs_left.update()
        rpm_right.configure(state="disabled")
        rpm_right.update()
        rpm_left.configure(state="disabled")
        rpm_left.update()
    elif inputType.get() == 2:
        revs_right.configure(state="disabled")
        revs_right.update()
        revs_left.configure(state="disabled")
        revs_left.update()
        rpm_right.configure(state="normal")
        rpm_right.update()
        rpm_left.configure(state="disabled")
        rpm_left.update()
    hours_left.configure(state="disabled")
    hours_left.update()
    mins_left.configure(state="disabled")
    mins_left.update()
    secs_left.configure(state="disabled")
    secs_left.update()
    hours_right.configure(state="normal")
    hours_right.update()
    mins_right.configure(state="normal")
    mins_right.update()
    secs_right.configure(state="normal")
    secs_right.update()


def disableRevs():
    revs_left.configure(state="disabled")
    revs_left.update()
    revs_right.configure(state="disabled")
    revs_right.update()
    if drum.get() == 1:
        rpm_left.configure(state="normal")
        rpm_left.update()
        rpm_right.configure(state="disabled")
        rpm_right.update()
    elif drum.get() == 2:
        rpm_left.configure(state="disabled")
        rpm_left.update()
        rpm_right.configure(state="normal")
        rpm_right.update()
    else:
        rpm_left.configure(state="normal")
        rpm_left.update()
        rpm_right.configure(state="normal")
        rpm_right.update()


def disableRPM():
    rpm_left.configure(state="disabled")
    rpm_left.update()
    rpm_right.configure(state="disabled")
    rpm_right.update()
    if drum.get() == 1:
        revs_left.configure(state="normal")
        revs_left.update()
        revs_right.configure(state="disabled")
        revs_right.update()
    elif drum.get() == 2:
        revs_left.configure(state="disabled")
        revs_left.update()
        revs_right.configure(state="normal")
        revs_right.update()
    else:
        revs_left.configure(state="normal")
        revs_left.update()
        revs_right.configure(state="normal")
        revs_right.update()


def validateRev(rev):
    if rev.isdigit() and int(rev, 10) >= 0 and int(rev, 10) <= 999:
        return True
    elif rev == '':
        return True
    else:
        return False


def validateRPM(rpm):
    if rpm.isdigit() and int(rpm, 10) >= 0 and int(rpm, 10) <= 100:
        return True
    elif rpm == "":
        return True
    else:
        return False


def validateHH(h):
    if h.isdigit() and int(h, 10) >= 0 and int(h, 10) <= 23:
        return True
    elif h == '':
        return True
    else:
        return False


def validateMM(m):
    if m.isdigit() and int(m, 10) >= 0 and int(m, 10) <= 59:
        return True
    elif m == '':
        return True
    else:
        return False


def validateSS(s):
    if s.isdigit() and int(s, 10) >= 0 and int(s, 10) <= 59:
        return True
    elif s == '':
        return True
    else:
        return False


# Heading of the form
label_0 = Label(root, text="Friability Tester", width=20, font=("bold", 30))
label_0.place(x=190, y=53)

#com-port label
com_port_label = Label(root, text='COM-Port', width=12, font=("bold", 10));
com_port_label.place(x = 1, y = 11)

# Drum Selection
label_1 = Label(root, text="Select Drum", width=20, font=("bold", 13))
label_1.place(x=120, y=130)
drum = IntVar()
Radiobutton(root, text="Left Drum", padx=5, variable=drum,
            value=1, command=disbaleRight).place(x=285, y=130)
Radiobutton(root, text="Both Drums", padx=20, variable=drum,
            value=3, command=enableAll).place(x=390, y=130)
Radiobutton(root, text="Right Drum", padx=35, variable=drum,
            value=2, command=disbaleLeft).place(x=495, y=130)

# Input Type Selection
inputType = IntVar()

# Input Revolutions
Radiobutton(root, text="", padx=5, variable=inputType,
            value=1, command=disableRPM).place(x=150, y=180)
revs = Label(root, text="Revolutions", width=10, font=("bold", 13))
revs.place(x=170, y=180)
revs_left = Entry(root, width=20, state='disabled')
revs_left.place(x=285, y=180)
regRev = root.register(validateRev)
revs_left.config(validate="key",  validatecommand=(regRev, '%P'))
revs_right = Entry(root, width=20, state='disabled')
revs_right.place(x=480, y=180)
revs_right.config(validate="key",  validatecommand=(regRev, '%P'))

# Input RPM
Radiobutton(root, text="", padx=5, variable=inputType,
            value=2, command=disableRevs).place(x=150, y=230)
rpm = Label(root, text="RPM [20-60]", width=10, font=("bold", 13))
rpm.place(x=170, y=230)
rpm_left = Entry(root, width=20, state='disabled')
rpm_left.place(x=285, y=230)
regRPM = root.register(validateRPM)
rpm_left.config(validate="key",  validatecommand=(regRPM, '%P'))
rpm_right = Entry(root, width=20, state='disabled')
rpm_right.place(x=480, y=230)
rpm_right.config(validate="key", validatecommand=(regRPM, '%P'))

# Runtime Label
runtime_label = Label(root, text="Enter Runtime", width=20, font=("bold", 13))
runtime_label.place(x=120, y=280)

# Hours Input
hours_left = Entry(root, width=20, state='disabled')
hours_left.place(x=285, y=330)
regHH = root.register(validateHH)
hours_left.config(validate="key",  validatecommand=(regHH, '%P'))
hours_label = Label(root, text="HH", width=2, font=("bold", 8))
hours_label.place(x=420, y=330)
hours_right = Entry(root, width=20, state='disabled')
hours_right.place(x=480, y=330)
hours_right.config(validate="key", validatecommand=(regHH, '%P'))
hours_label = Label(root, text="HH", width=2, font=("bold", 8))
hours_label.place(x=610, y=330)


# Minutes Input
mins_left = Entry(root, width=20, state='disabled')
mins_left.place(x=285, y=380)
regMM = root.register(validateMM)
mins_left.config(validate="key",  validatecommand=(regMM, '%P'))
mins_label = Label(root, text="MM", width=2, font=("bold", 8))
mins_label.place(x=420, y=380)
mins_right = Entry(root, width=20, state='disabled')
mins_right.place(x=480, y=380)
mins_right.config(validate="key",  validatecommand=(regMM, '%P'))
mins_label = Label(root, text="MM", width=2, font=("bold", 8))
mins_label.place(x=610, y=380)


# Seconds Input
secs_left = Entry(root, width=20, state='disabled')
secs_left.place(x=285, y=430)
regSS = root.register(validateSS)
secs_left.config(validate="key",  validatecommand=(regSS, '%P'))
secs_label = Label(root, text="SS", width=2, font=("bold", 8))
secs_label.place(x=420, y=430)
secs_right = Entry(root, width=20, state='disabled')
secs_right.place(x=480, y=430)
secs_right.config(validate="key",  validatecommand=(regSS, '%P'))
secs_label = Label(root, text="SS", width=2, font=("bold", 8))
secs_label.place(x=610, y=430)


# Send Button
Button(root, text='SEND', width=20, height=1, bg='brown', fg='white', command=writeToSerial).place(x=350, y=530)

# connect Button
connectBTN = Button(root, text='CONNECT', width=14, height=1, bg='brown', fg='white', command=connectToSerial)
connectBTN.pack()
connectBTN.place(x=680, y=11)



# logo
companyLogo = Label(root, text='Kaywo', width=20, font=("bold", 15))
companyLogo.place(x=300, y=600)
companyWebsite = Label(root, text='www.kaywolabs.com',
                       width=20, font=("bold", 13))
companyWebsite.place(x=320, y=627)
companyName = Label(root, text='KUMAR INSTRUMENTS CO.',
                    width=40, font=("bold", 15))
companyName.place(x=205, y=655)
companyAddress = Label(root, text='AMBALA CANTT', width=20, font=("bold", 13))
companyAddress.place(x=320, y=680)

# Getting ports and writing data
foundPorts = get_ports()
selectSerial(foundPorts)

# run application
root.mainloop()
