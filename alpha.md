# Figures and Tables

## Introduction

![](data/figures/modified_sections_aoa35.pdf)

**Figure:** Modified profiles of the snake during the gliding phase. From left to right: (1) original profile, (2) with the back lip, (3) missing the front lip, and (4) missing both lips.

## Grid-independence study

**Table:** Mean and RMS of the drag and lift coefficient for a snake cross-section with both lips and $AoA = 30^o$ at $Re = 2000$. Statistics are computed between 50 and 80 non-dimensional time units of flow simulation.
| Case | <C_D> | rms(C_D) | <C_L> | rms(C_L) |
|:-|:-:|:-:|:-:|:-:|
| Base | 0.960 | 0.967 | 1.524 | 1.564 |
| Coarser in Space | 0.968 (+0.89 %) | 0.976 (+0.94 %) | 1.554 (+1.95 %) | 1.593 (+1.83 %) |
| Finer in Space | 0.967 (+0.73 %) | 0.974 (+0.77 %) | 1.537 (+0.86 %) | 1.578 (+0.88 %) |
| Finer in Time | 0.960 (+0.02 %) | 0.967 (+0.02 %) | 1.524 | 1.564 |
| Larger Domain | 0.951 (-0.89 %) | 0.958 (-0.89 %) | 1.513 (-0.74 %) | 1.553 (-0.71 %) |
| Larger Uniform Area | 0.960 (+0.01 %) | 0.967 (+0.01 %) | 1.524 (+0.01 %) | 1.564 (+0.01 %) |
| Shifted Markers | 0.959 (-0.08 %) | 0.966 (-0.08 %) | 1.522 (-0.14 %) | 1.562 (-0.13 %) |
| Tighter Iterative Solvers ($atol = 10^{-9}$) | 0.960 | 0.967 | 1.524 | 1.564 |

---

| p | u | v |
|:-:|:-:|:-:|
| ![](runs/independence/2k30/figures/p_profiles_compare_dx_dt.png) | ![](runs/independence/2k30/figures/u_profiles_compare_dx_dt.png) | ![](runs/independence/2k30/figures/v_profiles_compare_dx_dt.png) |

---

**Table:** Mean and RMS of the drag and lift coefficient for a snake cross-section with both lips and $AoA = 35^o$ at $Re = 2000$. Statistics are computed between 50 and 80 non-dimensional time units of flow simulation.
| Case | <C_D> | rms(C_D) | <C_L> | rms(C_L) |
|:-|:-:|:-:|:-:|:-:|
| Base | 1.179 | 1.185 | 1.892 | 1.936 |
| Coarser in Space | 1.261 (+6.96 %) | 1.269 (+7.02 %) | 1.969 (+4.04 %) | 2.026 (+4.68 %) |
| Finer in Space | 1.121 (-4.90 %) | 1.126 (-4.97 %) | 1.731 (-8.54 %) | 1.772 (-8.46 %) |
| Finer in Time | 1.142 (-3.14 %) | 1.147 (-3.22 %) | 1.789 (-5.46 %) | 1.834 (-5.26 %) |
| Larger Domain | 1.128 (-4.37 %) | 1.133 (-4.46 %) | 1.765 (-6.75 %) | 1.808 (-6.60 %) |
| Larger Uniform Area | 1.148 (-2.61 %) | 1.153 (-2.69 %) | 1.802 (-4.80 %) | 1.846 (-4.66 %) |
| Shifted Markers | 1.154 (-2.16 %) | 1.159 (-2.22 %) | 1.818 (-3.95 %) | 1.862 (-3.80 %) |
| Tighter Iterative Solvers ($atol = 10^{-9}$) | 1.178 (-0.08 %) | 1.184 (-0.08 %) | 1.891 (-0.07 %) | 1.934 (-0.07 %) |

---

| p | u | v |
|:-:|:-:|:-:|
| ![](runs/independence/2k35/figures/p_profiles_compare_dx_dt.png) | ![](runs/independence/2k35/figures/u_profiles_compare_dx_dt.png) | ![](runs/independence/2k35/figures/v_profiles_compare_dx_dt.png) |

---

