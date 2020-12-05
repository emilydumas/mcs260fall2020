# tkinter examples

These example programs accompany lectures 36, 38, 40, and 43 of MCS 260 (Fall 2020, instructor David Dumas).

There are two applications here that are essentially equivalent in functionality. One was developed in each of the two course lectures (10am and 2pm), and each exists in several versions.  The applications were given arbitrary names that do not reflect their functionality.

Both applications implement an alphabet rotation code (e.g. ROT13) with a slider to select the amount of rotation.

* [lasercode.py](lasercode.py) and [sharkencode.py](sharkencode.py) - Original application.  Encoding runs in the main thread.
* [lasercode2.py](lasercode2.py) and [sharkencode2.py](sharkencode2.py)- Modified version with slow encoding (1s delay).  Suffers from unresponsive GUI.
* [lasercode3.py](lasercode3.py) and [sharkencode3.py](sharkencode3.py)- Multi-threaded version that moves slow encoding to a worker thread, keeping the GUI responsive.