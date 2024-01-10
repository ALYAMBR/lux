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
from lux.vis.VisList import VisList


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

    posbl_attrs = [c for c in ldf.columns if ldf.data_type[c] == "quantitative"]
    combinations = {f'{posbl_attrs[i1]}_x_{ldf.intent[i2].attribute}' : (posbl_attrs[i1], ldf.intent[i2].attribute) 
                    for i1 in range(len(posbl_attrs))
                    for i2 in range(len(ldf.intent))}
    
    for k, v in combinations.items():
        ldf[k] = ldf[v[0]] * ldf[v[1]]

    combinations_names = [k for k in combinations.keys()]

    vlist = VisList([lux.Clause('?')], source=ldf)
    vlist = vlist.showK()
    # vlist=ldf.current_vis

    recommendation["collection"] = vlist
    return recommendation