#  Copyright 2023-2026 Nikita Radeev.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

import lux
from lux.vis.Vis import Vis


def combine(ldf):
    """
    Generates all possible combinations of numerical features.

    Parameters
    ----------
    ldf : lux.core.frame
            LuxDataFrame with underspecified intent.

    Returns
    -------
    recommendations : Dict[str,obj]
            object with a collecttion of visualizations that result from the Combine action.

    """
    # takes in a dataObject and generates a list of new dataObjects, each with
    # combination of two features
    # --> return list of dataObjects with corresponding interestingness scores





    recommendation = { 
        "action": "Combine",
        "description": f"Combine an attribute with other features.",
        "long description": f"Combine features via operations and show the most interesting ones."

    }



    # vlist = lux.vis.VisList.VisList(combinations, source=ldf)
    vlist=[]




    recommendation["collection"] = vlist
    return recommendation