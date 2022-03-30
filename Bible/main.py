import requests
import json
import tkinter as tk
from tkinter import Button, ttk,messagebox
####################   Global variables  #####################
global book
book=''
verse=''
url="http://getbible.net/json?passage="
end="&raw=true"
all_books=[]
books=[('Genesis', 'Exodus', 'Leviticus', 'Numbers', 'Deuteronomy', 'Joshua'), ('Judges', 'Ruth', '1 Samuel', '2 Samuel', '1 Kings', '2 Kings'), ('1 Chronicles', '2 Chronicles', 'Ezra', 'Nehemiah', 'Esther', 'Job'), ('Psalms', 'Proverbs', 'Ecclesiastes', 'Song of Songs', 'Isaiah', 'Jeremiah'), ('Lamentations', 'Ezekiel', 'Daniel', 'Hosea', 'Joel', 'Amos'), ('Obadiah', 'Jonah', 'Micah', 'Nahum', 'Habakkuk', 'Zephaniah'), ('Haggai', 'Zechariah', 'Malachi', 'Matthew', 'Mark', 'Luke'), ('John', 'Acts', 'Romans', '1 Corinthians', '2 Corinthians', 'Galatians'), ('Ephesians', 'Philippians', 'Colossians', '1 Thessalonians', '2 Thessalonians', '1 Timothy'), ('2 Timothy', 'Titus', 'Philemon', 'Hebrews', 'James', '1 Peter'), ('2 Peter', '1 John', '2 John', '3 John', 'Jude', 'Revelation')]
chapter="1"

#############   Function to get the entire chapter   #######################
def get_book(x):
    verse_int = 1
    while True:
        verse_str=str(verse_int)
        url_response = url + x + chapter + ":" + verse_str + end + "&version=asv"
        response = requests.get(url_response).json()
        verse_upper = response['book'][0]['chapter']
        verse_lower = verse_upper[verse_str]['verse']
        print(f'{verse_str}: {verse_lower}')
        verse_int = verse_int + 1
        
###################  Tkinter interace Setup   ################################        
root=tk.Tk()
root.title("Bible")
root.geometry("819x720") 

welcome = tk.Label(root, text="Bible App", font=('Ariel'))
welcome.pack()
mainFrame = tk.Frame(root, padx=2,pady=20)
mainFrame.configure(bg='black')
mainFrame.pack()
###############  Create Buttons with Chapter Names of the Bible  ###############
for i in range(11):
    for j in range(6):
        name = books[i][j] 
        btn=tk.Button(mainFrame, text=name, width=18, height=3, bg='light blue', command=lambda x=name: get_book(x))
        btn.grid(row=i,column=j)
        #btn.bind('<Button-1>', lambda : get_book(event))

root.mainloop()



