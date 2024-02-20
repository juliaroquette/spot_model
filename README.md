This repository includes the spot model (spot_model.ipynb) I used in [Roquette et al. (2020)](https://ui.adsabs.harvard.edu/abs/2020A%26A...640A.128R/abstract) for looking at typical amplitudes produced by spot variability in YSOs.

This spot-model for YSOs considering the formulation from [Bouvier et al. 1993](ttps://ui.adsabs.harvard.edu/abs/1993A%26A...272..176B/abstract)

$$\Delta m=-2.5\log{\Bigg(1-\frac{f}{1-\frac{\mu}{3}}\Bigg[1-\frac{B_\lambda(T_\mathrm{spot})}{B_\lambda(T_*)}\Bigg]\Bigg)}$$

where:
- $m$ is the magnitude at a filter with an effective wavelength $\lambda$.
- $B_\lambda(T)$ are the value of a Planck-curve for a Black-Body for temperature $T$ at a wavelength $\lambda$.
- $T_{spot}$ and $T_{*}$ are the spot and stellar temperature respectively. 
- $f$ is the fraction of coverage by spots. 
- $\mu$ is the limb darkening coefficient for that filter

The Limb-darkening values in `LimbDarkeningClaret&Blomen_2011.fit` are linear limb-darkening coefficients from [Claret & Bloemen 2011](https://ui.adsabs.harvard.edu/abs/2011A%26A...529A..75C/abstract).

Photometric bands' effective wavelengths are from [SVO-database](http://svo2.cab.inta-csic.es/svo/theory/fps/index.php?mode=browse&gname=Generic&gname2=Johnson_UBVRIJHKL&asttype=)

Typical Spot temperatures for YSOs (`Venuti15_spot_parameters.csv`) are from [Venuti et al. 2015](https://ui.adsabs.harvard.edu/abs/2015A%26A...581A..66V/abstract).

**@juliaroquette 20 February 2024:** Feel free to use it, but please acknowledge the appropriate references mentioned here. 
