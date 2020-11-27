"""
################################################################
################# Φ-Net demonstration ##########################
#################  Visualize results  ##########################
################################################################

Created on Fri Oct 16 2020

This code visualizes phase and coherence estimated by using the Φ-Net
in comparison with a boxcar filter and the noisy data.


@authors: 
Giorgia Gobbi
Francescopaolo Sica*

*corresponding author
francescopaolo.sica@dlr.de

Microwaves and Radar Institute
German Aerospace Center (DLR)
Münchener Str. 20, 82234 Weßling


The present code is implemented on the basis of the paper:
F. Sica, G. Gobbi, P. Rizzoli and L. Bruzzone, 
"Φ-Net: Deep Residual Learning for InSAR Parameters Estimation," 
in IEEE Transactions on Geoscience and Remote Sensing, 
doi: 10.1109/TGRS.2020.3020427.

Please cite this paper as:
@ARTICLE{Sica2020,
  author={F. {Sica} and G. {Gobbi} and P. {Rizzoli} and L. {Bruzzone}},
  journal={IEEE Transactions on Geoscience and Remote Sensing}, 
  title={ϕ-Net: Deep Residual Learning for InSAR Parameters Estimation}, 
  year={2020},
  volume={},
  number={},
  pages={1-25},
  doi={10.1109/TGRS.2020.3020427}}

#################################################################
"""

import argparse
import sys
import os
import matplotlib.pyplot as plt
import numpy as np
from scipy import ndimage as ndi


def parse_args():
    parser = argparse.ArgumentParser(usage='Visualize results\n')
    #    ====================== INPUT DATA FOLDER ====================
    parser.add_argument('--noisy_dir', default='./data/', type=str, help='directory of test dataset')
    parser.add_argument('--result_dir', default='./result/', type=str, help='directory of results')

    return parser.parse_args()


def check_input_data(arguments):
    """
    Check if the passed arguments are valid for processing
    """
    if not os.path.exists(arguments.noisy_dir):
        print("Error: Input noisy data directory %s doesn't exists." % arguments.noisy_dir)
        sys.exit(1)

    if not os.path.exists(arguments.result_dir):
        print("Error: Input data directory %s doesn't exists." % arguments.result_dir)
        sys.exit(1)


if __name__ == '__main__':
    args = parse_args()
    check_input_data(args)

    master = np.load(os.path.join(args.noisy_dir, '/master.npy'))
    slave  = np.load(os.path.join(args.noisy_dir, '/slave.npy'))

    pha = np.load(os.path.join(args.result_dir, '/estimated_phase.npy'))
    coh = np.load(os.path.join(args.result_dir, '/estimated_coherence.npy'))

    intf = master * np.conj(slave)
    noisyPha = np.angle(intf)
    win = 5

    intf_box = ndi.uniform_filter(np.real(intf), size=win) + 1j * ndi.uniform_filter(np.imag(intf), size=win)

    phaBox = np.angle(intf_box)
    cohBox = np.abs(intf_box) / np.sqrt(ndi.uniform_filter(np.abs(master) ** 2, size=win)) / np.sqrt(
        ndi.uniform_filter(np.abs(slave) ** 2, size=win))
    noisyAmp = np.sqrt((np.abs(master) ** 2 + np.abs(slave) ** 2) / 2)

    plt.figure(figsize=(12, 8)),
    plt.subplot(231)
    plt.imshow(noisyPha, vmin=-np.pi, vmax=np.pi, cmap='jet'), plt.colorbar(), plt.title('Noisy phase')
    plt.subplot(234)
    plt.imshow(noisyAmp, vmin=0, vmax=2.5 * np.mean(noisyAmp), cmap='jet'), plt.colorbar(), plt.title('Noisy amplitude')
    plt.subplot(233)
    plt.imshow(phaBox, vmin=-np.pi, vmax=np.pi, cmap='jet'), plt.colorbar(), plt.title('Boxcar phase')
    plt.subplot(236)
    plt.imshow(pha, vmin=-np.pi, vmax=np.pi, cmap='jet'), plt.colorbar(), plt.title('Phi-Net phase')
    plt.subplot(232)
    plt.imshow(cohBox, vmin=0, vmax=1, cmap='jet'), plt.colorbar(), plt.title('Boxcar coherence')
    plt.subplot(235)
    plt.imshow(coh, vmin=0, vmax=1, cmap='jet'), plt.colorbar(), plt.title('Phi-Net coherence')
