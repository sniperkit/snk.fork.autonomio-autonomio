def get_method_with_string(method_name, mode):

    '''
    Utility function that helps calling methods/functions
    within Keras dynamically using strings.

    method = a string value with the method name

    mode = 'layers', 'activations', and 'optimizers'. Note
           that the method needs to be included within the
           selected mode.
    '''

    if mode is 'layers':
        from keras.layers import *
    if mode is 'activations':
        from keras.activations import *
    if mode is 'optimizers':
        from keras.optimizers import *


def _get_method(method_name):

    possibles = globals().copy()
    possibles.update(locals())
    method = possibles.get(method_name)

    return method
