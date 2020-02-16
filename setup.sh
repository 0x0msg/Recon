#!/bin/bash

function sublister {
  #cloning sublister
  git clone https://github.com/aboul3la/Sublist3r.git

  #entering sublister directory
  cd Sublist3r/

  #installing requirements of sublister
  pip install -r requirements.txt

  #installing sublister
  python setup.py install

  #coming out of directory
  cd ..
}

function amass {
    #install amass
    apt-get install amass
}

function crtndstry {
  #cloning crtndstry repo
  git clone https://github.com/nahamsec/crtndstry.git
}

function knockpy {
  #cloning knockpy repo
  git clone https://github.com/guelfoweb/knock.git
  #entering knock
  cd knock/
  #installing requirements
  pip install -r requirements.txt
  #installing knock
  python setup.py install
  #out of dir
  cd ..
}

function subbrute {
  #cloning the repo
  git clone https://github.com/TheRook/subbrute.git

}

function assetfinder{
  go get -u github.com/tomnomnom/assetfinder
}

sublister
amass
crtndstry
knockpy
subbrute
assetfinder