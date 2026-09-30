"""```python
def prepare_notebook():
    ip = get_ipython()
    if ip is None: return
    from IPython.core.interactiveshell import InteractiveShell
    from array import array
    from pprint import pprint
    from wigglystuff import LiveEdit
    import operator
    from functools import partial 
    import matplotlib.pyplot as plt
    from collections import namedtuple
    import random, copy 
    import ctypes
    import sys
    from ipaddress import IPv4Address
    from typing import Sequence
    import numpy as np
    InteractiveShell.ast_node_interactivity = "all"
    ip.user_ns.update(
        array=array, 
        pprint=pprint, 
        LiveEdit=LiveEdit, 
        operator=operator, 
        partial=partial, 
        plt=plt,
        namedtuple=namedtuple,
        random=random,
        copy=copy,
        ctypes=ctypes,
        sys=sys,
        IPv4Address=IPv4Address,
        Sequence=Sequence,
        np=np
    )
```"""

__version__ = "0.0.1"
