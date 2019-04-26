# easyexception

Conveniently submit and print an error, warning, or message from your codes, and specify where the error, warning, or message came from.

### Purpose
When one raise an exception in his/her program, or throws a warning, on the screen it is often unclear where the error/warning/message was initiated. This makes it hard for users of the program to troubleshoot the problem.

In **easyexception**, this is solved by a simple trick, we combine all kinds of screen messages into one function: \
`easyexception(origin, code, severity, msg)`\
where *severity* can be "Error", "Warning", or "Message"

### Usage

The program developer just calls the function to define the above information and deliver the message to the user screen. e.g. if you are developing a calculator program and the user puts in a negative number and then presses "Square Root". You want to throw a warning but not to stop the program, you may do:

    easyexception("mymath.py", "calculate_sqrt(n)", "Warning",
    "Can not give the square root for a negative number")

The above assumes `easyexception` is called in function `calculate_sqrt(n)` in file mymath.py.

Or, if the user magically puts some texts in the input bar, and you hate it so much that you would like to raise an Error and stop the program. You may then do:

    easyexception("get_user_input.py", "eval_expr(eq)", "Error",
    "Texts are not allowed in the input bar!")

Similarly, the above assumes `easyexception` is called in function `eval_expr(eq)` in file get_user_input.py.

Finally, `severity="Message"` can be used if you want to notify the user that a calculation is complete, or the user has cleared the memory, etc.


### Installation
Install easyexception using `pip`, or `pip3`

    pip install easyexception

### Repository
[GitHub page](https://github.com/frankliuao/easyexception)
