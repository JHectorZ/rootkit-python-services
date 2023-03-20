import wmi
from win10toast import ToastNotifier

# Función para ocultar el servicio
def hide_service(service_name):
    c = wmi.WMI()
    service = c.Win32_Service(Name=service_name)
    result, = service[0].Modify(servicesStartName='')

# Función para monitorear los servicios de Windows
def monitor_services():
    c = wmi.WMI()
    process_watcher = c.Win32_Process.watch_for("Creation")
    while True:
        try:
            process_created = process_watcher()
            process_owner = process_created.GetOwner()
            process_name = process_created.Name
            message = f"Se ha creado un nuevo servicio: {process_name}, \nProveniente: \n{process_owner}"
            toaster.show_toast("Nuevo servicio", message, duration=5)
            
        except:
            continue

# Nombre del servicio que se desea ocultar
service_name = "Code.exe"

#Funcion de notificaciones
toaster = ToastNotifier()

# Ocultar el servicio
hide_service(service_name)

# Monitorear los servicios
monitor_services()