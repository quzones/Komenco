import math

def kl_divergence(P_ref, P_device, epsilon=1e-10):
    """
    Calculate KL Divergence between two probability distributions.
    Handles missing or zero probabilities by applying smoothing.
    
    :param P_ref: Dictionary representing the reference probability distribution
                  (e.g., simulator), with format {'state': probability}
    :param P_device: Dictionary representing the probability distribution of the
                     quantum device to compare.
    :param epsilon: Small smoothing value to avoid division by zero and log(0).
    :return: KL Divergence value
    """
    kl_div = 0.0
    
    # Get the union of states from both distributions
    all_states = set(P_ref.keys()).union(set(P_device.keys()))
    
    for state in all_states:
        # Get probabilities, use epsilon to handle missing states or zero values
        p = P_ref.get(state, epsilon)
        q = P_device.get(state, epsilon)
        
        # Only calculate contribution if P_ref[state] > 0
        if p > 0:
            kl_div += p * math.log(p / q)
    
    return kl_div

# Example usage
P_ref = {
    "00": 0.25,
    "01": 0.25,
    "10": 0.25,
    "11": 0.25
}

P_device_1 = {
    "00": 0.30,
    "10": 0.25,
    "11": 0.25  # Missing "|01⟩"
}

# Calculate KL divergence between reference (simulator) and device 1
kl_device_1 = kl_divergence(P_ref, P_device_1)
print(f"KL Divergence (Simulator || Device 1): {kl_device_1}")
