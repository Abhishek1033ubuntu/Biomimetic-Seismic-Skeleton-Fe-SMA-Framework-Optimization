"""
Thermal Modelling Framework: Transient Solidification & Heat Transfer Gradient Solvers
Project: Biomimetic Seismic Skeleton Optimization
License: MIT License

Disclaimer: This is a generalized macro-thermal cooling model using reference 
heat dissipation factors. Exact industrial casting setup constants are proprietary.
"""

import numpy as np
import matplotlib.pyplot as plt

# =====================================================================
# GENERALIZED THERMAL PARAMETERS (IP PROTECTED)
# =====================================================================
TEMPERATURE_POUR = 1500     # Molten alloy pouring temperature (Celsius)
TEMPERATURE_MOLD = 200     # Pre-heated mold ambient baseline (Celsius)
SOLIDUS_THRESHOLD = 1350    # Generalized alloy phase crystallization boundary (°C)

def simulate_casting_solidification():
    """Models thermal gradient paths over time for thick vs thin node elements."""
    time_steps = np.linspace(0, 60, 1000) # Tracking the critical first 60 seconds
    
    # 1. UNOPTIMIZED CONFIGURATION (Standard Uniform Mold Insulation)
    # Massive thermal lag between the thin flared boundaries and the thick central core axis
    temp_thin_unopt = TEMPERATURE_MOLD + (TEMPERATURE_POUR - TEMPERATURE_MOLD) * np.exp(-0.12 * time_steps)
    temp_core_unopt = TEMPERATURE_MOLD + (TEMPERATURE_POUR - TEMPERATURE_MOLD) * np.exp(-0.03 * time_steps)
    
    # 2. OPTIMIZED CONFIGURATION (Directional Solidification via Automated Chill-Plates)
    # Artificially boosting heat extraction rates at the thick core to align phase changes
    temp_thin_opt = TEMPERATURE_MOLD + (TEMPERATURE_POUR - TEMPERATURE_MOLD) * np.exp(-0.10 * time_steps)
    temp_core_opt = TEMPERATURE_MOLD + (TEMPERATURE_POUR - TEMPERATURE_MOLD) * np.exp(-0.09 * time_steps)
    
    plt.figure(figsize=(10, 5.5))
    
    # Plotting Unoptimized Data Profiles
    plt.plot(time_steps, temp_core_unopt, color='crimson', linestyle=':', 
             label='Unoptimized: Thick Core Element (Defect-Prone Segregation Zone)', linewidth=2)
    plt.plot(time_steps, temp_thin_unopt, color='red', alpha=0.35, 
             label='Unoptimized: Thin Flared End Boundary')
    
    # Plotting Optimized Chilled Framework Profiles
    plt.plot(time_steps, temp_core_opt, color='teal', 
             label='Optimized: Thick Core Interface (Controlled Thermal Sinks)', linewidth=2.5)
    plt.plot(time_steps, temp_thin_opt, color='darkgreen', linestyle='--', 
             label='Optimized: Thin Flared Boundary (Stabilized Heat Path)', linewidth=1.5)
    
    # Critical Structural Metallurgical Threshold
    plt.axhline(y=SOLIDUS_THRESHOLD, color='purple', alpha=0.5, linestyle='--', 
                label='Solidus Cross Horizon (~1350°C Crystallization)', linewidth=1.2)
    
    plt.title('Transient Thermal Solidification Profile Matrix: Node Geometry Model', fontsize=11, fontweight='bold')
    plt.xlabel('Time Elapsed Post-Pour (Seconds)')
    plt.ylabel('Material Temperature Modulus (°C)')
    plt.ylim(0, 1600)
    plt.grid(True, linestyle=':', alpha=0.5)
    plt.legend(loc='upper right')
    plt.show()

if __name__ == "__main__":
    # Execute casting solidification model when file is initialized directly
    simulate_casting_solidification()
