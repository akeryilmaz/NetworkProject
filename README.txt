----- GROUP MEMBERS -----

Buğra Aker Yılmaz, 2167617
Ekin Tire, 2167369

----- RTT DISCOVERY -----

For RTT discovery scripts to be run successfully, they must be executed in the following order:
1. s_discovery
2. d_discovery
3. r2_discovery
4,5. r1_discovery and r3_discovery; interchangeable.

- The RTT value outputs can be found in the nodes r1,r2 and r3. Output files for the link costs are:
In r1:
- "s.txt" -> r1-s link cost
- "r2.txt" -> r1-r2 link cost
- "d.txt" -> r1-d link cost

In r2:
- "s.txt" -> r2-s link cost
- "d.txt" -> r2-d link cost

In r3:
- "s.txt" -> r3-s link cost
- "r2.txt" -> r3-r2 link cost
- "d.txt" -> r3-d link cost

----- EXPERIMENTS -----

- Commands to be executed for each node and for each experiment is given below.

Before each experiment, for each node s,r3,d; in order to sync time, run:
    $ sudo service ntp stop
    $ sudo ntpdate time.google.com
    $ sudo service ntp start

----- s -----
experiment 1: $ sudo tc qdisc add dev eth3 root netem delay 20ms 5ms distribution normal
experiment 2: $ sudo tc qdisc replace dev eth3 root netem delay 40ms 5ms distribution normal
experiment 3: $ sudo tc qdisc replace dev eth3 root netem delay 50ms 5ms distribution normal
-------------

----- r3 -----
experiment 1:
$ sudo tc qdisc add dev eth1 root netem delay 20ms 5ms distribution normal
$ sudo tc qdisc add dev eth3 root netem delay 20ms 5ms distribution normal

experiment 2: 
$ sudo tc qdisc replace dev eth1 root netem delay 40ms 5ms distribution normal
$ sudo tc qdisc replace dev eth3 root netem delay 40ms 5ms distribution normal

experiment 3: 
$ sudo tc qdisc replace dev eth1 root netem delay 50ms 5ms distribution normal
$ sudo tc qdisc replace dev eth3 root netem delay 50ms 5ms distribution normal
-------------

----- d -----
$ experiment 1: sudo tc qdisc add dev eth1 root netem delay 20ms 5ms distribution normal
$ experiment 2: sudo tc qdisc replace dev eth1 root netem delay 40ms 5ms distribution normal
$ experiment 3: sudo tc qdisc replace dev eth1 root netem delay 50ms 5ms distribution normal
-------------


- After the configurations are made, run the experiment scripts in this order:
$ python3 d_experiment.py
$ python3 r3_experiment.py
$ python3 s_experiment.py

When s_experiment finishes its execution, stop the scripts running on r3 and d, and make the configurations described above for each experiment.
