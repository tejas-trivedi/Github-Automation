#!/bin/bash

function create() {
    cd
    python3 create.py $1
    cd D:/Dev/$1
    git init
    git remote add origin https://github.com/tejas-trivedi/$1.git
    touch README.md
    git add .
    git commit -m "Initial commit"
    git push origin master
    code .
}