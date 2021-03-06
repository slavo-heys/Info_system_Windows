# -*- coding: utf-8 -*-
"""
Created on Fri Sep  3 10:26:24 2021

@author: ilodz

Program dostarcza nam informacji na temat naszego komputera, dane wywietlane są
w niewielkim oknie na pulpicie naszego komputera. Przy jego pomocy możesz sprawdzić
IP wewnętrzne i zewnętrzne maszyny której używasz. Możesz również sprawdzić
geolokalizację IP podanego w osobnym oknie, niestety jest to tylko przybliżona 
lokalizacja. W takim przypadku należy brać pod uwagę tylko miasto i sieć.
Możesz też sprawdzić Ip interesującej cię strony internetowej.

Program jest w pełni darmowy z przeznaczeniem dla systemów Windows.

"""

import tkinter as tk
import platform
import socket
import re
import uuid
import json
import psutil
import logging
import socket
import re
import uuid
import requests
import urllib.request
import json
import webbrowser

from win32api import GetSystemMetrics


class Program:
    def __init__(self):
        self.window = tk.Tk()

# %% deklaracja zmiennych
        self.linia = ("-"*34)+" System Information "+("-"*34)
        self.linia0 = ("-"*42)+" Memory "+("-"*42)
        self.linia1 = ("-"*40)+" Info Disks "+("-"*40)
        self.linia2 = ("-"*42)+" Network "+("-"*42)

        self.system = tk.StringVar()
        self.machineName = tk.StringVar()
        self.versionSystem = tk.StringVar()
        self.machine = tk.StringVar()
        self.processor = tk.StringVar()
        self.zuzycieProcesora = tk.StringVar()
        self.calaMemory = tk.StringVar()
        self.percent = tk.StringVar()
        self.zajetaMemory = tk.StringVar()
        self.freeMemory = tk.StringVar()
        self.dyskDevice = tk.StringVar()
        self.dyskTotal = tk.StringVar()
        self.dyskUsed = tk.StringVar()
        self.dyskFree = tk.StringVar()
        self.dyskPercent = tk.StringVar()
        self.dyskDeviceType = tk.StringVar()
        self.dyskPercent = tk.StringVar()
        self.mac = tk.StringVar()
        self.ip_address = tk.StringVar()
        self.IP_adress = tk.StringVar()
        self.netSent = tk.StringVar()
        self.netRecv = tk.StringVar()

        self.inputIp = tk.StringVar()
        self.ip = tk.StringVar()
        self.country = tk.StringVar()
        self.city = tk.StringVar()
        self.postal = tk.StringVar()
        self.latitude = tk.StringVar()
        self.longitude = tk.StringVar()
        self.regionName = tk.StringVar()
        self.isp = tk.StringVar()
        self.link = tk.StringVar()

        self.inputIpWWW = tk.StringVar()


