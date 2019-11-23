import RunMaxima

# Given a list of equations in Maxima syntax and a list of variables,
# using Maximas solve command solve the corresponding system of equations.
#
# @param[in]    equations   List of equations given as strings.
# @param[in]    variables   List of variables given as strings.
#
# returns
def solveSystemOfEquations(equations, variables):
    try:
        # Create a string containing the equations and the variables.
        maximaInput = 'solve(['
        for i in range(len(equations)):
            if i > 0:
                maximaInput += ','
            maximaInput += str(equations[i])
        maximaInput += '],['
        for i in range(len(variables)):
            if i > 0:
                maximaInput += ','
            maximaInput += str(variables[i])
        maximaInput += ']);'
        # Run the maxima code.
        solution = RunMaxima.runMaximaCode([maximaInput])
        # If the length of solution is 0 an erro must have occured
        # in maxima.
        if len(solution) == 0:
            raise Exception('Unexpected error occured in solveSystemOfEquations.\nPlease check your input.')
        # Return the solution.
        return solution[0]
    except Exception as e:
        raise e
