# Vacuum-Cleaner-World
# SIMPLE AGENT FUNCTION FOR THE VACUUM-CLEANER WORLD IN PYTHON

The code essentially allows the user to simulate the actions of a vacuum cleaner for different percept sequences and displays the actions taken in each case. The vacuumcleaner function encapsulates the logic for deciding the actions based on the percepts received.

The vacuum cleaner, represented by an agent, receives percept information about the state of two locations (A and B) and decides on actions to perform. The possible percepts are whether a location is clean or dirty.

The logic in the function is as follows:

If location A is clean, the vacuum cleaner moves to the right.
If location A is dirty, the vacuum cleaner sucks the dirt and updates its status to clean.
If location B is clean, the vacuum cleaner moves to the left.
If location B is dirty, the vacuum cleaner sucks the dirt and updates its status to clean.