# %% wywołanie okna
        self.width = GetSystemMetrics(0)
        self.height = GetSystemMetrics(1)
        self.pozX = self.width - 400
        self.pozY = self.height - 5
        self.window.geometry("310x400+"+str(self.pozX)+"+5")
        self.window.configure(background="black")
        self.window.overrideredirect(1)

        self.rama = tk.LabelFrame(self.window, padx=5, pady=5)
        self.rama.configure(background="black")
        self.rama.pack(fill="both", expand="yes")

        self.exitButton = tk.Button(self.rama, text=" Exit ", font=(
            "Arial", 7, "italic"), bg="gray", fg="gold", command=self.exit)
        self.exitButton.place(x=0, y=0)

        self.sprawdzIPButton = tk.Button(self.rama, text=" sprawdz IP ", font=(
            "Arial", 7, "italic"), bg="gray", fg="gold", command=self.sprawdz_IP)
        self.sprawdzIPButton.place(x=32, y=0)

        self.sprawdzWww = tk.Button(self.rama, text=" sprawdz IP strony ", font=(
            "Arial", 7, "italic"), bg="gray", fg="gold", command=self.sprawdz_WWW)
        self.sprawdzWww.place(x=94, y=0)

        self.liniaOkno = tk.Label(self.rama, text=self.linia, font=(
            "Arial", 7, "italic"), bg="black", fg="gold")
        self.liniaOkno.place(x=0, y=25)

        self.liniaSystem = tk.Label(self.rama, textvariable=self.system, font=(
            "Arial", 7), bg="black", fg="gold")
        self.liniaSystem.place(x=2, y=50)

        self.liniaVersionSystem = tk.Label(
            self.rama, textvariable=self.versionSystem, font=("Arial", 7), bg="black", fg="gold")
        self.liniaVersionSystem.place(x=100, y=50)

        self.liniaMachineName = tk.Label(
            self.rama, textvariable=self.machineName, font=("Arial", 7), bg="black", fg="gold")
        self.liniaMachineName.place(x=2, y=70)

        self.liniaMachine = tk.Label(
            self.rama, textvariable=self.machine, font=("Arial", 7), bg="black", fg="gold")
        self.liniaMachine.place(x=180, y=70)

        self.liniaProcesor = tk.Label(self.rama, textvariable=self.processor, font=(
            "Arial", 7), bg="black", fg="gold")
        self.liniaProcesor.place(x=2, y=90)

        self.liniaProcentProcesora0 = tk.Label(
            self.rama, text="CPU usage:", font=("Arial", 7), bg="black", fg="gold")
        self.liniaProcentProcesora0.place(x=2, y=110)

        self.liniaProcentProcesora1 = tk.Label(
            self.rama, textvariable=self.zuzycieProcesora, font=("Arial", 7), bg="black", fg="gold")
        self.liniaProcentProcesora1.place(x=60, y=110)

        self.liniaProcentProcesora2 = tk.Label(
            self.rama, text="%", font=("Arial", 7), bg="black", fg="gold")
        self.liniaProcentProcesora2.place(x=90, y=110)

        self.liniaOkno0 = tk.Label(self.rama, text=self.linia0, font=(
            "Arial", 7, "italic"), bg="black", fg="gold")
        self.liniaOkno0.place(x=0, y=135)

        self.liniaMemory = tk.Label(self.rama, text="Total memory:", font=(
            "Arial", 7, "italic"), bg="black", fg="gold")
        self.liniaMemory.place(x=2, y=160)

        self.liniaMemory0 = tk.Label(self.rama, textvariable=self.calaMemory, font=(
            "Arial", 7, "italic"), bg="black", fg="gold")
        self.liniaMemory0.place(x=70, y=160)

        self.liniaMemory0 = tk.Label(self.rama, text="GB", font=(
            "Arial", 7, "italic"), bg="black", fg="gold")
        self.liniaMemory0.place(x=95, y=160)

        self.liniaMemory1 = tk.Label(self.rama, text="Memory consumption:", font=(
            "Arial", 7, "italic"), bg="black", fg="gold")
        self.liniaMemory1.place(x=130, y=160)

        self.liniaMemory2 = tk.Label(self.rama, textvariable=self.percent, font=(
            "Arial", 7, "italic"), bg="black", fg="gold")
        self.liniaMemory2.place(x=230, y=160)

        self.liniaMemory2 = tk.Label(self.rama, text="%", font=(
            "Arial", 7, "italic"), bg="black", fg="gold")
        self.liniaMemory2.place(x=245, y=160)

        self.liniaZajety = tk.Label(self.rama, text="Memory used:", font=(
            "Arial", 7, "italic"), bg="black", fg="gold")
        self.liniaZajety.place(x=2, y=180)

        self.liniaZajety0 = tk.Label(self.rama, textvariable=self.zajetaMemory, font=(
            "Arial", 7, "italic"), bg="black", fg="gold")
        self.liniaZajety0.place(x=70, y=180)

        self.liniaZajety1 = tk.Label(self.rama, text="GB", font=(
            "Arial", 7, "italic"), bg="black", fg="gold")
        self.liniaZajety1.place(x=95, y=180)

        self.liniaZajety = tk.Label(self.rama, text="Memory free:", font=(
            "Arial", 7, "italic"), bg="black", fg="gold")
        self.liniaZajety.place(x=130, y=180)

        self.liniaZajety0 = tk.Label(self.rama, textvariable=self.freeMemory, font=(
            "Arial", 7, "italic"), bg="black", fg="gold")
        self.liniaZajety0.place(x=190, y=180)

        self.liniaZajety1 = tk.Label(self.rama, text="GB", font=(
            "Arial", 7, "italic"), bg="black", fg="gold")
        self.liniaZajety1.place(x=215, y=180)

        self.liniaOkno1 = tk.Label(self.rama, text=self.linia1, font=(
            "Arial", 7, "italic"), bg="black", fg="gold")
        self.liniaOkno1.place(x=0, y=205)

        self.liniaDevice0 = tk.Label(self.rama, text="Disk:", font=(
            "Arial", 7, "italic"), bg="black", fg="gold")
        self.liniaDevice0.place(x=2, y=230)

        self.liniaDevice1 = tk.Label(self.rama, textvariable=self.dyskDevice, font=(
            "Arial", 7, "italic"), bg="black", fg="gold")
        self.liniaDevice1.place(x=30, y=230)

        self.liniaDevice2 = tk.Label(self.rama, text="FsType:", font=(
            "Arial", 7, "italic"), bg="black", fg="gold")
        self.liniaDevice2.place(x=70, y=230)

        self.liniaDevice1 = tk.Label(self.rama, textvariable=self.dyskDeviceType, font=(
            "Arial", 7, "italic"), bg="black", fg="gold")
        self.liniaDevice1.place(x=110, y=230)

        self.liniaDevice2 = tk.Label(self.rama, text="Total:", font=(
            "Arial", 7, "italic"), bg="black", fg="gold")
        self.liniaDevice2.place(x=150, y=230)

        self.liniaDevice3 = tk.Label(self.rama, textvariable=self.dyskTotal, font=(
            "Arial", 7, "italic"), bg="black", fg="gold")
        self.liniaDevice3.place(x=190, y=230)

        self.liniaDevice4 = tk.Label(self.rama, text="GB", font=(
            "Arial", 7, "italic"), bg="black", fg="gold")
        self.liniaDevice4.place(x=230, y=230)

        self.liniaDevice5 = tk.Label(self.rama, text="Disk Used:", font=(
            "Arial", 7, "italic"), bg="black", fg="gold")
        self.liniaDevice5.place(x=2, y=250)

        self.liniaDevice6 = tk.Label(self.rama, textvariable=self.dyskUsed, font=(
            "Arial", 7, "italic"), bg="black", fg="gold")
        self.liniaDevice6.place(x=60, y=250)

        self.liniaDevice7 = tk.Label(self.rama, text="GB", font=(
            "Arial", 7, "italic"), bg="black", fg="gold")
        self.liniaDevice7.place(x=100, y=250)

        self.liniaDevice8 = tk.Label(self.rama, text="Disk Free:", font=(
            "Arial", 7, "italic"), bg="black", fg="gold")
        self.liniaDevice8.place(x=135, y=250)

        self.liniaDevice9 = tk.Label(self.rama, textvariable=self.dyskFree, font=(
            "Arial", 7, "italic"), bg="black", fg="gold")
        self.liniaDevice9.place(x=180, y=250)

        self.liniaDevice10 = tk.Label(self.rama, text="GB", font=(
            "Arial", 7, "italic"), bg="black", fg="gold")
        self.liniaDevice10.place(x=215, y=250)

        self.liniaDevice11 = tk.Label(self.rama, textvariable=self.dyskPercent, font=(
            "Arial", 7, "italic"), bg="black", fg="gold")
        self.liniaDevice11.place(x=240, y=250)

        self.liniaDevice10 = tk.Label(self.rama, text="%", font=(
            "Arial", 7, "italic"), bg="black", fg="gold")
        self.liniaDevice10.place(x=268, y=250)

        self.liniaOkno2 = tk.Label(self.rama, text=self.linia2, font=(
            "Arial", 7, "italic"), bg="black", fg="gold")
        self.liniaOkno2.place(x=0, y=270)

        self.liniaNetwork0 = tk.Label(self.rama, text="ip:", font=(
            "Arial", 7, "italic"), bg="black", fg="gold")
        self.liniaNetwork0.place(x=2, y=300)

        self.liniaNetwork1 = tk.Label(self.rama, textvariable=self.ip_address, font=(
            "Arial", 7, "italic"), bg="black", fg="gold")
        self.liniaNetwork1.place(x=15, y=300)

        self.liniaNetwork0 = tk.Label(self.rama, text="mac:", font=(
            "Arial", 7, "italic"), bg="black", fg="gold")
        self.liniaNetwork0.place(x=160, y=300)

        self.liniaNetwork1 = tk.Label(self.rama, textvariable=self.mac, font=(
            "Arial", 7, "italic"), bg="black", fg="gold")
        self.liniaNetwork1.place(x=180, y=300)

        self.liniaNetwork0 = tk.Label(self.rama, text="IP:", font=(
            "Arial", 7, "italic"), bg="black", fg="gold")
        self.liniaNetwork0.place(x=2, y=320)

        self.liniaNetwork1 = tk.Label(self.rama, textvariable=self.IP_adress, font=(
            "Arial", 7, "italic"), bg="black", fg="gold")
        self.liniaNetwork1.place(x=15, y=320)

        self.liniaNetwork2 = tk.Label(self.rama, text="Sent:", font=(
            "Arial", 7, "italic"), bg="black", fg="gold")
        self.liniaNetwork2.place(x=2, y=340)

        self.liniaNetwork3 = tk.Label(self.rama, textvariable=self.netSent, font=(
            "Arial", 7, "italic"), bg="black", fg="gold")
        self.liniaNetwork3.place(x=30, y=340)

        # self.liniaNetwork2 = tk.Label(self.rama, text = "bytes", font=("Arial", 7, "italic"), bg = "black", fg = "gold")
        # self.liniaNetwork2.place(x=90, y=340)

        self.liniaNetwork2 = tk.Label(self.rama, text="Recv:", font=(
            "Arial", 7, "italic"), bg="black", fg="gold")
        self.liniaNetwork2.place(x=160, y=340)

        self.liniaNetwork3 = tk.Label(self.rama, textvariable=self.netRecv, font=(
            "Arial", 7, "italic"), bg="black", fg="gold")
        self.liniaNetwork3.place(x=190, y=340)

        # self.liniaNetwork2 = tk.Label(self.rama, text = "bytes", font=("Arial", 7, "italic"), bg = "black", fg = "gold")
        # self.liniaNetwork2.place(x=250, y=340)


