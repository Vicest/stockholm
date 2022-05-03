#Stockholm

A python3 program replicating the behaviour of the wannacy ransomware for predagogical purposes. It will infect and reverse the infection of files within the contained environment of the $HOME/infection folder. It uses the symmetrical encryption method AES.

##Usage
To run, make sure you have installed `python3`, and the test folder `$HOME/infection` with some files in it to infect.
Help menu
```Shell
python3 stockholm.py -h
```
Infect files
```Shell
python3 stockholm.py
```
Silence output
```Shell
python3 stockholm.py -s
```
Revert the infection
```Shell
python3 stockholm.py -r <key>
```
Since the encryption is symmetrical, decription key and encryption key are the same:
>`"a quien buen arbol se arrima ..."`
```Shell
python3 stockholm.py -r "a quien buen arbol se arrima ..."
```
