import sys
import time
import random

import os
import shutil
import logging

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "C:/Users/joaq/Downloads"

class FileEventHandler(FileSystemEventHandler):

    def on_created(self, event):
        print(f"¡Oye, {event.src_path} ha sido creado!")

    def on_deleted(self, event):
        print(f"¡Lo siento! ¡Alguien borró {event.src_path}!")

    def on_modified(self, event):
        print(f"¡Hola!, {event.src_path} ha sido modificado")
    
    def on_moved(self, event):
        print(f"Alguien movió {event.src_path} a {event.dest_path}")
        

event_handler = FileEventHandler()

observer = Observer()

observer.schedule(event_handler, from_dir, recursive=True)

observer.start()

try:
    while True:
        time.sleep(2)
        print("ejecutando...")
except KeyboardInterrupt:
    print("¡detenido!")
    observer.stop()
       