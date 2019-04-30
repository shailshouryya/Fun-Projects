import argparse
parser = argparse.ArgumentParser()
parser.add_argument("echo")
args = parser.parse_args()
print (args.echo)

'''
Here is what’s happening:

    We’ve added the add_argument() method, which is what we use to specify which command-line options the program is willing to accept. In this case, I’ve named it echo so that it’s in line with its function.
    Calling our program now requires us to specify an option.
    The parse_args() method actually returns some data from the options specified, in this case, echo.
    The variable is some form of ‘magic’ that argparse performs for free (i.e. no need to specify which variable that value is stored in). You will also notice that its name matches the string argument given to the method, echo.

Note however that, although the help display looks nice and all, it currently is not as helpful as it can be. For example we see that we got echo as a positional argument, but we don’t know what it does, other than by guessing or by reading the source code. So, let’s make it a bit more useful:
'''