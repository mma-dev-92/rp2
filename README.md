# How to run the program

To run this program first create python virtual environment:

```commandline
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Note: it is possible, that instead of `python3` you need to use a path to a python3 interpreter on your machine.

Next, create an *.ini file with the following structure and save it on the machine, on which you are currently working 
on.

```ini
[car_wash]
n = <int>
t_0 = <float>
a = <float>
P = <float>

[checkout_queue]
a = <int>
t_0 = <float>
Q = <float>
L = <int>
```

It contains two sections: `car_wash` and `checkout_queue`. First section contains parameters for exercise 2 (car wash
queue problem), second section contains parameters for exercise 3 (checkout queue problem). Parameter names match the 
naming convention from the problem list. Please, provide values for each parameter and save the file.

To calculate car wash problem and checkout queue problem, simply run (from the root directory) the following command

```commandline
python -m src ini_file_path
```

where the `ini_file_path` is the path to your *.ini file, that you have created in previous step.

Once you run the program, results will be displayed in the console.