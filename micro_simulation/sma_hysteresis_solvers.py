"""
Micro-Simulation Framework: Shape Memory Alloy Hysteresis & Fatigue Solvers
Project: Biomimetic Seismic Skeleton Optimization
License: MIT License

Disclaimer: This is a generalized phenomenological reference model for 
educational and validation visualization. Exact industrial manufacturing 
constants are proprietary and omitted.
"""

import numpy as np
import matplotlib.pyplot as plt

# =====================================================================
# GENERALIZED MATERIAL PARAMETERS (IP PROTECTED MODULI)
# =====================================================================
E_AUSTENITE = 1300          # Abstract Elastic Modulus factor
PLATEAU_YIELD = 455         # Normalized transformation stress trigger (MPa)
PLATEAU_SLOPE = 190         # Generalized post-yield hardening tangent
FATIGUE_RATE = 0.03         # Normalized asymptotic degradation coefficient
MAX_RESIDUAL_DRIFT = 0.60   # Capped baseline for maximum residual strain accumulation

def compute_single_cycle(strain_array, cycle_number):
    """
    Computes continuous, non-discontinuous loading and unloading paths 
    for a Shape Memory Alloy undergoing pseudoelastic phase transitions.
    """
    # Asymptotic tracking of functional fatigue decay over cycles
    degradation_factor = (1 - np.exp(-FATIGUE_RATE * cycle_number))
    loss_plateau = 70 * degradation_factor
    residual_strain = MAX_RESIDUAL_DRIFT * degradation_factor
    
    stress_loading = []
    stress_unloading = []
    
    for eps in strain_array:
        # Loading Path (Austenite -> Martensite)
        if eps < 0.35:
            load = eps * E_AUSTENITE
        else:
            load = (PLATEAU_YIELD - loss_plateau) + (eps - 0.35) * PLATEAU_SLOPE
            
        # Unloading Path (Martensite -> Austenite)
        if eps > 2.0:
            unload = (300 - loss_plateau * 0.5) + (eps - 2.0) * 82
        elif eps > residual_strain:
            unload = 50 + (eps - residual_strain) * 131
        else:
            unload = eps * (50 / max(0.01, residual_strain))
            
        stress_loading.append(load)
        stress_unloading.append(min(unload, load)) # Enforce numerical boundaries
        
    return np.array(stress_loading), np.array(stress_unloading)

def run_fatigue_simulation():
    """Generates and plots multi-cycle structural lifespan validation profiles."""
    strain_range = np.linspace(0, 5.5, 1000) # Maximum design deformation %
    
    # Track critical operational lifecycle milestones
    cycles_to_test = [1, 20, 100]
    colors = {1: 'teal', 20: 'darkorange', 100: 'crimson'}
    styles = {1: '-', 20: '--', 100: ':'}
    
    plt.figure(figsize=(10, 6))
    
    for c in cycles_to_test:
        loading, unloading = compute_single_cycle(strain_range, c)
        
        # Plot loading curve
        plt.plot(strain_range, loading, color=colors[c], 
                 label=f'Cycle {c} Performance Horizon', linewidth=2)
        # Plot unloading curve
        plt.plot(strain_range, unloading, color=colors[c], linestyle='--', linewidth=1.5)
        
    plt.title('Reference Material Profile: Multi-Cycle Fatigue Track (Generalized Framework)', fontsize=11, fontweight='bold')
    plt.xlabel('Strain / Structural Deformation (%)')
    plt.ylabel('Internal Stress Proxy (MPa)')
    plt.grid(True, linestyle=':', alpha=0.6)
    plt.legend(loc='upper left')
    plt.show()

if __name__ == "__main__":
    # Execute visualization run when file is executed directly
    run_fatigue_simulation()
