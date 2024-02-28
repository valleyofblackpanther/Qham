# qham/__init__.py


from .FHM.fhm import HubbardModel
from .HBM.hmb import HeisenbergModel
from .HBM.hmbq import create_heisenberg_circuit
from .HBM.hmbslq import SquareLattice
from .HBM.hmbsmlq import SquareLatticeMatrix
from .QHO.qho import QuantumHarmonicOscillator
from .TFIM.tfim import TFIMSimulation
from .TFIM.tfimq import create_tfim_circuit

__all__ = [
    "HubbardModel",
    "HeisenbergModel",
    "create_heisenberg_circuit",
    "SquareLattice",
    "SquareLatticeMatrix",
    "QuantumHarmonicOscillator",
    "TFIMSimulation",
    "create_tfim_circuit"
]

# Import subpackages
from . import FHM
from . import HBM
from . import QHO
from . import TFIM

# Now users can access, for example, qham.FHM.some_class_or_function


