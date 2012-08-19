import urllib2 
from BeautifulSoup import BeautifulSoup
from Tkinter import *

class Crawler:
    def scrape(self):
        name_site = self.entry.get()
        limit = self.entry_url_number.get()    
        self.url = []
        self.url.append(name_site)
        self.entry_url_number.delete(0,'end')
        self.entry.delete(0,'end')
        for i in self.url:
            try:
                soup = BeautifulSoup(urllib2.urlopen(i).read())
                links = soup.findAll('a')
                for link in links:
                    new = link['href']
                    if 'http://' in new:
                        self.url.append(new)
            except:
                urllib2.HTTPError or urllib2.URLError or i.ValueError or UnboundLocalError or KeyError
            try:
                if len(set(self.url)) > int(limit):
                    break
            except ValueError:
                limit = 0
        print len(set(self.url)) 
        for i in set(self.url):
            self.listbox.insert(END,i)

    def __init__(self):
        self.root = Tk()
        self.root.title('Url Crawler')
        frame = Frame(width = 150, height = 150)
        frame.pack()
        enter_button = Button(self.root, text= 'Enter', command = self.scrape)
        self.entry = Entry(self.root)
        self.entry_url_number = Entry(self.root)
        self.entry_url_number.pack(side=TOP,fill=X)
        self.entry.pack(side=TOP,fill=X)   
        enter_button.pack(side=TOP,fill=X)
        y_scrollbar = Scrollbar(self.root)
        y_scrollbar.pack(side=RIGHT, fill=Y) 
        self.listbox = Listbox(self.root,height=30,width=100,yscrollcommand=y_scrollbar.set)
        label = Label(frame, text='URL Address')
        label.pack()
        number_label = Label(frame,text='Amount of URL\'s')
        number_label.pack()
        select_button = Button(self.root, text= 'Select', command=self.site)
        select_button.pack(side=TOP,fill=X)
        clearone_button = Button(self.root, text= 'Clear', command=lambda listbox=self.listbox: self.listbox.delete(ANCHOR))
        clearall_button = Button(self.root, text= 'Clear All', command=lambda listbox=self.listbox: self.listbox.delete(0,END))
        clearone_button.pack(side=TOP,fill=X)
        clearall_button.pack(side=TOP,fill=X)
        self.listbox.pack()
        y_scrollbar.config(command=self.listbox.yview)

    def site(self):
        for i in self.listbox.curselection():
            print self.url[int(i)]

    def main(self):
        self.root.mainloop() 


if __name__ == "__main__":
    Crawler().main()










