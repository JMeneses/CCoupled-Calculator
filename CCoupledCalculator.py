from tkinter import * 
from tkinter.ttk import *
from tkinter import messagebox
from PIL import ImageTk,Image
import CCoupledScript

# 0. Callback Fuctions
def callback(input):
    if input.isdigit():
        print(input)
        return True
                        
    elif input is "":
        print(input)
        messagebox.askquestion("askquestion", "All fields are required!")
        return True

    else:
        print(input)
        return False


def TextBoxUpdate(event):
    if (signalchosen.current()==0):
        txt_t.config(state='disabled')
        lbl_t.config(state='disabled')
        txt_f.config(state='enabled')
        lbl_f.config(state='enabled')
        canvas.itemconfig(image_id, image=img)
    else:
        txt_t.config(state='enabled')
        lbl_t.config(state='enabled')
        txt_f.config(state='disabled')
        lbl_f.config(state='disabled')
        canvas.itemconfig(image_id, image=img2)
    return True

def callback_cm(input):
    if float(input)>=1 and float(input)<=2:
        return True
    else:
        messagebox.showwarning(title="Unusual Values", message="Culture Medium conductivity values are usually between 1-2 S/m.")
        return False

def buttonpress():
    global details_reported_str
    if (signalchosen.current()==0):
        pulsebool = False
    else:
        pulsebool = True
    
    result_str, details_str = CCoupledScript.calculate_electric_field(float(txt_r.get()),
                                                                      float(txt_i1_c.get()),
                                                                      float(txt_i1_e.get()),
                                                                      float(txt_i1_h.get()),
                                                                      float(txt_cm_c.get()),
                                                                      float(txt_cm_e.get()),
                                                                      float(txt_cm_h.get()),
                                                                      float(txt_i2_c.get()),
                                                                      float(txt_i2_e.get()),
                                                                      float(txt_i2_h.get()),
                                                                      float(txt_f.get()),
                                                                      float(txt_v.get()),
                                                                      pulsebool,
                                                                      float(txt_t.get()))
    print(result_str)
    results.configure(text=result_str)
    lbl_res.configure(text="Electric Field in the Culture Medium:")
    details_reported_str = details_str

def about():
    newWindow = Toplevel(root)
    newWindow.title("About this CCoupled EF Calculator")
    newWindow.geometry("560x420")
    Label(newWindow,text="This software (version:1.0.04.11.2021) was created as part of a research article entitled \'How to (correctly) estimate the Electric Field in Capacitively Coupled Systems\'. The main results of this study were published in\n(add reference here). Please cite this paper if you use this software in your research work.\n\nThis software is released online under GNU General Public License v3 (GPL-3) license. It is provided \'as is\'\nand \'as available\' without representations, warranties, or conditions of any kind. Its authors or the\ninstitutions that they represent accept no liability or responsibility for any direct, indirect, incidental,\nspecial or consequential damages, or loss of profits that result from the use or inability to use this\napplication.\n\nThis software is a product of a project funded by Fundação para a Ciência e Tecnologia (FCT) and\nCentro2020 through the following grants: CDRSP UIDP/04044/2020, UIDB/04044/2020, Stimuli2BioScaffold\nPTDC/EMESIS/32554/2017, IBEB UIDB/00645/2020 and under FCT PhD grant 2021.05145.BD.\n", justify=LEFT).pack()
    canvasFCT = Canvas(newWindow, width=551, height=185)
    imageFCT = ImageTk.PhotoImage(Image.open("Logos.png"))
    canvasFCT.create_image(5, 5, anchor=NW, image=imageFCT)
    canvasFCT.pack()
    newWindow.mainloop()
    print("License")

def openDetailsWindow():
    newWindow = Toplevel(root)
    newWindow.title("Electric Field Calculation Details")
    newWindow.geometry("350x380")
    Label(newWindow,text=details_reported_str).pack()
    print("Details")

