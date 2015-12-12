class CxConstants(object):
    """ This is to hold constants relevant for CX data.
    """

    META_DATA = 'metaData'
    NUMBER_VERIFICATION = 'numberVerification'
    NUMBER_VERIFICATION_VALUE = 281474976710655
    STATUS = 'status'
    NODES = 'nodes'
    EDGES = 'edges'
    CARTESIAN_LAYOUT = 'cartesianLayout'
    EDGE_ATTRIBUTES = 'edgeAttributes'
    NODE_ATTRIBUTES = 'nodeAttributes'
    NETWORK_ATTRIBUTES = 'networkAttributes'
    HIDDEN_ATTRIBUTES = 'hiddenAttributes'
    VISUAL_PROPERTIES = 'visualProperties'
    SUB_NETWORKS = 'subNetworks'
    NETWORK_RELATIONS = 'networkRelations'
    DATA_TYPE_BOOLEAN = "boolean"
    DATA_TYPE_DOUBLE = "double"
    DATA_TYPE_FLOAT = "float"
    DATA_TYPE_INTEGER = "integer"
    DATA_TYPE_LONG = "long"
    DATA_TYPE_SHORT = "short"
    DATA_TYPE_STRING = "string"
    DATA_TYPE_LIST_OF_BOOLEAN = "list_of_boolean"
    DATA_TYPE_LIST_OF_DOUBLE = "list_of_double"
    DATA_TYPE_LIST_OF_FLOAT = "list_of_float"
    DATA_TYPE_LIST_OF_INTEGER = "list_of_integer"
    DATA_TYPE_LIST_OF_LONG = "list_of_long"
    DATA_TYPE_LIST_OF_SHORT = "list_of_short"
    DATA_TYPE_LIST_OF_STRING = "list_of_string"

    SINGLE_ATTRIBUTE_TYPES = frozenset([
        DATA_TYPE_BOOLEAN,
        DATA_TYPE_DOUBLE,
        DATA_TYPE_FLOAT,
        DATA_TYPE_INTEGER,
        DATA_TYPE_LONG,
        DATA_TYPE_SHORT,
        DATA_TYPE_STRING])

    LIST_ATTRIBUTE_TYPES = frozenset([
        DATA_TYPE_LIST_OF_BOOLEAN,
        DATA_TYPE_LIST_OF_DOUBLE,
        DATA_TYPE_LIST_OF_FLOAT,
        DATA_TYPE_LIST_OF_INTEGER,
        DATA_TYPE_LIST_OF_LONG,
        DATA_TYPE_LIST_OF_SHORT,
        DATA_TYPE_LIST_OF_STRING])
