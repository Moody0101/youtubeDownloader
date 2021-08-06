from tkinter import LabelFrame, Label, Button, Tk, Entry

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Author : Moody0101
# version: 0.0.1
# github: github.com/Moody0101
# the Youtube downloader section
# just be cause I could not import it, so it made me mad, so it is better to copy it and paste
# dependencies are  { pafy, youtube-dl, os, Tkinter}
# to know how to use the YoutubeDownloader class you can go to this repo
# www.github.com/Moody0101/youtubeDownloader

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
from pafy import new
from pprint import pprint
from os import path, mkdir, chdir


def createdir(arg0: str):
    if not path.exists(arg0):
        mkdir(arg0)
        chdir(arg0)


class youtubeDownloader:
    def __init__(self, url):
        self.url = url
        self.video = new(self.url)
        self.stats = self.displayStats

    @property
    def displayStats(self) -> dict:
        return {
            "author": self.video.author,
            "title": self.video.title,
            "duration": self.video.duration,
            "viewcount": self.video.viewcount,
            "allStreams": self.video.allstreams
        }

    def pprintStats(self) -> None:
        pprint(self.stats)

    def Downloadvideo(self):
        createdir("./videos°^°")
        self.video.getbestvideo().download()

    def DownloadAudio(self):
        createdir("./music°^°")
        self.video.getbestaudio().download()

    @property
    def getStreams(self) -> list:
        return self.video.allstreams

    def downloadbyIndex(self):
        for i, value in enumerate(self.getStreams):
            print(
                f"{i} \t ===> {value} ==> \t {value.get_filesize()}"
            )
        index = int(input('choose the stream you want ammongs the numbers above : \t'))
        self.getStreams[int(index)].download()


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# the gui section....
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


class YDL(Tk):
    searchButton: Button

    def __init__(self):
        super().__init__()
        self.stats = {
            "title": "Hazamat",
            "duration": "00:12",
            "author": "Mohamed"
        }
        self.title = "YTDL :)"
        self.configure(background="white")
        self.wm_resizable(False, False)
        self.wm_minsize(500, 100)
        self.frame = LabelFrame(self, text=None, background="#191900", bd=0, padx=200, pady=50)
        self.frame.pack(padx=10, pady=10)
        self.main()

    def searchQuery(self):
        self.titleLab = Label(
            self,
            text=self.stats['title'],
            background="white",
            fg="black",
            font="sans-serif",
            bd=0,
            padx=70,
            pady=30)
        self.titleLab.pack(pady=10)
        self.authorLab = Label(
            self,
            text=self.stats['author'],
            background="white",
            fg="black",
            font="sans-serif",
            bd=0,
            padx=70,
            pady=30)
        self.authorLab.pack(pady=10)
        self.durationLab = Label(
            self,
            text=self.stats['duration'],
            background="white",
            fg="black",
            font="sans-serif",
            bd=0,
            padx=70,
            pady=30)
        self.durationLab.pack(pady=10)
        self.download = Button(
            self, text="download", bd=0, background="black", font="sans-serif, 10",
            padx=10, pady=5, fg="white", command=self.downloadVid
        )
        self.download.pack(pady=10)

    def destroyEverything(self):
        self.ENTRY.destroy()
        self.durationLab.destroy()
        self.authorLab.destroy()
        self.titleLab.destroy()
        self.download.destroy()
        self.searchButton.destroy()

    def downloadVid(self):
        self.destroyEverything()
        self.frame.configure(padx=0, background="white")
        self.configure(background="white")
        dps = ['mp3' for i in range(0, 10)]
        j = 0
        k = 0
        for i in dps:
            self.i = Button(
                self.frame, text=i, padx=50, pady=10, bd=0,
                fg="White", font="sans-serif", background="black"
            )
            self.i.grid(pady=10, padx=10, row=k, column=j)
            j += 1
            if j > 3:
                k += 1
                j = 0

    def main(self):
        self.ENTRY = Entry(self.frame, border=0)
        self.ENTRY.grid(column=0, row=0, columnspan=3, ipadx=100, ipady=8, padx=10)
        self.searchButton = Button(self.frame, text="Search Now",
                                   bd=0, bg="black", fg="white", font="sans-serif",
                                   command=self.searchQuery)
        self.searchButton.grid(column=4, row=0)


root = YDL()
root.mainloop()
