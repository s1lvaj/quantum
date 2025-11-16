# Introduction to Quantum Computers

In this repository, we built a custom interface to communicate with IBM's opensource quantum computers. It allows to simulate a particle passing through a barrier, where the probability is calculated in a quantum computer, emmulating quantum tunneling effects. This program is activated by running `GUI.py`.

<img src="./doc/GUI.png" width="750">

The graphical user interface, as presented in the image above, has 4 inputs:
- Your IBM API key, which you need to go get in your IBM Qiskit account, if you still don't have one.
- A drop down menu with 2 backends to choose from (a simulator and a quantum computer).
- The barrier strength.
- The number of shots/particles to fire at the barrier.

We assume we have a laser shooting that amount of particles. Their velocity is a random value between 0 and 1 and the probability of passing the barrier (result |01>) or not (result |00>) is calculated in order to emmulate quantum tunneling, as soon as the user presses the button "Run Circuit". The button "Save Plot" can also be pressed in order to save the image as a .png file.

Besides the `GUI.py`, which the user has to run to get the custom interface, inside the folder `circuits`, one can find the needed code to make this work, namely, `circuit_layout.py`, where the basic quantum gates are presented, as well as the opportunity to create simple systems and "orcales" (black boxes) with them, `run_circuit.py`, where we define how we call Qiskit's backend and run the simulation, and `tunneling.py`, where we combine the previous two in a simple game to emmulate tunneling effects.

Documentation from the Faculty of Sciences of University of Porto can be seen in the folder `doc`. More information can be seen on qiskit's official textbook: https://qiskit.org/textbook/preface.html or in their youtube channel.