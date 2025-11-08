
__license__ = "Apache-2.0"
__version__ = "0.1.0"
__maintainer__ = "Mihir Deo"

from typing import List, Dict, Any, Tuple, Union, Set
from collections import defaultdict, deque


"""
A graph is represented as AdjacentList, AdjacentMatrix, AdjacentSet
"""

# For non-weighted graph
AdjacentList = Dict[Union[str,int],List[Union[str,int]]] # {1:[2,3,4]...}
AdjacentMatrix = List[List[int]] # With 1 or 0 to represent the connection
AdjacentSet = Set[Tuple[Union[str,int]]] # {(1,3),(1,4),(3,4)...}

# For weighted graph
AdjacentList = Dict[Union[int,str],Dict[Union[int,str],int]] # {A:{B:5,C:4..}, B:{A:3,D:1} ..} For A -> B weight is 5 etc.
AdjacentMatrix = List[List[int]] # With value representing weight of between points