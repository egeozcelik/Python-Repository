import time


#parametre almayan callback functions

def download_data(callback):
    print("Downloading Data...")
    time.sleep(2)
    print("Download Completed.")
    callback()




def start_process():
    print("processing downloaded data...")


download_data(start_process)