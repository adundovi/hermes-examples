from pyhermes import *

import numpy as np
import healpy
import matplotlib.pyplot as plt

nside = 128
skymap = DMSkymap(nside)
gas = YMW16()
integrator = DMIntegrator(gas)
integrator.setSunPosition(Vector3QLength(8.3*kiloparsec, 0*parsec, 0*parsec))

#mask = RectangularWindow(-5*deg, 5*deg, 40*deg, 95*deg)
#skymap.setMask(mask)

skymap.setIntegrator(integrator)
skymap.compute()

output = FITSOutput("!fits/dm-ymw16-skymap-nside{}.fits.gz".format(nside))
skymap.save(output)

healpy.visufunc.mollview(
#        np.log10(np.array(skymap)),
        skymap,
        title='DM of YMW16 log([pc/cm3])', cmap='magma')

plt.savefig('img/dm-ymw16-skymap-nside{}.png'.format(nside))
