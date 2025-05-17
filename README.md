# Synthetic Biology Ring Oscillator 🧬🔁

A numerical simulation of a **genetic inverter** and a **ring oscillator** circuit, built using Python.  
Inspired by **MIT's 20.180 Synthetic Biology course**, this project models the behavior of gene regulatory networks using **protein production, decay dynamics**, and **PoPS signal regulation**.


---

## 🧠 What This Project Does

- Simulates a **protein generator** using PoPS input and models repressor concentration over time.
- Models a **PoPS regulator** that applies second-order repression kinetics to produce a regulated PoPS output.
- Combines both into a functional **inverter** (genetic NOT gate).
- Chains multiple inverters into a **ring oscillator**, a foundational synthetic circuit.
- Uses **Euler's method** for numerical integration.

---

## 📐 Biological Background

### Inverter Design

Each inverter models the following:

- **Protein Generator**:  
  $\frac{dR}{dt}$ = $\text{Productionrate} \times \text{PoPS}{in}$ - $k_d \times R$
  Where:
  - $\( R \)$ is the concentration of repressor protein.
  - $\( k_d = \frac{\ln 2}{t_{1/2}} \)$

- **PoPS Regulator** (Repression Kinetics):  
  $\text{PoPS}_{out}$ = $\text{PoPS}{max} \times \frac{k_D}{k_D + R}$

  This models a binding equilibrium where the repressor \( R \) binds to DNA and blocks transcription.

### Ring Oscillator

- A loop of 3 (or more) inverters where output of one becomes input to the next.
- Odd number of inverters introduces signal oscillation over time.

---

## 🛠️ Files and Structure

```bash
inverter.py         # Classes for ProteinGenerator, PoPSRegulator, and Inverter
ring_oscillator.py  # Chains inverters into a functional oscillator
```

## 📊 Sample Output
```
Input Signal : 70 PoPS
Output Signal : 0.0689 PoPS

Repressor Protein : 1014.49

Output : 0.0689
Output : 35.0172
Output : 0.1376
Output : 23.3716
...
```


## 📌 Notes

- Simulation assumes steady-state protein production unless otherwise specified.
- Time step dtdt and total simulation time are adjustable.
- All constants (e.g., kDkD​, half-life) are biologically inspired, but simplified.

