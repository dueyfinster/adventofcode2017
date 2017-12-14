#!/usr/bin/env python3
import os
from subprocess import call

def list_files():
    return [each for each in os.listdir("2017") if each.endswith('.py')]

def run_script(script):
    call(["python", script])

def main():
	files = list_files()
	for file in files:
	    run_script("2017/"+file)


if __name__ == '__main__':
    main()
