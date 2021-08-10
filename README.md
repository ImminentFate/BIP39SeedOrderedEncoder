# BIP39 Seed Ordered Encoder
Encoded a BIP39 Seedphrase into a non-ordered list of encoded strings


Takes an input of 6/12/24-word seed phrases and converts them into a non-ordered list of Base26 encoded characters, _while retaining the original position information from the seedphrase_

This means you can then take the resulting list and split it up however you want; each word contains its own position information so it doesn't matter if you scramble the order afterwards. 

This is mostly a novelty, but it could be handy if you want to split up your seed list into arbitrary groups and store them separately (For example stamping each code into a separate piece of metal and storing them in 24 different locations). 


## Example:
The following **ordered** seed:
01. Increase
02. Total
03. Income
04. Gain
05. Future
06. Security
07. Hold
08. Until
09. Moon
10. Then
11. Retire
12. Rich

Becomes the following **unordered** list:

- BJH
- FTN
- HKW
- KFP
- NGI
- RLZ
- TMG
- YAY
- ZYQ
- BDYG
- BGMR
- BJNX

# Video Example
[See here](https://giant.gfycat.com/RectangularBlushingIberiannase.mp4)


# Requirements
- Python 3.6+
- English.txt (or other wordlist) stored next to the python script

# How to run
Run in any console (tested on Windows with `Powershell` but hopefully works fine on Mac/Linux)

**For safety, it's probably best to run this on an offline computer if there's any chance you have a virus/keylogger**

```py
python B39SeedEncoder.py
```



I was going to make this a standalone program with a user interface, but it's generally better to let people see the code they're about to run when dealing with sensitive information. 

