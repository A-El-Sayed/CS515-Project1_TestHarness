# Test Harness - Project 1 - CS515

- Ali El Sayed aelsaye1@stevens.edu
- https://github.com/A-El-Sayed/CS515-Project1_TestHarness
- It took me about 20 hours
- the way I tested my code is by running it on terminal and started debugging the code using breakpoints on vs code
- I had a lot of bugs, but thankfully i was able to get it all to work
- I had an issue with the test.py program where i could not allow the subprocess to run the actual command lines that were in the PROG.NAME.in files. However, after carefulling debugging the test.py file and realizing that i was using subprocess.communicate instead of subprocess.run and that's why it wasn't working.
- for the three extentions i've chosen to implement, i chose to do "the more advanced wc: multiple files", "more advanced wc: flags to control output", and "More advanced gron: control the base-object name".

## Extensions -  the path file may vary depending on where you are in the directory
### WC extension: flags to control ouput
- in order to run this,
```
python wc.py [-h] [-l] [-w] [-c] [files ...]
#EXAMPLE: python wc.py -lw foo.txt
#EXAMPLE: python wc.py -l -w foo.txt
#EXAMPLE: python wc.py -wc foo.txt
#EXAMPLE: cat foo.txt | python wc.py -l
```
### WC extension: multiple files
- in order to run this,
```
python wc.py [-h] [-l] [-w] [-c] [files ...]
#EXAMPLE: python wc.py foo.txt bar.txt
#EXAMPLE: python wc.py -l -w foo.txt bar.txt
#EXAMPLE: cat foo.txt bar.txt | python wc.py 
```

### GRON extension: control the base-object name
- in order to run this,
```
python gron.py [-h] [--obj base_object] [filename]
#EXAMPLE: python gron.py eg.json --obj o
#EXAMPLE: python gron.py --obj a eg.json
#EXAMPLE: cat eg.json | python gron.py --obj a
```
