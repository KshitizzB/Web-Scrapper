from tkinter import *
root = Tk()
root.title('Web Scraper')
root.geometry('500x500')
root.resizable(False, False)
app = Frame(root)
app.grid()
l = Label(app, text='  WEB SCRAPER')
l.config(font=("Century Gothic", 44))
l2 = Label(app, text='\n  Welcome to free Web Scraper!')
l2.config(font=("Century Gothic", 22))
l3 = Label(app, text=' \nThis software scraps a webpage, \ncollects its data and store it in\n a .csv file only requiring its\n correct URL. Click the \nbelow button to proceed.\n')
l3.config(font=("Century Gothic", 18))
def start():
    l.destroy()
    l2.destroy()
    l3.destroy()
    b.destroy()
    l4 = Label(app, text='\n  You are one step away from\n scraping your desired webpage.\nEnter the correct URL in below,\nhit the button and you\n are done!\n')
    l4.config(font=("Century Gothic", 22))
    l4.grid()
    t = Entry()
    t.config(font=("Century Gothic", 25))
    t.grid()
    def submit():
        import requests
        import bs4
        import pandas as pd
        res = requests.get(t.get())
        soup = bs4.BeautifulSoup(res.content, 'lxml')
        size = []
        q1 = ['']
        for i in soup.select('title'):
            q1.append(i.text)
        q2 = ['']
        for i in soup.select('h3'):
            q2.append(i.text)
        q3 = ['']
        for i in soup.select('li'):
            q3.append(i.text)
        q4 = ['']
        for i in soup.select('a'):
            q4.append(i.text)
        q5 = ['']
        for i in soup.select('span'):
            q5.append(i.text)
        q6 = ['']
        for i in soup.select('table'):
            q6.append(i.text)
        q7 = ['']
        for i in soup.select('i'):
            q7.append(i.text)
        q8 = ['']
        for i in soup.select('style'):
            q8.append(i.text)
        q9 = ['']
        for i in soup.select('script'):
            q9.append(i.text)
        lq1 = len(q1)
        lq2 = len(q2)
        lq3 = len(q3)
        lq4 = len(q4)
        lq5 = len(q5)
        lq6 = len(q6)
        lq7 = len(q7)
        lq8 = len(q8)
        lq9 = len(q9)
        size.append(lq1)
        size.append(lq2)
        size.append(lq3)
        size.append(lq4)
        size.append(lq5)
        size.append(lq6)
        size.append(lq7)
        size.append(lq8)
        size.append(lq9)
        msize = size[0]
        for i in size:
            if i > msize:
                msize = i
        for i in range(lq1,msize):
            q1.append('')
        df1 = pd.DataFrame(q1, columns=['TITLE'])
        for i in range(lq2,msize):
            q2.append('')
        df2 = pd.DataFrame(q2, columns=['HEADINGS'])
        for i in range(lq3,msize):
            q3.append('') 
        df3 = pd.DataFrame(q3, columns=['LISTS'])
        for i in range(lq4,msize):
            q4.append('')
        df4 = pd.DataFrame(q4, columns=['LINKS'])
        for i in range(lq5,msize):
            q5.append('')
        df5 = pd.DataFrame(q5, columns=['SPANS'])
        for i in range(lq6,msize):
            q6.append('')
        df6 = pd.DataFrame(q6, columns=['TABLES'])
        for i in range(lq7,msize):
            q7.append('')
        df7 = pd.DataFrame(q7, columns=['KEYWORDS'])
        for i in range(lq8,msize):
            q8.append('')
        df8 = pd.DataFrame(q8, columns=['CSS'])
        for i in range(lq9,msize):
            q9.append('')
        df9 = pd.DataFrame(q9, columns=['SCRIPTS'])
        result = pd.concat([df1, df2, df3, df4, df5, df6, df7, df8, df9], axis=1, join_axes=[df1.index])
        result.to_csv('output.csv', index=False)
        l4.destroy()
        l5.destroy()
        t.destroy()
        b2.destroy()
        l6 = Label(app, text='\n   Thanks for using Web Scraper.\n  For more updates please follow')
        l6.config(font=("Century Gothic", 22))
        l6.grid()
        l7 = Label(app, text='  @kshitizz420')
        l7.config(font=("Century Gothic", 30))
        l7.grid()
        l8 = Label(app, text='\n  Your .csv is ready.\n Click below to open it.\n')
        l8.config(font=("Century Gothic", 20))
        l8.grid()
        def opencsv():
            from subprocess import Popen
            p = Popen('output.csv', shell=True)
            root.destroy()
        b3 = Button(app, text="Open CSV File!", command=opencsv)
        b3.config(font=("Century Gothic", 25))
        b3.grid()
    b2 = Button(app, text="Scrap it!", command=submit)
    b2.config(font=("Century Gothic", 25))
    b2.grid()
    l5 = Label(app, text='\n  Enter the correct URL of wesbpage:\n')
    l5.config(font=("Century Gothic", 15))
    l5.grid()     
l.grid()
l2.grid()
l3.grid()
b = Button(app, text='Scrap a webpage!', command=start)
b.config(font=("Century Gothic", 25))
b.grid()
root.mainloop()