def setBrighton():
    defaultDatasetIsBrighton = True
    txt_r.delete(0, 'end')
    txt_i1_c.delete(0, 'end')
    txt_i1_e.delete(0, 'end')
    txt_i1_h.delete(0, 'end')
    txt_cm_c.delete(0, 'end')
    txt_cm_e.delete(0, 'end')
    txt_cm_h.delete(0, 'end')
    txt_i2_c.delete(0, 'end')
    txt_i2_e.delete(0, 'end')
    txt_i2_h.delete(0, 'end')
    txt_v.delete(0, 'end')
    txt_t.delete(0, 'end')
    txt_f.delete(0, 'end')
    txt_r.insert(0, "16.5")
    txt_i1_c.insert(0, "1.0E-13")
    txt_i1_e.insert(0, "6.85")
    txt_i1_h.insert(0, "0.16")
    txt_cm_c.insert(0, "1.5")
    txt_cm_e.insert(0, "80.1")
    txt_cm_h.insert(0, "9.8")
    txt_i2_c.insert(0, "1E-13")
    txt_i2_e.insert(0, "6.85")
    txt_i2_h.insert(0, "0.16")
    txt_v.insert(0, "44.81")
    txt_t.insert(0, "0.000000045")
    txt_f.insert(0, "60000")
    signalchosen.current(0)
    txt_t.config(state='disabled')
    lbl_t.config(state='disabled')
    txt_f.config(state='enabled')
    lbl_f.config(state='enabled')
    canvas.itemconfig(image_id, image=img)
    print("Set Default Dataset Brigthon")

def setHartig():
    defaultDatasetIsBrighton = False
    txt_r.delete(0, 'end')
    txt_i1_c.delete(0, 'end')
    txt_i1_e.delete(0, 'end')
    txt_i1_h.delete(0, 'end')
    txt_cm_c.delete(0, 'end')
    txt_cm_e.delete(0, 'end')
    txt_cm_h.delete(0, 'end')
    txt_i2_c.delete(0, 'end')
    txt_i2_e.delete(0, 'end')
    txt_i2_h.delete(0, 'end')
    txt_v.delete(0, 'end')
    txt_t.delete(0, 'end')
    txt_f.delete(0, 'end')
    txt_r.insert(0, "65.0")
    txt_i1_c.insert(0, "1.0E-14")
    txt_i1_e.insert(0, "1.005")
    txt_i1_h.insert(0, "2.00")
    txt_cm_c.insert(0, "1.5")
    txt_cm_e.insert(0, "80.1")
    txt_cm_h.insert(0, "2.50")
    txt_i2_c.insert(0, "6.7E-14")
    txt_i2_e.insert(0, "2.50")
    txt_i2_h.insert(0, "1.00")
    txt_v.insert(0, "100")
    txt_t.insert(0, "0.000000045")
    txt_f.insert(0, "60000")
    signalchosen.current(1)
    txt_t.config(state='enabled')
    lbl_t.config(state='enabled')
    txt_f.config(state='disabled')
    lbl_f.config(state='disabled')
    canvas.itemconfig(image_id, image=img2)
    print("Set Default Dataset Hartig")

# 1. Main Window
root = Tk()
root.title("E-Field Calculator for CCoupled Systems")
root.geometry('800x500')
root.columnconfigure(0, weight=3)
root.columnconfigure(1, weight=2)

# 1.1 Add Menu Bar
menubar = Menu(root)
menubar.add_command(label="About", command=about)

# 1.2 Add Option Menu
defaultDatasetIsBrighton = True 
menu_options = Menu(menubar)
menubar.add_cascade(label="Default Dataset", menu=menu_options)
menu_options.add_radiobutton(label="Brighton et al. 1992", command=setBrighton)
menu_options.add_radiobutton(label="Hartig et al. 2000", command=setHartig)

