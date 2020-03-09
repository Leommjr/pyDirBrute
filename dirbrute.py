# -*- coding: utf-8 -*-

import argparse
import requests
import sys
import threading
from termcolor import colored

def brute(wl,url):
    for word in wl:
        urlz = url.replace("FUZZ",word)
        r= requests.get(urlz)
        print(urlz + " -- "+ r.status_code)

def divide_file_t(wordlist,t):
    try:
        with open(wordlist) as f:
            dirs = f.read()
        dirsl = dirs.split("\n")
        med = len(dirsl)/t
        med = int(med)
        lp = [[] for _ in range(t)]
        for i in range(t):
            for _ in range(med):
                lp.append(dirsl.pop())
            if(i == t-1):
                while(len(lista)!= 0):
                    lp[i].append(dirsl.pop())
        return lp
    except(FileNotFoundError):
        print("Arquivo nao encontrado")
        sys.exit(1)

    except:
        print("Erro ao dividir arquivo")
        sys.exit(1)

#######################################MAIN###################################################
parser = argparse.ArgumentParser(description="Bruteforce web dir.")
parser.add_argument("-u", "--url", dest='url', type=str,help="specify url address with FUZZ")
parser.add_argument("-w", "--wordlist", dest='wl', type=str,help="specify wordlist")
parser.add_argument("-t", "--threads", dest='t', default=2, type=int,help="number of threads")
args = parser.parse_args()
if(len(sys.argv) < 3):
    parser.print_help()
    sys.exit(1)
else:
    url = args.url
    wl = args.wl
    t = args.t
    lp = divide_file_t(wl,t)
    for index in range(t):
        x = threading.Thread(target=brute,args=(url,lp[index]))
        x.start()