**Table:** Mean and RMS of the drag and lift coefficient for a snake cross-section with no lips and $AoA = 35^o$ at $Re = 2000$. Statistics are computed between 50 and 80 non-dimensional time units of flow simulation.
| Case | <C_D> | rms(C_D) | <C_L> | rms(C_L) |
|:-|:-:|:-:|:-:|:-:|
| Base | 0.885 | 0.892 | 1.085 | 1.180 |
| Coarser in Space | 0.842 (-4.88 %) | 0.849 (-4.84 %) | 1.054 (-2.88 %) | 1.146 (-2.90 %) |
| Finer in Space | 0.886 (+0.05 %) | 0.893 (+0.03 %) | 1.102 (+1.52 %) | 1.194 (+1.16 %) |
| Finer in Time | 0.884 (-0.13 %) | 0.891 (-0.14 %) | 1.084 (-0.11 %) | 1.179 (-0.11 %) |
| Larger Domain | 0.872 (-1.46 %) | 0.879 (-1.45 %) | 1.071 (-1.33 %) | 1.164 (-1.33 %) |
| Larger Uniform Area | 0.885 (-0.01 %) | 0.892 (-0.01 %) | 1.085 (-0.03 %) | 1.180 (-0.03 %) |

---

| p | u | v |
|:-:|:-:|:-:|
| ![](runs/independence/2k35-nolips/figures/p_profiles_compare_dx_dt.png) | ![](runs/independence/2k35-nolips/figures/u_profiles_compare_dx_dt.png) | ![](runs/independence/2k35-nolips/figures/v_profiles_compare_dx_dt.png) |

---

## Main

|  |  |
|:-:|:-:|
| ![](runs/Re1000/figures/avg_drag_coefficients_vs_aoa.png) | ![](runs/Re2000/figures/avg_drag_coefficients_vs_aoa.png) |
| ![](runs/Re1000/figures/avg_lift_coefficients_vs_aoa.png) | ![](runs/Re2000/figures/avg_lift_coefficients_vs_aoa.png) |

**Figure:** Time-averaged drag (top) and lift (bottom) coefficients at Reynolds numbers $1000$ and $2000$ versus the angle of attack of a snake cross-section with both lips, only the front lip or the back lip, and no lips. All averages are computed between 50 and 80 non-dimensional time units of flow simulation.

---

|  |  |
|:-:|:-:|
| ![](runs/Re1000/figures/avg_lift_drag_ratio_vs_aoa.png) | ![](runs/Re2000/figures/avg_lift_drag_ratio_vs_aoa.png) |

**Figure:** Time-averaged lift-to-drag ratio at Reynolds numbers $1000$ and $2000$ versus the angle of attack of a snake cross-section with both lips, only the front lip or the back lip, and no lips. All averages are computed between 50 and 80 non-dimensional time units of flow simulation.

---

| p | u | v |
|:-:|:-:|:-:|
| ![](runs/Re2000/figures/p_profiles_2k35.png) | ![](runs/Re2000/figures/u_profiles_2k35.png) | ![](runs/Re2000/figures/v_profiles_2k35.png) |

**Figure:** Time-averaged vertical profiles of the pressure and velocity components in the near wake of the body. Comparing the four cross-sections at a 35-degree angle of attack at Reynolds number 2000.

---

![](runs/Re2000/figures/surface_pressure_2k35.png)

**Figure:** Time-averaged pressure along the surface for the four cross-sections with a 35-degree angle of attack and at Reynolds number 2000.

---

|  |  |
|:-:|:-:|
| ![](runs/Re2000/both_lips/figures/surface_pressure.png) | ![](runs/Re2000/front_lip/figures/surface_pressure.png) |
| ![](runs/Re2000/back_lip/figures/surface_pressure.png) | ![](runs/Re2000/no_lips/figures/surface_pressure.png) |

**Figure:** Time-averaged surface pressure profiles at Reynolds number 2000 for the section with both lips (top left), with only the front lip (top right) or the back lip (bottom left), and with no lip (bottom right).

---

|  |  |
|:-:|:-:|
| ![](runs/Re2000/both_lips/2k35/figures/vorticity.gif) | ![](runs/Re2000/front_lip/2k35/figures/vorticity.gif) |
| ![](runs/Re2000/back_lip/2k35/figures/vorticity.gif) | ![](runs/Re2000/no_lips/2k35/figures/vorticity.gif) |

**Figure:** Filled contours of the vorticity field at every non-dimensional time unit of flow simulation for a cross-section with a 35-degree angle of attack and at Reynolds number 2000. Top left: both lips; top right: front lip; bottom left: back lip; bottom right: no lips.
