from PyPDF2 import PdfReader
from gtts import gTTS
from tkinter import *
from tkinter import filedialog
import webbrowser

BG_COLOR = "#39B5E0"
save_path_directory = "C:/"
file_path = "C:/"

def get_audio():
    reader = PdfReader(file_path)
    number_of_pages = len(reader.pages)

    all_pages_texts = []
    for i in range(number_of_pages):
        page = reader.pages[i]
        page_texts = page.extract_text()
        all_pages_texts.append(page_texts)
    all_texts = " ".join(all_pages_texts)

    tts = gTTS(all_texts)
    tts.save(save_path_directory)

    title.config(text="done your pdf converted",fg="green")
    webbrowser.open(save_path_directory)

def get_save_pass():
    global save_path_directory
    save_path_directory = filedialog.asksaveasfilename(title="save at",
                                         initialfile="mypdf-audio.mp3",
                                         defaultextension=".mp3",
                                         filetypes=[("music", "*.mp3*")])
    save_path_entry.delete(0,END)
    save_path_entry.insert(0,save_path_directory)

def get_pdf():
    global file_path
    file_path = filedialog.askopenfilename(title="select your pdf",
                                               filetypes=[("pdf file", "*.pdf*")])
    directory_entry.delete(0,END)
    directory_entry.insert(0,file_path)

# ------------------graphical user interface ----------- #
window = Tk()
window.minsize(400,200)
window.config(bg=BG_COLOR,pady=10,padx=10)

title = Label(text="convert your pdf to audio file",font=("arial",25,"bold"),fg="yellow",bg=BG_COLOR)
title.grid(column=0,row=0,columnspan=3,pady=20)

browser_label = Label(text="put pdf directory:",font=("arial",10,"bold"),bg=BG_COLOR)
browser_label.grid(column=0,row=1)
directory_entry = Entry(width=40,font=("arial",10,"bold"))
directory_entry.grid(column=1,row=1,padx=20)
browser_btn = Button(text="browser",width=20,command=get_pdf,bg=BG_COLOR)
browser_btn.grid(column=2,row=1)

save_path = Label(text="page number:",font=("arial",10,"bold"),bg=BG_COLOR)
save_path.grid(column=0,row=2)
save_path_entry = Entry(width=40,font=("arial",10,"bold"))
save_path_entry.grid(column=1,row=2,padx=20)
save_path_browser = Button(text="save at",width=20,command=get_save_pass,bg="green")
save_path_browser.grid(column=2,row=2,pady=10)

generate_audio = Button(text="generate",bg="red",command=get_audio)
generate_audio.grid(column=2,row=3)


window.mainloop()