import numpy as np
import matplotlib.pyplot as plt

# Simulate ground acceleration demand spectrum (Scaling from minor shake to cataclysmic M9.5 shock)
seismic_demand = np.linspace(0, 100, 500)

def simulate_all_sectors_strain():
    """
    Simulates mechanical core strain profiles and foundation rotation limits
    across all five diversified infrastructure archetypes.
    """
    # Initialize data dicts
    strains = {}
    rotations = {}

    # 1. High-Density Residential Towers
    # Uniform loading, shared mat base, flush beam-column joints
    strains['Residential Towers'] = (seismic_demand * 0.035) / 1 + 0.05 * np.sin(seismic_demand * 0.1)
    rotations['Residential Towers'] = (seismic_demand * 0.022) / 1.1

    # 2. Monolithic Sovereign Monument
    # Top-heavy asymmetric mass, aggressive wind/overturning interactions
    strains['Sovereign Monument'] = (seismic_demand * 0.028) + 0.0001 * (seismic_demand ** 2)
    rotations['Sovereign Monument'] = (seismic_demand * 0.038)  # Higher unmitigated tilting risk

    # 3. Commercial Open-Span Complex
    # Long spans, flexible frame, high inter-story drift susceptibility
    strains['Commercial Open-Span'] = (seismic_demand * 0.042)  # Higher structural drift demand
    rotations['Commercial Open-Span'] = (seismic_demand * 0.015)

    # 4. Integrated Municipal Hubs
    # Rigid base-isolation bounds, lower allowed internal deformations
    strains['Municipal Hubs'] = (seismic_demand * 0.012) + 0.005 * np.cos(seismic_demand * 0.2)
    rotations['Municipal Hubs'] = (seismic_demand * 0.008)

    # 5. Transportation Infrastructure
    # High dynamic cyclic loading, narrow single piers, bridge deck seats
    strains['Transit Infrastructure'] = (seismic_demand * 0.025) + 0.00015 * (seismic_demand ** 2)
    rotations['Transit Infrastructure'] = (seismic_demand * 0.029)

    return strains, rotations

strains, rotations = simulate_all_sectors_strain()

# =====================================================================
# TECHNICAL MULTI-ARCHETYPE STRAIN VISUALIZATION
# =====================================================================
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 11))
colors = ['#1F497D', '#C00000', '#7030A0', '#008080', '#E36C0A']
styles = ['-', '--', '-.', ':', '-']

# Chart 1: Microstructural Joint Core Strain Testing
for idx, (sector, strain_profile) in enumerate(strains.items()):
    ax1.plot(seismic_demand, strain_profile, label=f"Adaptive {sector}", color=colors[idx], linestyle=styles[idx], linewidth=2.5)

ax1.axhline(y=4.0, color='red', linestyle='--', alpha=0.6, label='Fe-SMA Superelastic Reversible Elasticity Limit (4.0% Strain Ceiling)')
ax1.set_title('Microstructural Joint Core Strain Responses Across Diversified Structural Archetypes', fontsize=12, fontweight='bold')
ax1.set_xlabel('Simulated Seismic Ground Motion Intensity Acceleration Demand (%)')
ax1.set_ylabel('Calculated Internal Core Strain ($\epsilon$) [%]')
ax1.set_ylim(0, 5.0)
ax1.grid(True, linestyle=':', alpha=0.5)
ax1.legend(loc='upper left')

# Chart 2: Dynamic Foundation Overturning Rotation Testing
for idx, (sector, rot_profile) in enumerate(rotations.items()):
    ax2.plot(seismic_demand, rot_profile, label=f"Flared Base: {sector}", color=colors[idx], linestyle=styles[idx], linewidth=2.5)

ax2.axhline(y=1.2, color='black', linestyle='--', alpha=0.5, label='Critical Foundation Rotation Hazard Limit (1.2° Code Cap)')
ax2.set_title('Dynamic Foundation Overturning Rotation Matrix under Asymmetric Torsional Shocks', fontsize=12, fontweight='bold')
ax2.set_xlabel('Simulated Seismic Ground Motion Intensity Acceleration Demand (%)')
ax2.set_ylabel('Calculated Foundation Tilt / Rotation Angle ($\theta$) [Degrees]')
ax2.set_ylim(0, 4.0)
ax2.grid(True, linestyle=':', alpha=0.5)
ax2.legend(loc='upper left')

plt.tight_layout()
plt.show()
