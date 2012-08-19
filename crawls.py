from urllib2 import urlopen
from BeautifulSoup import BeautifulSoup
from Tkinter import *

class Crawler:
    def scrape(self):
        name_site = self.entry.get()    
        self.url = []
        self.url.append(name_site)
        self.entry.delete(0,'end')
        count = 0
        for i in self.url:
            try:
                soup = BeautifulSoup(urlopen(i).read())
            except:
                urllib2.HTTPError or urllib2.URLError or i.ValueError
            links = soup.findAll('a')
            for link in links:
                try:
                    new = link['href']
                    if 'http://' in new:
                        self.url.append(new)
                except KeyError:
                    pass
            count += 1
            if count > 2:
                break
        for i in set(self.url):
            self.listbox.insert(END,i)

    def __init__(self):
        self.root = Tk()
        self.root.title('Url Crawler')
        frame = Frame(width = 150, height = 150)
        frame.pack()
        enter_button = Button(self.root, text= 'Enter', command = self.scrape)
        self.entry = Entry(frame)
        self.entry.pack()   
        enter_button.pack()
        y_scrollbar = Scrollbar(self.root)
        y_scrollbar.pack(side=RIGHT, fill=Y) 
        self.listbox = Listbox(self.root,height=30,width=100,yscrollcommand=y_scrollbar.set)
        label = Label(frame, text='URL Address')
        label.pack()
        select_button = Button(self.root, text= 'Select', command=self.site)
        select_button.pack()
        clearone_button = Button(self.root, text= 'Clear', command=lambda listbox=self.listbox: self.listbox.delete(ANCHOR))
        clearall_button = Button(self.root, text= 'Clear All', command=lambda listbox=self.listbox: self.listbox.delete(0,END))
        clearone_button.pack(side='right')
        clearall_button.pack(side='right')
        self.listbox.pack()
        y_scrollbar.config(command=self.listbox.yview)

    def site(self):
        for i in self.listbox.curselection():
            print self.url[int(i)]

    def main(self):
        self.root.mainloop() 


if __name__ == "__main__":
    Crawler().main()










