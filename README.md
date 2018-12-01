# Advent of Code
A space for my work participating in advent of code

## Usage

From a particular day folder, the `main.py` module can be run with the day's
input, using:

```bash
python ./lib/main.py input.txt
```

### Running tests

First install the `nose` package:

```bash
pip install nose
```

If the executables aren't installed on the OS, you may need to run either of
these:
```bash
sudo apt install pyton-pip
sudo apt install pyton-nose
```

Then run nosetests from a day directory, e.g. from /2017/01:

```bash
nosetests -vs
```