# 2. Add Grid Structure
frame = LabelFrame(root, text="Layers Parameters", width=430)
frame.grid(row=0, column=0, sticky='NSEW')
canvas = Canvas(root, width=300, height=300)  
canvas.grid(row=0, column=1, sticky='NSEW')
frame2 = LabelFrame(root, text="Signal Parameters", width=450)
frame2.grid(row=1, column=0, sticky='NSEW')
frame3 = LabelFrame(root, text="Results", width=430)
frame3.grid(row=1, column=1, sticky='NSEW')



# Add Image
img = ImageTk.PhotoImage(Image.open("Img_Calculator_Sin.png"))
img2 = ImageTk.PhotoImage(Image.open("Img_Calculator_Ramp.png")) 
image_id = canvas.create_image(20, 20, anchor=NW, image=img) 


#--------
# FRAME 1
#--------
# 1.0 Adding Label and Entry Widgets
txt_r = Entry(frame, width=10)
txt_r.grid(column=0, row=0, sticky='w')
txt_r.insert(0, "16.5")
lbl_r = Label(frame, text="Radius - common to all layers (mm)                                           ")
lbl_r.grid(column=1, row=0, sticky='we')

style = Style()
style.configure("Line.TSeparator", background="black")
style.configure('Culture.TLabel', background='#6fa8dc')
style.configure('Electrode.TLabel', background='#d9d9d9')

separator_1 = Separator(frame, orient=HORIZONTAL, style="Line.TSeparator")
separator_1.grid(column=0, row=1, columnspan=2, sticky=(W,E), pady=10)
lbl_s1 = Label(frame, text = "Top Electric Insulator:", style='Electrode.TLabel')
lbl_s1.grid(column=0, row=2, columnspan=2, sticky=(W,E))

txt_i1_c = Entry(frame, width=10)
txt_i1_c.grid(column=0, row=3, sticky='we')
txt_i1_c.insert(0, "1.0E-13")
lbl_i1_c = Label(frame, text = "Electric Conductivity (S/m)", style='Electrode.TLabel')
lbl_i1_c.grid(column=1, row=3, sticky='we')

txt_i1_e = Entry(frame, width=10)
txt_i1_e.grid(column=0, row=4, sticky='we')
txt_i1_e.insert(0, "6.85")
lbl_i1_e = Label(frame, text = "Relative Permitivitty", style='Electrode.TLabel')
lbl_i1_e.grid(column=1, row=4, sticky='we')

txt_i1_h = Entry(frame, width=10)
txt_i1_h.grid(column=0, row=5, sticky='we')
txt_i1_h.insert(0, "0.16")
lbl_i1_h = Label(frame, text = "Layer Height (mm)", style='Electrode.TLabel')
lbl_i1_h.grid(column=1, row=5, sticky='we')

separator_2 = Separator(frame, orient=HORIZONTAL, style="Line.TSeparator")
separator_2.grid(column=0, row=6, columnspan=2, sticky=(W,E), pady=10)
lbl_s2 = Label(frame, text = "Culture Medium:", style="Culture.TLabel")
lbl_s2.grid(column=0, row=7, columnspan=2, sticky=(W,E))

txt_cm_c = Entry(frame, width=10)
txt_cm_c.grid(column=0, row=8, sticky='we')
txt_cm_c.insert(0, "1.5")
lbl_cm_c = Label(frame, text = "Electric Conductivity (S/m)", style="Culture.TLabel")
lbl_cm_c.grid(column=1, row=8, sticky='we')

txt_cm_e = Entry(frame, width=10)
txt_cm_e.grid(column=0, row=9, sticky='we')
txt_cm_e.insert(0, "80.1")
lbl_cm_e = Label(frame, text = "Relative Permitivitty", style="Culture.TLabel")
lbl_cm_e.grid(column=1, row=9, sticky='we')

txt_cm_h = Entry(frame, width=10)
txt_cm_h.grid(column=0, row=10, sticky='we')
txt_cm_h.insert(0, "9.8")
lbl_cm_h = Label(frame, text = "Layer Height (mm)", style="Culture.TLabel")
lbl_cm_h.grid(column=1, row=10, sticky='we')