# %% wywołanie definicji
        self.twoj_komputer()
        self.cpu()
        self.memory()
        self.dyski()
        self.network()
        self.net_counters()

# %%
        self.window.mainloop()

# %% definicje programu

    def exit(self):
        self.window.destroy()

    def sprawdz_WWW(self):
        self.topik = tk.Toplevel()
        self.topik.geometry("600x150")
        self.topik.configure(background="black")
        self.topik.title("Sprawdź IP strony WWW")

        self.liniaIpWww = tk.Label(
            self.topik, text="WWW:", font=("Arial"), bg="black", fg="gold")
        self.liniaIpWww.place(x=140, y=11)

        self.liniaIpWww1 = tk.Entry(self.topik, textvariable=self.inputIpWWW)
        self.liniaIpWww1.place(x=205, y=11)

        self.buttonIPWww = tk.Button(
            self.topik, text=" pokaż IP ", command=self.pokaz_IP_WWW)
        self.buttonIPWww.place(x=350, y=8)

        self.topik.mainloop()

    def pokaz_IP_WWW(self):
        self.ipStrony = self.inputIpWWW.get()
        self.IP_addres = socket.gethostbyname(
            self.ipStrony)  # sprawdzanie adresu ip witryny

        self.liniaIP = tk.Label(self.topik, text=self.IP_addres, font=(
            "Arial", 16), bg="black", fg="gold")
        self.liniaIP.place(x=190, y=100)

    def sprawdz_IP(self):
        self.top = tk.Toplevel()
        self.top.geometry("600x400")
        self.top.configure(background="black")
        self.top.title("Geolokalizacja IP")

        self.liniaIp = tk.Label(self.top, text="IP:", font=(
            "Arial"), bg="black", fg="gold")
        self.liniaIp.place(x=170, y=11)

        self.liniaIp1 = tk.Entry(self.top, textvariable=self.inputIp)
        self.liniaIp1.place(x=205, y=11)

        self.buttonIP = tk.Button(
            self.top, text=" Sprawdź ", command=self.wynik_IP)
        self.buttonIP.place(x=350, y=8)

        self.top.mainloop()

    def wynik_IP(self):
        self.ip = self.inputIp.get()
        self.zap = requests.get("http://ip-api.com/json/"+self.ip).json()
        self.country.set(self.zap["country"])
        self.city.set(self.zap["city"])
        self.postal.set(self.zap["zip"])
        self.latitude.set(self.zap["lat"])
        self.longitude.set(self.zap["lon"])
        self.regionName.set(self.zap["regionName"])
        self.isp.set(self.zap["isp"])

        self.dlugosc = self.zap["lat"]
        self.szerokosc = self.zap["lon"]

        self.liniaGeo = ("_"*52)+" geolokalizacja "+("_"*52)
        self.liniaGeo0 = ("_"*53)+" współrzędne "+("_"*53)

        self.liniaCountry = tk.Label(self.top, text=self.liniaGeo, font=(
            "Arial", 7), bg="black", fg="DarkOrange")
        self.liniaCountry.place(x=2, y=40)

        self.liniaCountry0 = tk.Label(self.top, text="Kraj:", font=(
            "Arial", 10, "bold"), bg="black", fg="DarkOrange")
        self.liniaCountry0.place(x=10, y=80)

        self.liniaCountry1 = tk.Label(self.top, textvariable=self.country, font=(
            "Arial", 10, "italic"), bg="black", fg="gold")
        self.liniaCountry1.place(x=150, y=80)

        self.liniaCountry2 = tk.Label(self.top, text="Miasto:", font=(
            "Arial", 10, "bold"), bg="black", fg="DarkOrange")
        self.liniaCountry2.place(x=300, y=80)

        self.liniaCountry3 = tk.Label(self.top, textvariable=self.city, font=(
            "Arial", 10, "italic"), bg="black", fg="gold")
        self.liniaCountry3.place(x=400, y=80)

        self.liniaCountry4 = tk.Label(self.top, text="Nazwa regionu:", font=(
            "Arial", 10, "bold"), bg="black", fg="DarkOrange")
        self.liniaCountry4.place(x=10, y=120)

        self.liniaCountry5 = tk.Label(self.top, textvariable=self.regionName, font=(
            "Arial", 10, "italic"), bg="black", fg="gold")
        self.liniaCountry5.place(x=150, y=120)

        self.liniaCountry6 = tk.Label(self.top, text="Kod:", font=(
            "Arial", 10, "bold"), bg="black", fg="DarkOrange")
        self.liniaCountry6.place(x=300, y=120)

        self.liniaCountry7 = tk.Label(self.top, textvariable=self.postal, font=(
            "Arial", 10, "italic"), bg="black", fg="gold")
        self.liniaCountry7.place(x=400, y=120)

        self.liniaDostawca = tk.Label(self.top, text="Dostawca internetu:", font=(
            "Arial", 10, "italic"), bg="black", fg="DarkOrange")
        self.liniaDostawca.place(x=10, y=160)

        self.liniaDostawca1 = tk.Label(self.top, textvariable=self.isp, font=(
            "Arial", 10, "italic"), bg="black", fg="gold")
        self.liniaDostawca1.place(x=200, y=160)

        self.liniaCountry8 = tk.Label(self.top, text=self.liniaGeo0, font=(
            "Arial", 7), bg="black", fg="DarkOrange")
        self.liniaCountry8.place(x=2, y=200)

        self.liniaCountry9 = tk.Label(self.top, text="latitude:", font=(
            "Arial", 10, "bold"), bg="black", fg="DarkOrange")
        self.liniaCountry9.place(x=10, y=240)

        self.liniaCountry10 = tk.Label(self.top, textvariable=self.latitude, font=(
            "Arial", 10, "italic"), bg="black", fg="gold")
        self.liniaCountry10.place(x=150, y=240)

        self.liniaCountry11 = tk.Label(self.top, text="longitude:", font=(
            "Arial", 10, "bold"), bg="black", fg="DarkOrange")
        self.liniaCountry11.place(x=300, y=240)

        self.liniaCountry12 = tk.Label(self.top, textvariable=self.longitude, font=(
            "Arial", 10, "italic"), bg="black", fg="gold")
        self.liniaCountry12.place(x=400, y=240)

        self.link.set("https://www.google.com/maps/search/?api=1&query=" +
                      str(self.dlugosc)+"+"+str(self.szerokosc))

        self.buttonWWW = tk.Button(self.top, text="Otwórz stronę", font=(
            "Arial", 10), command=self.open_www)
        self.buttonWWW.place(x=270, y=300)

    def open_www(self):
        webbrowser.open(self.link.get())

    def twoj_komputer(self):
        uname = platform.uname()
        self.system.set(f"System: {uname.system}")
        self.machineName.set(f"Machine Name: {uname.node}")
        self.versionSystem.set(f"Version: {uname.version}")
        self.machine.set(f"Machine: {uname.machine}")
        self.processor.set(f"Processor: {uname.processor}")

    def cpu(self):
        self.zP = psutil.cpu_percent()
        self.zuzycieProcesora.set(self.zP)

        self.window.after(1000, self.cpu)

    def memory(self):
        self.mem = psutil.virtual_memory()
        self.cala = ((self.mem[0])/(1000*1024*1024))
        self.cala = (round(self.cala, 2))
        self.calaMemory.set(self.cala)

        self.percent.set(self.mem.percent)

        self.free = ((self.mem[4])/(1000*1024*1024))
        self.free = (round(self.free, 2))
        self.freeMemory.set(self.free)

        self.zajeta = ((self.mem[3])/(1000*1024*1024))
        self.zajeta = (round(self.zajeta, 2))
        self.zajetaMemory.set(self.zajeta)

        self.window.after(1000, self.memory)

    def dyski(self):
        self.dysk = psutil.disk_partitions()
        self.dysk_1 = psutil.disk_usage('/')

        self.dyskDevice.set(self.dysk[0].device)
        self.dyskDeviceType.set(self.dysk[0].fstype)

        self.dyskTo = (self.dysk_1.total)/(1000*1024*1024)
        self.dyskTo = (round(self.dyskTo, 2))
        self.dyskTotal.set(self.dyskTo)

        self.dyskUs = (self.dysk_1.used) / (1000*1024*1024)
        self.dyskUs = (round(self.dyskUs, 2))
        self.dyskUsed.set(self.dyskUs)

        self.dyskFr = (self.dysk_1.free) / (1000*1024*1024)
        self.dyskFr = (round(self.dyskFr, 2))
        self.dyskFree.set(self.dyskFr)

        self.dyskPercent.set(self.dysk_1.percent)

        self.window.after(10000, self.dyski)

    def network(self):
        self.mac.set(':'.join(re.findall('..', '%012x' % uuid.getnode())))
        self.hostname = socket.gethostname()
        self.ip_address.set(socket.gethostbyname(self.hostname))

        self.ip = requests.get('https://api.ipify.org').text
        self.IP_adress.set(self.ip)

        self.window.after(10000, self.network)

    def net_counters(self):
        self.netCount = psutil.net_io_counters()
        self.netSent.set(self.netCount.bytes_sent)
        self.netRecv.set(self.netCount.bytes_recv)

        self.window.after(1000, self.net_counters)


prog = Program()
