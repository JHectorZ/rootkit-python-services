import wmi
from win10toast import ToastNotifier

# Function to hide the service
def hide_service(service_name):
    c = wmi.WMI()
    service = c.Win32_Service(Name=service_name)
    result, = service[0].Modify(servicesStartName='')

# Function to monitor Windows services
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

# Name of the service you want to hide
service_name = "Code.exe"

#Funcion of notifications
toaster = ToastNotifier()

# Hide the service
hide_service(service_name)

# Monitor services
monitor_services()