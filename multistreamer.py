import subprocess
import os
import time
from colorama import Fore
from pystyle import Center, Colors, Colorate
from tkinter import Tk, filedialog


os.system(f"title Kichi779 - Twitch Multistream Bot v1.0.0 ")

def check_for_updates():
    try:
        r = requests.get("https://raw.githubusercontent.com/Kichi779/Twitch-Multi-Stream/main/version.txt")
        remote_version = r.content.decode('utf-8').strip()
        local_version = open('version.txt', 'r').read().strip()
        if remote_version != local_version:
            print("A new version is available. Please download the latest version from GitHub.")
            time.sleep(3)
            return False
        return True
    except:
        return True


def main():
    if not check_for_updates():
        return

def print_announcement():
    try:
        r = requests.get("https://raw.githubusercontent.com/Kichi779/Twitch-Multi-Stream/main/announcement.txt", headers={"Cache-Control": "no-cache"})
        announcement = r.content.decode('utf-8').strip()
        return announcement
    except:
        print("Could not retrieve announcement from GitHub.\n")

    print(Colorate.Vertical(Colors.red_to_green, Center.XCenter("""
           
                       ▄█   ▄█▄  ▄█    ▄████████    ▄█    █▄     ▄█  
                       ███ ▄███▀ ███   ███    ███   ███    ███   ███  
                       ███▐██▀   ███▌  ███    █▀    ███    ███   ███▌ 
                      ▄█████▀    ███▌  ███         ▄███▄▄▄▄███▄▄ ███▌ 
                     ▀▀█████▄    ███▌  ███        ▀▀███▀▀▀▀███▀  ███▌ 
                       ███▐██▄   ███   ███    █▄    ███    ███   ███  
                       ███ ▀███▄ ███   ███    ███   ███    ███   ███  
                       ███   ▀█▀ █▀    ████████▀    ███    █▀    █▀   
                       ▀                                             
 Improvements can be made to the code. If you're getting an error, visit my discord.
  
                             Github  github.com/kichi779    """)))

announcement = print_announcement()
print("")
print(Colors.red, Center.XCenter("ANNOUNCEMENT"))
print(Colors.yellow, Center.XCenter(f"{announcement}"))
print("")
print("")


print(Colors.green, ("Select a file to stream .MP4 .PNG .GIF"))

def choose_file():
    root = Tk()
    root.withdraw()  

    file_path = filedialog.askopenfilename(title="Select a file to stream", filetypes=[("Video/Image Files", "*.mp4 *.png *.gif")])

    root.destroy()

    return file_path

def authenticate_user():
    pass

def check_file_exists(filename):
    if not os.path.isfile(filename):
        print("Error: The file was not found!")
        time.sleep(5)
        return False
    return True

def check_file_extension(filename):
    valid_extensions = [".mp4", ".png", ".gif"]
    file_extension = os.path.splitext(filename)[1]
    if file_extension.lower() not in valid_extensions:
        print("Error: Unsupported file extension!")
        time.sleep(5)
        return False
    return True

def start_streaming(filename, stream_key):
    music_file_path = os.path.join("data", "music.mp3")
    command = (
        f'ffmpeg -stream_loop -1 -re -i "{filename}" -stream_loop -1 -i "{music_file_path}" '
        f'-c:v libx264 -preset veryfast -b:v 3000k -maxrate 3000k -bufsize 6000k '
        f'-pix_fmt yuv420p -g 50 -c:a aac -b:a 160k -ac 2 -ar 44100 '
        f'-f flv "rtmp://live.twitch.tv/app/{stream_key}"'
    )
    subprocess.Popen(command, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL) 
    print("The broadcast has started")

def main():

    print("")
    selected_file = choose_file()

    if not selected_file:
        return

    filename = os.path.basename(selected_file)

    if not check_file_exists(selected_file):
        return

    if not check_file_extension(selected_file):
        return

    with open('stream_keys.txt', 'r') as keys:
        for key in keys:
            key = key.strip()
            authenticate_user()
            start_streaming(selected_file, key)


    stop_broadcast = input("Type 'y' to stop all broadcasts: ")
    if stop_broadcast.lower() == 'y':
        subprocess.run(['taskkill', '/f', '/im', 'ffmpeg.exe'])
        pass

if __name__ == "__main__":
    main()

# ==========================================
# Copyright 2023 Kichi779

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
# ==========================================