separator_3 = Separator(frame, orient=HORIZONTAL, style="Line.TSeparator")
separator_3.grid(column=0, row=11, columnspan=2, sticky=(W,E), pady=10)
lbl_s3 = Label(frame, text = "Bottom Electric Insulator:", style='Electrode.TLabel')
lbl_s3.grid(column=0, row=12, columnspan=2, sticky=(W,E))

txt_i2_c = Entry(frame, width=10)
txt_i2_c.grid(column=0, row=13, sticky='we')
txt_i2_c.insert(0, "1E-13")
lbl_i2_c = Label(frame, text = "Electric Conductivity (S/m)", style='Electrode.TLabel')
lbl_i2_c.grid(column=1, row=13, sticky='we')

txt_i2_e = Entry(frame, width=10)
txt_i2_e.grid(column=0, row=14, sticky='we')
txt_i2_e.insert(0, "6.85")
lbl_i2_e = Label(frame, text = "Relative Permitivitty", style='Electrode.TLabel')
lbl_i2_e.grid(column=1, row=14, sticky='we')

txt_i2_h = Entry(frame, width=10)
txt_i2_h.grid(column=0, row=15, sticky='we')
txt_i2_h.insert(0, "0.16")
lbl_i2_h = Label(frame, text = "Layer Height (mm)", style='Electrode.TLabel')
lbl_i2_h.grid(column=1, row=15, sticky='we')

#--------
# FRAME 2
#--------
n = StringVar()
signalchosen = Combobox(frame2, width = 20, textvariable = n)
signalchosen['values'] = (' Sinusoidal',' Ramp')
signalchosen['state'] = 'readonly'
signalchosen.current(0)
signalchosen.grid(column = 0, row = 0, sticky='w')
signalchosen.current()
lbl_wave = Label(frame2, text = "Waveform Selection")
lbl_wave.grid(column=1, row=0, sticky='w')

txt_t = Entry(frame2, width=20)
txt_t.grid(column=0, row=1, sticky='w')
txt_t.insert(0, "0.000000045")
txt_t.config(state='disabled')
lbl_t = Label(frame2, text="Rise/Fall Time (s)", state='disabled')
lbl_t.grid(column=1, row=1, sticky='w')

txt_f = Entry(frame2, width=20)
txt_f.grid(column=0, row=2, sticky='w')
txt_f.insert(0, "60000")
lbl_f = Label(frame2, text="Frequency (Hz)")
lbl_f.grid(column=1, row=2, sticky='w')

txt_v = Entry(frame2, width=20)
txt_v.grid(column=0, row=3, sticky='w')
txt_v.insert(0, "44.81")
lbl_v = Label(frame2, text="Voltage Amplitude (V)")
lbl_v.grid(column=1, row=3, sticky='w')



# 4. Register the callback function
reg_cm = root.register(callback_cm)
txt_cm_c.config(validate="focusout", validatecommand=(reg_cm, '%P'))
signalchosen.bind("<<ComboboxSelected>>", TextBoxUpdate)

# 5. Button panel to calculate
panel = Frame(frame3)
panel.pack(fill = BOTH, expand = True)

btn_calc = Button(panel, text ="Calculate", command = buttonpress)
btn_calc.pack(side = LEFT, expand = True, fill = BOTH)

details_reported_str = "Empty, please run Calculation before opening Details"
btn_details = Button(panel, text ="Details", command = openDetailsWindow)
btn_details.pack(side = LEFT, expand = True, fill = BOTH)

# 6. Show Results
lbl_res = Label(frame3, text = "INFO: Press Calculate to obain the Electric Field prediction...")
lbl_res.pack(side = TOP)

results = Label(frame3, text="", font=("Arial", 25))
results.pack(side = TOP)

# Tkinter event loop
root.config(menu=menubar)
root.mainloop()