# Figures and Tables

## Introduction

![geometries](data/figures/modified_sections_aoa35.png)

**Figure:** Original and modified geometries of the snake section (oriented at a $35$-degree angle of attack).}{From left to right: (1) original profile, (2) profile with the front lip only, (3) profile with the back lip only, and (4) profile with no lips.

## Grid-independence study

### Section with both lips at $Re=2000$ and $AoA=30^o$

**Table:** Comparison of the mean and RMS of the drag and lift coefficients for a section with both lips at $Re=2000$ and $AoA=30^o$ obtained with different simulation setups. Statistics are computed between $50$ and $80$ non-dimensional time units of flow simulation. Relative differences with respect to the Base case are reported between parentheses.
| Case | $<C_D>$ | $rms(C_D)$ | $<C_L>$ | $rms(C_L)$ |
|:-|:-:|:-:|:-:|:-:|
| Base case | 0.960 | 0.967 | 1.524 | 1.564 |
| Finer in time | 0.960 | 0.967 | 1.524 | 1.564 |
| Finer in space | 0.967 (+0.7%) | 0.974 (+0.7%) | 1.537 (+0.9%) | 1.578 (+0.9%) |
| Coarser in space | 0.968 (+0.8%) | 0.976 (+0.9%) | 1.554 (+2.0%) | 1.593 (+1.9%) |
| Extended domain | 0.951 (-0.9%) | 0.958 (-0.9%) | 1.513 (-0.7%) | 1.553 (-0.7%) |
| Extended uniform region | 0.960 | 0.967 | 1.524 | 1.564 |
| Displaced body | 0.959 (-0.1%) | 0.966 (-0.1%) | 1.522 (-0.1%) | 1.562 (-0.1%) |
| Tighter iterative solvers | 0.960 | 0.967 | 1.524 | 1.564 |

![independence:surface_pressure_2k30](runs/independence/2k30/figures/surface_pressure_compare_dx_dt.png)

**Figure:** Comparison of the mean surface pressure on a section with both lips at $Re=2000$ and $AoA=30^o$ obtained with different simulation setups. The surface pressure is averaged in time between $50$ and $80$ non-dimensional time units of flow simulation.

| u | v | p |
|:-:|:-:|:-:|
| ![independence:u_profiles_2k30](runs/independence/2k30/figures/u_profiles_compare_dx_dt.png) | ![independence:v_profiles_2k30](runs/independence/2k30/figures/v_profiles_compare_dx_dt.png) | ![independence:p_profiles_2k30](runs/independence/2k30/figures/p_profiles_compare_dx_dt.png) |

**Figure:** Comparison of the mean vertical profiles of the pressure and velocity components in the near wake of a section with both lips at $Re=2000$ and $AoA=30^o$. We compare the profiles obtained with different simulation setups. Profiles are averaged in time between $50$ and $80$ non-dimensional time units of flow simulations.

### Section with both lips at $Re=2000$ and $AoA=35^o$

**Table:** Comparison of the mean and RMS of the drag and lift coefficients for a section with both lips at $Re=2000$ and $AoA=35^o$ obtained with different simulation setups. Statistics are computed between $50$ and $80$ non-dimensional time units of flow simulation. Relative differences with respect to the Base case are reported between parentheses.
| Case | $<C_D>$ | $rms(C_D)$ | $<C_L>$ | $rms(C_L)$ |
|:-|:-:|:-:|:-:|:-:|
| Base case | 1.179 | 1.185 | 1.892 | 1.936 |
| Finer in time | 1.142 (-3.1%) | 1.147 (-3.2%) | 1.789 (-5.4%) | 1.834 (-5.3%) |
| Finer in space | 1.121 (-4.9%) | 1.126 (-5.0%) | 1.731 (-8.5%) | 1.772 (-8.5%) |
| Coarser in space | 1.261 (+7.0%) | 1.269 (+7.1%) | 1.969 (+4.1%) | 2.026 (+4.6%) |
| Extended domain | 1.128 (-4.3%) | 1.133 (-4.4%) | 1.765 (-6.7%) | 1.808 (-6.6%) |
| Extended uniform region | 1.148 (-2.6%) | 1.153 (-2.7%) | 1.802 (-4.8%) | 1.846 (-4.6%) |
| Displaced body | 1.154 (-2.1%) | 1.159 (-2.2%) | 1.818 (-3.9%) | 1.862 (-3.8%) |
| Tighter iterative solvers | 1.178 (-0.1%) | 1.184 (-0.1%) | 1.891 (-0.1%) | 1.934 (-0.1%) |

![independence:force_coefficients_2k35](runs/independence/2k35/figures/force_coefficients_compare_dx_dt.png)

**Figure:** History of the drag and lift coefficients for a snake cross-section with both lips at $AoA=35^o$ and $Re=2000$. We compare the results obtained with the base-case setup to the results obtained on a finer spatial grid and using a smaller time-step size. For comparison, we also show the results from Krishnan et al. (2014).

![independence:surface_pressure_2k35](runs/independence/2k35/figures/surface_pressure_compare_dx_dt.png)

**Figure:** Comparison of the mean surface pressure on a section with both lips at $Re=2000$ and $AoA=35^o$ obtained with different simulation setups. The surface pressure is averaged in time between $50$ and $80$ non-dimensional time units of flow simulation.

| u | v | p |
|:-:|:-:|:-:|
| ![independence:u_profiles_2k35](runs/independence/2k35/figures/u_profiles_compare_dx_dt.png) | ![independence:v_profiles_2k35](runs/independence/2k35/figures/v_profiles_compare_dx_dt.png) | ![independence:p_profiles_2k35](runs/independence/2k35/figures/p_profiles_compare_dx_dt.png) |

**Figure:** Comparison of the mean vertical profiles of the pressure and velocity components in the near wake of a section with both lips at $Re=2000$ and $AoA=35^o$. We compare the profiles obtained with different simulation setups. Profiles are averaged in time between $50$ and $80$ non-dimensional time units of flow simulations.

### Section with no lips at $Re=2000$ and $AoA=35^o$

**Table:** Comparison of the mean and RMS of the drag and lift coefficients for a section with no lips at $Re=2000$ and $AoA=35^o$ obtained with different simulation setups. Statistics are computed between $50$ and $80$ non-dimensional time units of flow simulation. Relative differences with respect to the base case are reported between parentheses.
| Case | $<C_D>$ | $rms(C_D)$ | $<C_L>$ | $rms(C_L)$ |
|:-|:-:|:-:|:-:|:-:|
| Base case | 0.885 | 0.892 | 1.085 | 1.180 |
| Finer in time | 0.884 (-0.1%) | 0.891 (-0.1%) | 1.084 (-0.1%) | 1.179 (-0.1%) |
| Finer in space | 0.886 (+0.1%) | 0.893 (+0.1%) | 1.102 (+1.6%) | 1.194 (+1.2%) |
| Coarser in space | 0.842 (-4.9%) | 0.849 (-4.8%) | 1.054 (-2.9%) | 1.146 (-2.9%) |
| Extended domain | 0.872 (-1.5%) | 0.879 (-1.5%) | 1.071 (-1.3%) | 1.164 (-1.4%) |
| Extended uniform region | 0.885 | 0.892 | 1.085 | 1.180 |

![independence:surface_pressure_2k35_none](runs/independence/2k35-nolips/figures/surface_pressure_compare_dx_dt.png)

**Figure:** Comparison of the mean surface pressure on a section with no lips at $Re=2000$ and $AoA=35^o$ obtained with different simulation setups. The surface pressure is averaged in time between $50$ and $80$ non-dimensional time units of flow simulation.

| u | v | p |
|:-:|:-:|:-:|
| ![independence:u_profiles_2k35_none](runs/independence/2k35-nolips/figures/u_profiles_compare_dx_dt.png) | ![independence:v_profiles_2k35_none](runs/independence/2k35-nolips/figures/v_profiles_compare_dx_dt.png) | ![independence:p_profiles_2k35_none](runs/independence/2k35-nolips/figures/p_profiles_compare_dx_dt.png) |

**Figure:** Comparison of the mean vertical profiles of the pressure and velocity components in the near wake of a section with no lips at $Re=2000$ and $AoA=35^o$. We compare the profiles obtained with different simulation setups. Profiles are averaged in time between $50$ and $80$ non-dimensional time units of flow simulations.

## Results

### Mean force coefficients

|  |  |
|:-:|:-:|
| ![cl_re1000](runs/Re1000/figures/avg_lift_coefficients_vs_aoa.png) | ![cl_re2000](runs/Re2000/figures/avg_lift_coefficients_vs_aoa.png) |
| ![cd_re1000](runs/Re1000/figures/avg_drag_coefficients_vs_aoa.png) | ![cd_re2000](runs/Re2000/figures/avg_drag_coefficients_vs_aoa.png) |

**Figure:** Time-averaged drag (top) and lift (bottom) coefficients at Reynolds numbers $1000$ and $2000$ versus the angle of attack on all four sections. All averages are computed between $50$ and $80$ non-dimensional time units of flow simulation.

|  |  |
|:-:|:-:|
| ![ld_re1000](runs/Re1000/figures/avg_lift_drag_ratio_vs_aoa.png) | ![ld_re2000](runs/Re2000/figures/avg_lift_drag_ratio_vs_aoa.png) |

**Figure:** Time-averaged lift-to-drag ratio at Reynolds numbers $1000$ and $2000$ versus the angle of attack on all four sections. All averages are computed between $50$ and $80$ non-dimensional time units of flow simulation.

### $Re=1000$ and $AoA=35^o$

![surface_pressure_1k35](runs/Re1000/figures/surface_pressure_1k35.png)

**Figure:** Mean surface pressure on all four sections at $Re=1000$ and $AoA=35^o$. The surface pressure is averaged in time between $50$ and $80$ non-dimensional time units of flow simulation.

|  |  |
|:-:|:-:|
| ![wz_1k35_both](runs/Re1000/both_lips/1k35/figures/vorticity_0160000.png) | ![wz_1k35_front](runs/Re1000/front_lip/1k35/figures/vorticity_0180000.png) |
| ![wz_1k35_back](runs/Re1000/back_lip/1k35/figures/vorticity_0165000.png) | ![wz_1k35_none](runs/Re1000/no_lips/1k35/figures/vorticity_0145000.png) |

**Figure:** Filled contour of the vorticity field ($-5 \le \omega_z \le 5$) at $Re=1000$ and $AoA=35^o$ for all section: (a) with both lips, (b) no back lip, (c) no front lips, and (d) no lips. Snapshots correspond to instants where the lift force acting on the sections is near minimum.

![wz_1k25_back](runs/Re1000/back_lip/1k25/figures/vorticity_0180000.png)

**Figure:** Filled contour of the vorticity field ($-5 \le \omega_z \le 5$) at $Re=1000$ for a section with the back lip only at $AoA=25^o$. Snapshot corresponds to an instant where the lift force acting on the section is near minimum.

|  |  |
|:-:|:-:|
| ![u_profiles_1k35](runs/Re1000/figures/u_profiles_1k35.png) | ![v_profiles_1k35](runs/Re1000/figures/v_profiles_1k35.png) |

**Figure:** Time-averaged vertical profiles of the velocity components in the near wake of the body. Comparing the four cross-sections at a 35-degree angle of attack at Reynolds number 1000.

### $Re=2000$ and $AoA=35^o$

![surface_pressure_2k35](runs/Re2000/figures/surface_pressure_2k35.png)

**Figure:** Mean surface pressure on all four sections at $Re=2000$ and $AoA=35^o$. The surface pressure is averaged in time between $50$ and $80$ non-dimensional time units of flow simulation.

|  |  |
|:-:|:-:|
| ![wz_2k35_both](runs/Re2000/both_lips/2k35/figures/vorticity_0165000.png) | ![wz_2k35_front](runs/Re2000/front_lip/2k35/figures/vorticity_0192500.png) |
| ![wz_2k35_back](runs/Re2000/back_lip/2k35/figures/vorticity_0130000.png) | ![wz_2k35_none](runs/Re2000/no_lips/2k35/figures/vorticity_0172500.png) |

**Figure:** Filled contour of the vorticity field ($-5 \le \omega_z \le 5$) at $Re=2000$ and $AoA=35^o$ for all section: (a) with both lips, (b) no back lip, (c) no front lips, and (d) no lips. Snapshots correspond to instants where the lift force acting on the sections is near minimum.

|  |  |
|:-:|:-:|
| ![u_profiles_2k35](runs/Re2000/figures/u_profiles_2k35.png) | ![v_profiles_2k35](runs/Re2000/figures/v_profiles_2k35.png) |

**Figure:** Time-averaged vertical profiles of the velocity components in the near wake of the body. Comparing the four cross-sections at a 35-degree angle of attack at Reynolds number 2000.

### $Re=2000$ and $AoA=25^o$

![surface_pressure_2k25](runs/Re2000/figures/surface_pressure_2k25.png)

**Figure:** Mean surface pressure on all four sections at $Re=2000$ and $AoA=25^o$. The surface pressure is averaged in time between $50$ and $80$ non-dimensional time units of flow simulation.

|  |  |
|:-:|:-:|
| ![wz_2k25_both](runs/Re2000/both_lips/2k25/figures/vorticity_0180000.png) | ![wz_2k25_front](runs/Re2000/front_lip/2k25/figures/vorticity_0150000.png) |
| ![wz_2k25_back](runs/Re2000/back_lip/2k25/figures/vorticity_0180000.png) | ![wz_2k25_none](runs/Re2000/no_lips/2k25/figures/vorticity_0160000.png) |

**Figure:** Filled contour of the vorticity field ($-5 \le \omega_z \le 5$) at $Re=2000$ and $AoA=25^o$ for all section: (a) with both lips, (b) no back lip, (c) no front lips, and (d) no lips. Snapshots correspond to instants where the lift force acting on the sections is near minimum.

|  |  |
|:-:|:-:|
| ![u_profiles_2k25](runs/Re2000/figures/u_profiles_2k25.png) | ![v_profiles_2k25](runs/Re2000/figures/v_profiles_2k25.png) |

**Figure:** Time-averaged vertical profiles of the velocity components in the near wake of the body. Comparing the four cross-sections at a 25-degree angle of attack at Reynolds number 2000.

### Other

|  |  |
|:-:|:-:|
| ![](runs/Re2000/both_lips/figures/surface_pressure.png) | ![](runs/Re2000/front_lip/figures/surface_pressure.png) |
| ![](runs/Re2000/back_lip/figures/surface_pressure.png) | ![](runs/Re2000/no_lips/figures/surface_pressure.png) |

**Figure:** Time-averaged surface pressure profiles at Reynolds number 2000 for the section with both lips (top left), with only the front lip (top right) or the back lip (bottom left), and with no lip (bottom right).
