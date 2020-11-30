.. image:: logo/phinet_logo_ext.PNG
   :width: 1px
   :alt: PhiNet logo
   :align: left

------------------------------------------------------------------------------

Summary
-------

Phi-Net is a novel deep learning methodology for the joint estimation of the 
Interferometric Synthetic Aperture Radar (InSAR) phase and coherence.

Phi-Net is trained using synthetic data obtained by an innovative strategy based
on the theoretical modeling of the physics behind the SAR acquisition principle. 
This strategy allows the network to generalize the estimation problem with respect
to: 

*(1) different noise levels, 

*(2) the nature of the imaged target on the ground, 

*(3) the interferometric acquisition geometry.

The code has been developed at the Microwaves and Radar Institute of the 
German Aerospace Center (DLR). Münchener Str. 20, 82234 Weßling.


Academic publications
---------------------

The present code is implemented on the basis of the paper:

* F\. Sica, G. Gobbi, P. Rizzoli and L. Bruzzone, *Φ-Net: Deep Residual Learning for InSAR Parameters Estimation*, in IEEE Transactions on Geoscience and Remote Sensing, doi: 10.1109/TGRS.2020.3020427.

If you use this code in your own research, please cite `our paper describing it <https://www.researchgate.net/publication/344692853_ph-Net_Deep_Residual_Learning_for_InSAR_Parameters_Estimation>`_.

BibTex
@ARTICLE{Sica2020,
  author={F. {Sica} and G. {Gobbi} and P. {Rizzoli} and L. {Bruzzone}},
  
  journal={IEEE Transactions on Geoscience and Remote Sensing}, 
  
  title={ϕ-Net: Deep Residual Learning for InSAR Parameters Estimation}, 
  
  year={2020},
  
  volume={},
  
  number={},
  
  pages={1-25},
  
  doi={10.1109/TGRS.2020.3020427}}


Authors
-------

* Giorgia Gobbi
* Francescopaolo Sica

HowTo
-----

Folders
````````

* `phinet/data </phinet/data>`_: input files `master.npy` and `slave.npy` SAR Single Look Complex.
* `phinet/trained_model </phinet/trained_model>`_: Phi-Net trained model `phi_net_model.hdf5`.
* `phinet/result </phinet/result>`_: output files `estimated_phase.npy` and `estimated_coherence.npy`.

Demo steps (for Linux distribution)
````````````````````````````````````

1) Create environment from `YAML`::

	conda env create --name phinet_env --file requirements.yml

2) Activate environment::

	source activate phinet_env

3) Launch test::

	python test_demo.py

4) Visualize results obtained from the test::

	python visualize_results.py


Dependencies
------------

The ``requirements.yml`` file lists all packages necessary to run the
``test_demo.py`` file in the ``phinet`` folder.

This package is developed under Python 3.7 with tensorflow 1.13.1. 

Acknowledgements 
----------------

The authors would like to acknowledge Philipp Posovsky and Andrea Pulella for their support in the set up of this repository.


License
-------

::

Copyright © 2020 Deutsches Zentrum für Lüft und Raumfahrt e.V.

Permission is hereby granted, free of charge, to any person obtaining a copy of this software
and associated documentation files (the “Software”), to deal in the Software without 
restriction, including without limitation the rights to use, copy, modify, merge, publish, 
distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the 
Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or 
substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING 
BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND 
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, 
DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING 
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


