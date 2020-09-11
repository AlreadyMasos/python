import tkinter as tk
from tkinter import ttk
import webbrowser 
import win32api

app = tk.Tk()
app.title('benis')

a = (77, 88, 99)
b = (19, 19, 70)

pc_name = ttk.Label(app, text = "Имя компьютера: " + str(win32api.GetComputerName()))
pc_name.grid(row = 0,column = 0)

user_name = ttk.Label(app, text = "Имя пользователя: " + str(win32api.GetUserName()))
user_name.grid(row = 1, column = 0)

paths = ttk.Label(app, text = "Системные пути:")
paths.grid(row = 2, column = 0)

fPath = ttk.Label(app, text = str(win32api.GetWindowsDirectory()))
fPath.grid(row = 3, column = 0)

sPath = ttk.Label(app, text = str(win32api.GetSystemDirectory()))
sPath.grid(row = 4, column = 0)

tPath = ttk.Label(app, text = str(win32api.GetTempPath()))
tPath.grid(row = 5, column = 0)

version = ttk.Label(app, text = str(win32api.GetVersionEx()))
version.grid(row = 5, column = 0)

fMetr = ttk.Label(app, text = "Ширина экрана: " + str(win32api.GetSystemMetrics(0)))
fMetr.grid(row = 6, column = 0)

sMetr = ttk.Label(app, text = "Количество клавиш мыши: " + str(win32api.GetSystemMetrics(43)))
sMetr.grid(row = 7, column = 0)

fColor = ttk.Label(app, text = "Цвета: " + str(win32api.GetSysColor(3)))
fColor.grid(row = 8, column = 0)

sColor = ttk.Label(app, text = str(win32api.SetSysColors(a,b)))
sColor.grid(row = 9, column = 0)

time = ttk.Label(app, text = "Время: " + str(win32api.GetSystemTime()))
time.grid(row = 10, column = 0)

fApi = ttk.Label(app, text = str(win32api.GetCommandLine()))
fApi.grid(row = 11, column = 0)

sApi = ttk.Label(app, text = str(win32api.GetCurrentThread()))
sApi.grid(row = 12, column = 0)

thApi = ttk.Label(app, text = str(win32api.GetDiskFreeSpace('D:')))
thApi.grid(row = 13, column = 0)

foApi = ttk.Label(app, text = str(win32api.GetCursorPos()))
foApi.grid(row = 14, column = 0)



app.mainloop()