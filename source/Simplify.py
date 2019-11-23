import RunMaxima

# Given an expression in Maxima syntax, apply
# maximas expand command to it.
#
# @param[in]    expression     The expression
#
# return                       The expanded expression as a string.
def expandExpression(expression):
    try:
        # Run the maxima as a subprocess.
        output = RunMaxima.runMaximaCode([f'expand({expression});'])
        # An error has occured if the length of the output is zero.
        if len(output) == 0:
            # Raise exception.
            raise Exception('Unexpected error occured in expandExpression.\nPlease check your input.')
        # Return the expanded expression.
        return output[0]
    except Exception as e:
        raise e
