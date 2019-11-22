----- GROUP MEMBERS -----

Buğra Aker Yılmaz, 2167617
Ekin Tire, 2167369

----- RTT DISCOVERY -----
First, configure r1 and r2 by executing the following bash scripts:
- on r1: discoveryScripts/r1/configureR1.sh
- on r2: discoveryScripts/r2/configureR2.sh

For RTT discovery scripts to be run successfully, they must be executed in the following order:
1. discoveryScripts/s/s_discovery.py
2. discoveryScripts/d/d_discovery.py
3. discoveryScripts/r2/r2_discovery.py
4,5. discoveryScripts/r1/r1_discovery.py and discoveryScripts/r3/r3_discovery.py; interchangeable.

- The RTT value outputs can be found in the nodes r1,r2 and r3. Output files for the link costs are:
In r1:
- discoveryScripts/r1/s.txt -> r1-s link cost
- discoveryScripts/r1/r2.txt -> r1-r2 link cost
- discoveryScripts/r1/d.txt -> r1-d link cost

In r2:
- discoveryScripts/r2/s.txt -> r2-s link cost
- discoveryScripts/r2/d.txt -> r2-d link cost

In r3:
- discoveryScripts/r3/s.txt -> r3-s link cost
- discoveryScripts/r3/r2.txt -> r3-r2 link cost
- discoveryScripts/r3/r3.txt -> r3-d link cost

----- EXPERIMENTS -----

- Commands to be executed for each node and for each experiment is given below.

Before each experiment, for each node s,r3,d; in order to sync time, run:
    $ sudo service ntp stop
    $ sudo ntpdate time.google.com
    $ sudo service ntp start

For the configuration of Emulated Delays, run:

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
