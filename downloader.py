import tkinter
import customtkinter
import yt_dlp

def startDownload():
    
    try:
        ytlink = link.get()
        
        video = yt_dlp.YoutubeDL({"format": "bestaudio", 'outtmpl': '%(title)s.mp3'})
        video.download(ytlink)
    except:
        print("No download")

    print("Download Complete")

# System Settings 

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

# App frame
app = customtkinter.CTk()
app.geometry("720x480")
app.title("Youtube Downloader")

header = customtkinter.CTkLabel(app, text='Youtube to MP3 Converter')
header.pack(pady = 10)

title = customtkinter.CTkLabel(app, text="Insert a youtube link")
title.pack(padx = 10, pady = 10)




# Link input
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable= url_var)
link.pack()

#Download
download = customtkinter.CTkButton(app, text="Download", command=startDownload)
download.pack(pady = 30)
# Run app
app.mainloop()