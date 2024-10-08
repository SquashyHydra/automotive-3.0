# automotive-3.0
Fork of MikeyPPPPPPPP automotive-2.0 code they wrote to download movies from an illegal streaming website.

# Requirments:
## Python Requirements
```
pip install -r requirements.txt
```

## System Requirements
```
FoxyProxy (Chrome/FireFox Browser extention https://www.google.com/search?q=foxyproxy+extension)
mitmproxy (install guide https://docs.mitmproxy.org/stable/overview-installation/)
ffmpeg    (install guide https://www.ffmpeg.org/download.html)
```

# Setup

1. Navigate in your file explorer to ```~/.mitmproxy/``` on linux and ```%userprofile%/.mitmproxy/``` on windows, if this is your first time using mitmproxy, the file location will not exist.
2. If you cannot locate the folder ```~/.mitmproxy/``` or ```%userprofile%/.mitmproxy/``` if it is not there download automotive and start the [automotive exe](https://github.com/SquashyHydra/automotive-3.0/releases/tag/automotive-windows-only-executable) or [source](https://github.com/SquashyHydra/automotive-3.0) untill the terminal changes yet.
3. Find the file called ```mitmproxy-ca-cert.cer``` in the ```.mitmproxy``` folder there are other CA certificates there if your browser does not support this one.
4. Next we open your browser of choice personally i use Firefox (cause it doesn't cause any errors over TLS), but this should be the same for most browsers.
5. Navagate to your browsers settings and search for **certificates**.<br>![Screenshot 2024-08-12 114823](https://github.com/user-attachments/assets/dd59f9a6-9523-4df5-9140-5863521a2583) ![Screenshot 2024-08-12 115130](https://github.com/user-attachments/assets/eeafdc89-2127-4a63-8a1f-2ee0695ae337)<br>
6. Now you are going to want to view or manage your certificates to import the new ```mitmproxy-ca-cert.*```.<br>![Screenshot 2024-08-12 115513](https://github.com/user-attachments/assets/fc9d8df4-6208-4a3f-92e0-7dc1d18a9a8a) ![Screenshot 2024-08-12 115619](https://github.com/user-attachments/assets/01cc04eb-4dda-49f7-b866-a1e742c340f0)<br>
8. Click **Import** and navagate to the ```.mitmproxy/``` folder and select one of the certificates ```.cer``` should work in most cases.<br>![Screenshot 2024-08-12 120532](https://github.com/user-attachments/assets/cd14f187-39ba-4f03-8334-92c2eb3cb8d7)<br>
9. If you where getting any certificate errors in your browser they should be gone now.
10. After you have install ```mitmproxy-ca-cert```, it is time to setup **foxyproxy**.
11. First navigate to the foxyproxy extension and open the **options** setting.<br>![Screenshot 2024-08-12 160534](https://github.com/user-attachments/assets/731a83f7-d254-4dc1-8093-22140f05d0a0)<br>
12. Then go to the **proxies** tab and click **add**.<br>![Screenshot 2024-08-12 160748](https://github.com/user-attachments/assets/24a43a77-967d-4317-835a-e72db6375ef4)<br>
13. New configure your connection for the ```ip: localhost``` and ```port: 8080``` and name it how you would like to and click save.<br>![Screenshot 2024-08-12 161148](https://github.com/user-attachments/assets/5570cd73-6b0e-468e-97f5-521e8124c96d)<br>

# How To:

1. Start the program and enter the movie name
2. Setup your browser proxy to connect to *:8080 (basicly one click with Foxy Proxy)
3. Play the movie normaly until the program starts downloading (This should be instant from pressing play on the movie)
4. Enjoy!
   
# Usage:
```
usage: app.py [-h] [-r] [-d DESTINATION]

Manage movie folder location.

options:
  -h, --help            show this help message and exit
  -r, --reset           Reset movie's folder location
  -d DESTINATION, --destination DESTINATION
                        Specify the movie's folder location
```

# Demo Video (Youtube)
<a href="http://www.youtube.com/watch?feature=player_embedded&v=CeK18eqvpwo" target="_blank"><img src="http://img.youtube.com/vi/CeK18eqvpwo/0.jpg" alt="Youtube Video" width="240" height="180" border="10" /></a>

# Info

The site must just let you stream basically any movie or show you want. This works on another sites, but they fixed the bug,
not really - they just made it harder and also there selection was ... meh. This site is big and very popular with numerous
UI/UX updates. Theres a Cloudflare WAF along with a bunch of anti-dubugging techniques being used. Unfortunately for them,
with enough effort and time - anything is possible, especially with code.

## Python Modules Used
```python
from requests import Response
from requests import get
from concurrent.futures import ThreadPoolExecutor
from os import system
from os import remove
from os import mkdir
from os.path import exists
from os.path import isdir
from shutil import move
from shutil import rmtree
from time import sleep
from tkinter import filedialog
from mitmproxy import ctx
import tkinter as tk
import mitmproxy
import re
import argparse
import configparser
```
