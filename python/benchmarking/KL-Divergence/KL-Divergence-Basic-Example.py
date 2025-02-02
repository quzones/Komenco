import math

def kl_divergence(P_ref, P_device):
    """
    Calculate KL Divergence between two probability distributions.
    
    :param P_ref: Dictionary representing the reference probability distribution
                  (e.g., simulator), with format {'state': probability}
    :param P_device: Dictionary representing the probability distribution of the
                     quantum device to compare.
    :return: KL Divergence value
    """
    kl_div = 0.0
    
    for state in P_ref:
        p = P_ref.get(state, 0)
        q = P_device.get(state, 0)
        
        if p > 0 and q > 0:
            kl_div += p * math.log(p / q)
        elif p > 0 and q == 0:
            # If q is zero and p is non-zero, the divergence goes to infinity (or a large number).
            kl_div += float('inf')
    
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
    "01": 0.20,
    "10": 0.25,
    "11": 0.25
}

# Calculate KL divergence between reference (simulator) and device 1
kl_device_1 = kl_divergence(P_ref, P_device_1)
print(f"KL Divergence (Simulator || Device 1): {kl_device_1}")
