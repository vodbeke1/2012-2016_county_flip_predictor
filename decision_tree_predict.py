import numpy as np
import math

 

def format_to_dict(x):

    """Format from numpy array to f-dictionary

    Parameters
    ----------
    x : np.array or list
        array with ordered values

    Output : dictionary
        dictionary with order labeled values
    """

    f_dict = dict()

    for i in range(len(x)):
        f_dict['f'+str(i)] = x[i]

    return f_dict

 

def node_decision(node, x):

    """Get split condition and parameters

    Return state/decision

    """

    split = node['split']
    split_condition = node['split_condition']

    if x[split] < split_condition or np.isnan(x[split]):
        return 0
    else:
        return 1

 

def score_transform(x):

    """Transformation of score to probability

    Apply scklearn probability transformation
    Formula: 1 - (1/(1 + e^score))

    Parameters
    ----------
    x : float
        pre-transform score

    Output : float
        post-transform score

    """

    denom = (1 + math.exp(x))

    return round((1-(1/denom)), 8)





def predict(x, model_parameters, tree_limit, base_score=0, format_to_dictionary=True, transform_score=True):

    """Function for prediction of model

    Parameters
    ----------
    x : dictionary
        dictionary with {variable label : variable value}

    model_parameter : list
        list of nodes with conditions and values and leafs with value

    tree_limit : int
        which tree to stop on
    -----------
    Output : float
        float containing probability score

    """

    if format_to_dictionary:
        x = format_to_dict(x)

    val = base_score
    

    for i in range(len(model_parameters)):
        if i == tree_limit:
            break

        state = None
        node = model_parameters[i]

        trigger = True

        while trigger:
            state = node_decision(node, x)
            node = node['children'][state]

            if 'children' not in node.keys():
                break

        val += node['leaf']
    
    if transform_score:
        return score_transform(val)
    return val