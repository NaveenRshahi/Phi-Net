"""
################################################################
################# Φ-Net demonstration ##########################
################################################################

Created on Fri Oct 16 2020


This code is a demonstration about how to run the Φ-Net for the 
estimation of the interferometric phase and coherence.


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

import os
os.environ['CUDA_VISIBLE_DEVICES'] = "0"  # assign the GPU id to the processor
os.environ['TF_CPP_MIN_LOG_LEVEL'] = "2"  # INFO, WARNING messages are not printed (default is 0)

import sys
import argparse
import time
import numpy as np
stderr = sys.stderr
sys.stderr = open(os.devnull, 'w')
from keras.models import load_model
import PhiNet
sys.stderr = stderr


def parse_args():
    parser = argparse.ArgumentParser()
#    ====================== INPUT DATA FOLDER ====================
    parser.add_argument('--noisy_dir', default='./data/', type=str, help='directory of test dataset')
#    ====================== MODEL FOLDER ====================
    parser.add_argument('--model_dir', default='./trained_model/', type=str, help='directory of the model')
    parser.add_argument('--model_name', default='phi_net_model.hdf5', type=str, help='the model name')
#    ====================== OUTPUT DATA FOLDER ====================
    parser.add_argument('--result_dir', default='./result/', type=str, help='directory of results')

    return parser.parse_args()


if __name__ == '__main__':    
    
    
    args = parse_args()
    PhiNet.check_inputs(args)


    print('========= Load Phi-Net trained model ==========')
    model = load_model(os.path.join(args.model_dir, args.model_name),compile=False)
    
    print('============== Read input file ================')
    print('File: %s' % os.path.join(args.noisy_dir, 'master.npy'))
    master = np.load(os.path.join(args.noisy_dir,'master.npy'))
    print('File: %s' % os.path.join(args.noisy_dir, 'slave.npy'))
    slave = np.load(os.path.join(args.noisy_dir,'slave.npy'))
    
    print('================ Estimation ===================')
    start_time = time.time()
    x_phase, x_coh = PhiNet.inference(master,slave,model)
    elapsed_time = time.time() - start_time
    print('%10s : %2.4f second'%('time:',elapsed_time))
    
    print('================ Save output ==================')
    print('File: %s' % os.path.join(args.result_dir, 'estimated_phase.npy'))
    np.save(os.path.join(args.result_dir,'estimated_phase.npy'), x_phase)
    print('File: %s' % os.path.join(args.result_dir, 'estimated_coherence.npy'))
    np.save(os.path.join(args.result_dir,'estimated_coherence.npy'), x_coh)
    
    print('=================== DONE ======================')
    sys.exit(0)
