#!/bin/bash
gcc -c -fPIC hack.c -o hack
gcc --share hack -o hack.so
