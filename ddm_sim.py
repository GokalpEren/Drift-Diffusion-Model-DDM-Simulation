import numpy as np
import matplotlib.pyplot as plt

# Modify parameters as needed
drift = 0.10
noise = 0.6
boundary = 1.0
timestep = 0.01
maxtime = 10.0
bias = 0.0
n_trials = 10000

def run_trial(drift, noise, boundary, timestep, maxtime, bias):
    evidence = bias
    time = 0.0

    while abs(evidence) < boundary and time < maxtime:
        evidence += drift * timestep + noise * np.sqrt(timestep) * np.random.randn() # Standard DDM equation
        time += timestep

    if evidence >= boundary:
        decision = 1
    elif evidence <= -boundary:
        decision = -1
    else:
        decision = 0
    return decision, time

decisions = []
reaction_times = []

# Do trials
for _ in range(n_trials):
    d, t = run_trial(drift, noise, boundary, timestep, maxtime, bias)
    decisions.append(d)
    reaction_times.append(t)

rt_pos = [t for d, t in zip(decisions, reaction_times) if d == 1]
rt_neg = [t for d, t in zip(decisions, reaction_times) if d == -1]
rt_timeout = [t for d, t in zip(decisions, reaction_times) if d == 0]

n_pos = len(rt_pos)
n_neg = len(rt_neg)
n_timeout = len(rt_timeout)

timeout_rate = n_timeout / n_trials

# Plots
plt.figure(figsize=(12, 4))

plt.subplot(1, 3, 1)
plt.hist(rt_pos, bins=30)
plt.title(f"Decision +1 (n = {n_pos})")
plt.xlabel("RT (s)")
plt.ylabel("Count")

plt.subplot(1, 3, 2)
plt.hist(rt_neg, bins=30)
plt.title(f"Decision -1 (n = {n_neg})")
plt.xlabel("RT (s)")

plt.subplot(1, 3, 3)
plt.hist(rt_timeout, bins=30)
plt.title(f"Timeout (n = {n_timeout})")
plt.xlabel("RT (s)")

plt.tight_layout()
plt.show()

