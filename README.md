# Google-sheets-api-parser
Script that takes data from auction website and renew data in your google sheet automaticaly
every 15 minnutes

# Installation
Clone the repository using

git clone https://github.com/samoilenkoa7/Google-sheet-api-parser.git
or download it directly from github.

Then install all required packages:

pip install requirements.txt
# Usage

Main func is located at

./carParser/main.py , just run it.

You need to create your google development account, start project, create service account

and install credentials, rename it to saac1.json and move to .carParser/creds/.

Also, if you want work using API Key, insert it to ./carParser/creds/__init__.py