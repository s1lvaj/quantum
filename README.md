# IBM Quantum Computers

Qiskit is IBM’s opensource Python SDK for building, simulating, and running quantum circuits on both local simulators and real IBM quantum hardware. It provides high-level tools for circuit design, execution, and analysis, making quantum computing accessible for research, education, and experimentation.

In this repository, we built a custom interface to communicate with IBM's quantum computers. The project's simplicity, together with some documentation, mainly serves as a means to fascinate and give motivation to the reader to explore qiskit's capabilities.

While quantum computing, at the time of writing, is still considered a "mystery" by many, there are several tools available that allow anyone to explore this world, even if they know nothing of quantum mechanics, or even of general physics. So here we present a very minimalist code to show how any person can start this journey to create interesting projects.

# Quantum Tunneling Simulation

The project here presented allows the user to simulate a particle passing through a barrier, where the probability is calculated in a quantum computer, emmulating quantum tunneling effects. This program is activated by running `GUI.py`.

<img src="./doc/GUI.png" width="750">

The graphical user interface, as presented in the image above, has 4 inputs:
- Your IBM API key, which you need to go get in your IBM Qiskit account, if you still don't have one.
- A drop down menu with 2 backends to choose from (a simulator and a quantum computer).
- The barrier strength.
- The number of shots/particles to fire at the barrier.

We assume we have a laser shooting that amount of particles. Their velocity is a random value between 0 and 1 and the probability of passing the barrier (result |01>) or not (result |00>) is calculated in order to emmulate quantum tunneling, as soon as the user presses the button "Run Circuit". The button "Save Plot" can also be pressed in order to save the image as a .png file.

Besides the `GUI.py`, which the user has to run to get the custom interface, inside the folder `circuits`, one can find the needed code to make this work, namely, `circuit_layout.py`, where the basic quantum gates are presented, as well as the opportunity to create simple systems and "oracles" (black boxes) with them, `run_circuit.py`, where we define how we call Qiskit's backend and run the simulation, and `tunneling.py`, where we combine the previous two in a simple game to emmulate tunneling effects.

Documentation from the Faculty of Sciences of University of Porto (in portuguese) can be seen in the folder `doc`. More information can be seen on qiskit's official textbook: https://qiskit.org/textbook/preface.html or in their youtube channel.
