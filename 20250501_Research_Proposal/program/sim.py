import numpy as np
import matplotlib.pyplot as plt
from collections import Counter

states = ['Urn1', 'Urn2', 'Urn3']
observations = ['Red', 'Blue']
start_probability = np.array([0.6, 0.3, 0.1])
transition_probability = np.array([
    [0.7, 0.2, 0.1],
    [0.3, 0.5, 0.2],
    [0.2, 0.3, 0.5]
])
emission_probability = np.array([
    [0.6, 0.4],
    [0.4, 0.6],
    [0.7, 0.3]
])


def simulate_hmm(start_prob, trans_prob, emiss_prob, n_steps):
    states_list = []
    observations_list = []

    current_state = np.random.choice(len(start_prob), p=start_prob)
    for _ in range(n_steps):
        states_list.append(current_state)
        observation = np.random.choice(
            len(emiss_prob[current_state]), p=emiss_prob[current_state])
        observations_list.append(observation)
        current_state = np.random.choice(
            len(trans_prob[current_state]), p=trans_prob[current_state])

    return states_list, observations_list


n_steps = 100
states_sequence, observations_sequence = simulate_hmm(
    start_probability, transition_probability, emission_probability, n_steps)

state_counts = Counter(states_sequence)
observation_counts = Counter(observations_sequence)

state_observation_counts = {state: Counter() for state in range(len(states))}
for state, observation in zip(states_sequence, observations_sequence):
    state_observation_counts[state][observation] += 1

print("State Counts:", state_counts)
print("Observation Counts:", observation_counts)

state_observation_probabilities = {
    state: {obs: count / state_counts[state]
            for obs, count in obs_counts.items()}
    for state, obs_counts in state_observation_counts.items()
}
print("State-Observation Probabilities:", state_observation_probabilities)

time_steps = np.arange(n_steps)
state_names = [states[s] for s in states_sequence]
observation_colors = ['red' if o ==
                      0 else 'blue' for o in observations_sequence]

plt.figure(figsize=(15, 5))

plt.subplot(2, 1, 1)
plt.plot(time_steps, state_names, 'bo-', label='State')
plt.xlabel('Time Steps')
plt.ylabel('State')
plt.title('State Sequence')

plt.subplot(2, 1, 2)
plt.scatter(time_steps, observations_sequence,
            c=observation_colors, s=50, label='Observation')
plt.xlabel('Time Steps')
plt.ylabel('Observation')
plt.title('Observation Sequence')
plt.yticks([0, 1], ['Red', 'Blue'])

plt.tight_layout()
plt.show()
