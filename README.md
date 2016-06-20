# coffeeprice

This program is designed to calculate the coffee price for a coffee shop with a single server, i.e. basic application of a M/M/1 queue.

Based on the inputs given;
  -Number of customers expected in an hour (exponential)
  -Service rate of the server (exponential)
  -Goal check out time
  -Customers willingness to pay for a coffee (uniform)
the program first finds what the maximum arrival rate that the stable system can accommodate, and then finds the optimal price based on the maximum arrival rate possible.

The program takes all above parameters as an input and these values can be changed to see how the system reacts to changes in these parameters.

Method
I tried to come up with an object-oriented program, i.e. the program has a M/M/1 class. For an M/M/1 object, you can calculate Ws, Wq, Ls, Lq values easily.
