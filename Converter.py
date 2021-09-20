from tkinter import *
from lxml import etree
import requests
from bs4 import BeautifulSoup

window = Tk()
window.title("Converter")
window.wm_iconbitmap("logo.ico")
window.configure(background="black")
window.resizable(0, 0)

URL = "https://nbg.gov.ge/monetary-policy/currency"

HEADERS = ({'User-Agent':
                'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 \
                (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36', \
            'Accept-Language': 'en-US, en;q=0.5'})

webpage = requests.get(URL, headers=HEADERS)
soup = BeautifulSoup(webpage.content, "html.parser")
dom = etree.HTML(str(soup))

eu_row = dom.xpath('//*[@id="nbg"]/div[1]/div[4]/div/div[2]/div[2]/div[3]/div[14]/div/div/div[3]/span')[0].text
eur_value = float(eu_row)

usd_row = dom.xpath('//*[@id="nbg"]/div[1]/div[4]/div/div[2]/div[2]/div[3]/div[41]/div/div/div[3]/span')[0].text
usd_value = float(usd_row)


def converter(event):
    answer = entry1.get()
    try:
        if float(answer) > 0:
            us = float(entry1.get()) / usd_value
            eu = float(entry1.get()) / eur_value
            label_usd['text'] = str(round(us,4)) + " $"
            label_eur['text'] = str(round(eu,4)) + " €"
        elif float(answer) == 0:
            label_usd['text'] = "0"
            label_eur['text'] = "0"

        else:
            label_usd['text'] = "input Positive value "
            label_eur['text'] = "input Positive value "
    except ValueError:
        label_usd['text'] = "input number! "
        label_eur['text'] = "input number! "


photo1 = PhotoImage(file="me.gif")
Label(window, image=photo1, bg="black").grid(row=0, column=0)

Label(window, text="Input the GEL value into this box ↓↓↓: ", font=("Impact", 18), bg="black", fg="Green").grid(row=1,
                                                                                                                column=0,
                                                                                                                sticky=W,
                                                                                                                padx=30)
Label(window, text=" ₾  : ", font=("Impact", 20), bg="black", fg="Green").grid(row=2, column=0, sticky=W)

entry1 = Entry(window, font=(None, 20, "bold"), width=20, bg="white", fg="green", justify=CENTER)
entry1.grid(row=2, column=0, sticky=W, padx=55, pady=5)

Label(window, text=" Value in USD ↓↓↓: ", font=("Impact", 18), bg="black", fg="Green").grid(row=3, column=0, sticky=W,
                                                                                            padx=120)
Label(window, text=" $   : ", font=("Impact", 20), bg="black", fg="Green").grid(row=4, column=0, sticky=W)

label_usd = Label(window, text="", font=(None, 20, "bold"), width=18, bg="white", fg="red")
label_usd.grid(row=4, column=0, sticky=W, padx=55, pady=5)

Label(window, text=" Value in EUR ↓↓↓: ", font=("Impact", 18), bg="black", fg="Green").grid(row=5, column=0, sticky=W,
                                                                                            padx=120)
Label(window, text=" €   : ", font=("Impact", 20), bg="black", fg="Green").grid(row=6, column=0, sticky=W)

label_eur = Label(window, text="", font=(None, 20, "bold"), width=18, bg="white", fg="red")
label_eur.grid(row=6, column=0, sticky=W, padx=55, pady=5)

button_convert = Button(window, text="convert", font=("Tape Loop", 22, "bold"), bg="black", fg="green", width=10)
button_convert.grid(row=4, column=0, sticky=W, padx=400)
button_convert.bind("<Button-1>", converter)
window.bind("<Return>", converter)


def close_window(event):
    window.destroy()


button_exit = Button(window, text="Exit", font=("Tape Loop", 22, "bold"), bg="black", fg="green", width=10)
button_exit.grid(row=8, column=0, sticky=W, padx=20, pady=40)
button_exit.bind("<Button-1>", close_window)

window.mainloop()
