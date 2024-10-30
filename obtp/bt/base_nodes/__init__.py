from obtp.bt.base_nodes.Action import Action
from obtp.bt.base_nodes.Condition import Condition
from obtp.bt.base_nodes.Inverter import Inverter
from obtp.bt.base_nodes.Fallback import Fallback
from obtp.bt.base_nodes.Sequence import Sequence
from obtp.bt.base_nodes.CompositeAction import CompositeAction
from obtp.bt.base_nodes.CompositeCondition import CompositeCondition


base_node_map = {
    "act": Action,
    "action": Action,
    "composite_action": Action,

    "cond": Condition,
    "condition": Condition,
}

base_node_type_map={
    "Action": 'Action',
    "act": 'Action',
    "action": 'Action',
    "composite_action": 'Action',
    "sub": 'Action',
    "subtree": 'Action',

    "Condition": "Condition",
    "cond": "Condition",
    "condition": "Condition",
}

control_node_map = {
    "not": Inverter,
    "selector": Fallback,
    "fallback": Fallback,
    "sequence": Sequence
}


composite_node_map = {

    "act": CompositeAction,
    "action": CompositeAction,
    "composite_action": CompositeAction,
    "sub": CompositeAction,
    "subtree": CompositeAction,


    "cond" : CompositeCondition,
    "condition" : CompositeCondition,
    "composite_condition" : CompositeCondition,
}