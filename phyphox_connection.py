import pyphox
import phyphox_sismic_exploration as phy
import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
from ttkthemes import ThemedTk
import webbrowser


def Phyphox_connectionApp():

    
     def Start():
    
         print(before_hosts)
    
         try:
    
             for host in before_hosts:
    
                 conn = pyphox.connect(host)
    
                 conn.start()
    
             label.config(text='Inicializando..')
    
             label.after(100, lambda: label.config(text='Medición en curso'))
    
     
    
         except Exception:
    
             messagebox.showerror(
    
                 'Error', 'Primero ingresa la ip de los dispositivos o haz una prueba para comenzar')
    
     
    
     
    
     def Stop():
    
         try:
    
             for host in before_hosts:
    
                 conn = pyphox.connect(host)
    
                 conn.stop()
    
             label.config(text='Deteniendo..')
    
             label.after(100, lambda: label.config(text='Detenido'))
    
     
    
         except Exception:
    
             messagebox.showerror(
    
                 'Error', 'Primero ingresa la ip de los dispositivos o haz una prueba para comenzar')
    
     
    
     
    
     def OpenFilter():
    
         Phyphox_connection.destroy()
    
         phy.main()
    
     
    
     
    
     def clear():
    
         try:
    
             for host in before_hosts:
    
                 conn = pyphox.connect(host)
    
                 conn.clear()
    
             label.config(text='Limpiando..')
    
             label.after(100, lambda: label.config(text='Todo despejado'))
    
             label.after(1500, lambda: label.config(text='Esperando..'))
    
         except Exception:
    
             messagebox.showerror(
    
                 'Error', 'Primero ingresa la ip de los dispositivos o haz una prueba para comenzar')
    
     
    
     
    
     def show_inputs():
    
     
    
         try:
    
             for host in before_hosts:
    
                 conn = pyphox.connect(host)
    
                 conn.execute('/config')
    
             frame2 = tk.Frame(Phyphox_connection)
    
             frame2.pack(side='bottom', pady=10)
    
             frame2.place(relx=0.5, rely=0.6, anchor='center')
    
             label.config(
    
                 text='Haz abierto la configuración de exportación, recuerda mantener la medidición detenida antes de exportar')
    
             select = ttk.Combobox(frame2, values=['csv', 'excel'], state='readonly', width=20,
    
                                   height=3,  style='TCombobox', font=('Cascadia Code', 12), justify='center')
    
             select.grid(row=0, column=0, padx=10, pady=10)
    
             style = ttk.Style()
    
             style.theme_use('default')
    
             style.configure('TCombobox', fieldbackground='white', background='white',
    
                             foreground='black', bordercolor='black', arrowcolor='black')
    
             style.map('TCombobox', fieldbackground=[('readonly', 'white')])
    
             style.map('TCombobox', background=[('readonly', 'white')])
    
             style.map('TCombobox', foreground=[('readonly', 'black')])
    
             style.map('TCombobox', bordercolor=[('readonly', 'black')])
    
             style.map('TCombobox', arrowcolor=[('readonly', 'black')])
    
     
    
             def Export():
    
     
    
                 if select.get() == 'csv':
    
                     if messagebox.askquestion('Exportar', 'Aun se esta trabajando en esta funcion, al presionar aceptar enviaras una petición al desarrollador para desarrollar dicha función ') == 'yes':
    
     
    
                         webbrowser.open(
    
                             'mailto:ferneyandres10@hotmail.com?subject=Exportar a csv&body=Hola, me gustaria que implementaras la funcion de exportar a csv')
    
     
    
                 else:
    
                     try:
    
                         for host in before_hosts:
    
                             conn = pyphox.connect(host)
    
                             conn.execute('/config')
    
                         label.config(text='Exportando..')
    
                         for host in before_hosts:
    
                             conn = pyphox.connect(host)
    
                             conn.export(select.get())
    
     
    
                         label.after(100, lambda: label.config(
    
                             text='Los archivos se han exportado en el directorio seleccionado'))
    
     
    
                     except Exception:
    
                         messagebox.showerror(
    
                             'Error', 'Hubo un error al exportar los archivos, verifica que todo este bien')
    
                         print(before_hosts)
    
     
    
             def DeleteExportInterface():
    
                 frame2.destroy()
    
     
    
             export_button = tk.Button(frame2, text='Submit', command=Export)
    
             export_button.grid(row=0, column=2, padx=10, pady=10)
    
             export_button.config(bg='blue', fg='white', font=(
    
                 'Cascadia Code', 12, 'bold'), width=10)
    
             close_button = tk.Button(frame2, text='Close',
    
                                      command=DeleteExportInterface)
    
             close_button.grid(row=0, column=3, padx=10, pady=10)
    
             close_button.config(bg='red', fg='white', font=(
    
                 'Cascadia Code', 12, 'bold'), width=10)
    
         except Exception:
    
             messagebox.showerror(
    
                 'Error', 'Primero ingresa la ip de los dispositivos o haz una prueba para comenzar')
    
     
    
             print(before_hosts)
    
     
    
     
    
     def show_hosts():
    
     
    
         try:
    
             one_host_entry.grid_forget()
    
             one_host_button.grid_forget()
    
             del before_hosts[:]
    
             print(before_hosts)
    
         except Exception:
    
             pass
    
         if number_of_hosts.get() != '':
    
             global entries
    
             label.config(text='Creando entradas..')
    
             entries = []
    
             reset_button = tk.Button(
    
                 hosts_frame, text='Cancelar', command=delete_hosts)
    
             reset_button.grid(row=0, column=12, padx=10, pady=10)
    
             reset_button.config(bg='red', fg='white', font=(
    
                 'Cascadia Code', 8, 'bold'), width=10)
    
             finish_hosts_button = tk.Button(
    
                 hosts_frame, text='Finalizar', command=finish_hosts)
    
             finish_hosts_button.grid(row=0, column=11, padx=10, pady=10)
    
             finish_hosts_button.config(bg='blue', fg='white', font=(
    
                 'Cascadia Code', 8, 'bold'), width=10)
    
             for i in range(int(number_of_hosts.get())):
    
                 global host
    
                 host = tk.Entry(hosts_frame, width=15, font=('Cascadia Code', 7))
    
                 host.grid(row=0, column=i+2, padx=10, pady=10)
    
                 entries.append(host)
    
         else:
    
             messagebox.showerror(
    
                 'Error', 'Elige el numero de ip que vas a ingresar')
    
     
    
         label.config(text='Bien, ahora ingresa las IP en las entradas que creaste')
    
     
    
     
    
     def finish_hosts():
    
         global before_hosts
    
         after_hosts = [entry.get() for entry in entries]
    
         before_hosts = after_hosts
    
         print(before_hosts)
    
         for host in before_hosts:
    
             try:
    
                 conn = pyphox.connect(host)
    
                 conn.execute('/config')
    
                 label.config(text=f'El servidor {host} es valido')
    
             except Exception:
    
                 messagebox.showerror(
    
                     'Error', f'No se pudo conectar con el servidor, verifica la dirección {host}')
    
     
    
     
    
     def delete_hosts():
    
     
    
         before_hosts = ['']
    
         one_host_button.grid(row=0, column=2, padx=20, pady=10)
    
         accept_host_button.grid(row=0, column=0, padx=20, pady=10)
    
         number_of_hosts.grid(row=0, column=1, padx=20, pady=10)
    
         label.config(text='Cancelado')
    
         label.after(1000, lambda: label.config(
    
             text='Selecciona el numero de IP a ingresar o haz una prueba para comenzar'))
    
         for widget in hosts_frame.winfo_children():
    
             if widget.winfo_class() == 'Entry':
    
                 widget.destroy()
    
         for widget in hosts_frame.winfo_children():
    
             if widget.winfo_class() == 'Button':
    
                 widget.destroy()
    
     
    
     
    
     def one_host():
    
         global one_host_entry, accept_button, cancel_button
    
         one_host_button.grid_forget()
    
         accept_host_button.grid_forget()
    
         number_of_hosts.grid_forget()
    
         label.after(100, lambda: label.config(
    
             text='Has entrado al modo de prueba con un solo host'))
    
         label.after(2000, lambda: label.config(
    
             text='Ingresa la el ip del host que tienes en la app'))
    
         accept_button = tk.Button(
    
             hosts_frame, text='Finalizar', command=finish_one_host)
    
         accept_button.grid(row=0, column=3, padx=10, pady=10)
    
         accept_button.config(bg='blue', fg='white', font=(
    
             'Cascadia Code', 8, 'bold'), width=10)
    
         cancel_button = tk.Button(
    
             hosts_frame, text='Cancelar', command=delete_hosts)
    
         cancel_button.grid(row=0, column=4, padx=10, pady=10)
    
         cancel_button.config(bg='red', fg='white', font=(
    
             'Cascadia Code', 8, 'bold'), width=10)
    
         one_host_entry = tk.Entry(hosts_frame, width=15, font=('Cascadia Code', 7))
    
         one_host_entry.grid(row=0, column=2, padx=10, pady=10)
    
         one_host_entry.config(bg='white', fg='black', font=(
    
             'Cascadia Code', 8, 'bold'), width=20)
    
         one_host_entry.focus()
    
     
    
     
    
     def finish_one_host():
    
     
    
         del before_hosts[:]
    
         try:
    
             conn = pyphox.connect(one_host_entry.get())
    
             conn.execute('/config')
    
             one_host_button.grid(row=0, column=2, padx=20, pady=10)
    
             accept_host_button.grid(row=0, column=0, padx=10, pady=10)
    
             number_of_hosts.grid(row=0, column=1, padx=10, pady=10)
    
             accept_button.grid_forget()
    
             cancel_button.grid_forget()
    
             before_hosts.append(one_host_entry.get())
    
             label.config(text=f'Haz introducido: {before_hosts} como ip de prueba')
    
             one_host_entry.config(state='readonly',  justify='center')
    
     
    
         except Exception:
    
             messagebox.showerror(
    
                 'Error', f'No se pudo conectar con el servidor, verifica la dirección {one_host_entry.get()}')

         
    
     
    
     
    
     def credits():
    
         webbrowser.open('https://www.linkedin.com/in/ferney-castano/')
    
     
    
     
    
     def phyphox_help():
    
         webbrowser.open('https://phyphoxconnection.000webhostapp.com/')
    
     
    
     
    
     Phyphox_connection = ThemedTk(theme='arc')
    
     Phyphox_connection.title('Phyphox Connection')
    
     Phyphox_connection.state('zoomed')
    
     Phyphox_connection.attributes('-fullscreen', True)
    
     Phyphox_connection.resizable(False, False)
    
     global hosts
    
     before_hosts = ['']
    
     Header = tk.Frame(Phyphox_connection)
    
     Header.config(bg='black', pady=10, padx=10)
    
     Header.pack(fill='x')
    
     title = tk.Label(Header, text='Phyphox Connection', font=('Cascadia Code', 20))
    
     title.pack(side='top', pady=20)
    
     title.config(bg='black', fg='white')
    
     description = tk.Label(Header, text='En este programa se puede manipular la conexión remota de phyphox, para uno o más dispositivos mediante una petición HTTP al servidor con el comando necesario para ejecutar la acción, por ejemplo, Start => /control?cmd=start  ', font=('Cascadia Code', 8))
    
     description.pack(side='top', pady=0, anchor='w', padx=20)
    
     description.config(bg='black', fg='white')
    
     description = tk.Label(Header, text='', font=('Cascadia Code', 8))
    
     description.pack(side='top', pady=0, anchor='w')
    
     description.config(bg='black', fg='white')
    
     label_number_hosts = tk.Label(
    
         Header, text='Selecciona el numero de hosts a evaluar, si deseas probar la conexion con un solo dispositivo presiona el boton Probar', font=('Cascadia Code', 8))
    
     label_number_hosts.pack(side='left', pady=0, padx=20)
    
     label_number_hosts.config(bg='black', fg='white')
    
     hosts_frame = tk.Frame(Phyphox_connection)
    
     hosts_frame.config(bg='black', pady=10, padx=10)
    
     hosts_frame.pack(fill='x')
    
     number_of_hosts = tk.IntVar()
    
     number_of_hosts = ttk.Spinbox(hosts_frame, from_=2, to=10, width=5, font=(
    
         'Cascadia Code', 8), justify='center')
    
     number_of_hosts.grid(row=0, column=0, padx=20, pady=10)
    
     number_of_hosts.state(['readonly'])
    
     host_frame_Add = tk.Frame(Phyphox_connection)
    
     host_frame_Add.config(bg='black', pady=10, padx=10)
    
     host_frame_Add.pack(fill='x')
    
     accept_host_button = tk.Button(
    
         host_frame_Add, text='Aceptar', command=show_hosts)
    
     accept_host_button.grid(row=0, column=1, padx=20, pady=10)
    
     accept_host_button.config(bg='blue', fg='white', font=(
    
         'Cascadia Code', 8, 'bold'), width=10)
    
     one_host_button = tk.Button(host_frame_Add, text='Probar', command=one_host)
    
     one_host_button.grid(row=0, column=2, padx=20, pady=10)
    
     one_host_button.config(bg='blue', fg='white', font=(
    
         'Cascadia Code', 8, 'bold'), width=10)
    
     credit_button = tk.Button(
    
         host_frame_Add, text='By: FeRsOmBrA', command=credits)
    
     credit_button.place(x=1300, y=10)
    
     credit_button.config(bg='black', fg='white', font=(
    
         'Cascadia Code', 8, 'bold'), width=25)
    
     credit_button.config(relief='raised', borderwidth=10)
    
     credit_button.config(highlightthickness=0,
    
                          highlightbackground='black', highlightcolor='black')
    
     help_button = tk.Button(host_frame_Add, text='Ayuda', command=phyphox_help)
    
     help_button.place(x=1100, y=10)
    
     help_button.config(bg='black', fg='white', font=(
    
         'Cascadia Code', 8, 'bold'), width=25)
    
     help_button.config(relief='raised', borderwidth=10)
    
     connection_label = tk.Frame(Phyphox_connection)
    
     connection_label.config(padx=10, pady=10)
    
     connection_label.pack()
    
     label = tk.Label(connection_label, text='¡Hola!')
    
     label.after(500, lambda: label.config(
    
         text='Selecciona el numero de IP a ingresar o haz una prueba para comenzar'))
    
     label.grid(row=0, column=0, padx=10, pady=10)
    
     label.config(anchor='n', font=('Cascadia Code', 15), pady=20)
    
     buttons = tk.Frame(Phyphox_connection)
    
     buttons.pack()
    
     start_button = tk.Button(buttons, text='Start', command=Start)
    
     start_button.grid(row=0, column=0, padx=20, pady=20)
    
     stop_button = tk.Button(buttons, text='Stop', command=Stop)
    
     stop_button.grid(row=0, column=1, padx=10, pady=10)
    
     export_button = tk.Button(buttons, text='Export', command=show_inputs)
    
     export_button.grid(row=0, column=2, padx=10, pady=10)
    
     clear_button = tk.Button(buttons, text='Clear', command=clear)
    
     clear_button.grid(row=0, column=3, padx=10, pady=10)
    
     Anomaly_Detector_button = tk.Button(
    
         Phyphox_connection, text='--> Phyphox Anomaly Detector <--', command=OpenFilter)
    
     Anomaly_Detector_button.pack(side='bottom', pady=10, padx=20, anchor='se')
    
     exit_button = tk.Button(Phyphox_connection, text='Exit',
    
                             command=Phyphox_connection.destroy)
    
     exit_button.pack(side='bottom', pady=10, anchor='se', padx=20)
    
     start_button.config(bg='green', fg='white', font=('Cascadia Code', 20, 'bold'))
    
     stop_button.config(bg='red', fg='white', font=('Cascadia Code', 20, 'bold'))
    
     export_button.config(bg='blue', fg='white', font=('Cascadia Code', 20, 'bold'))
    
     clear_button.config(bg='#FF0000', fg='white',
    
                         font=('Cascadia Code', 20, 'bold'))
    
     exit_button.config(bg='black', fg='white', font=('Cascadia Code', 10, 'bold'))
    
     Anomaly_Detector_button.config(
    
         bg='red', fg='white', font=('Cascadia Code', 10, 'bold'))
    
     start_button.config(width=20)
    
     stop_button.config(width=20)
    
     export_button.config(width=20)
    
     clear_button.config(width=20)
    
     exit_button.config(width=35)
    
     Anomaly_Detector_button.config(width=35)
    
     buttons.pack(side='bottom', pady=10)
    
     buttons.place(relx=0.5, rely=0.5, anchor='center')
    
     Phyphox_connection.mainloop()



if __name__ == '__main__':
    
     Phyphox_connectionApp()   
     