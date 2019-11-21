import subprocess

# Module for running maxima as a subprocess while running Python.
# Use runMaximaCode or runMaximaFile, as they are intended to be the main
# API. Their output is a list of strings that represent every output
# of the maxima program (only the expressions).

cmd = ['C:/maxima-5.43.0/bin/maxima.bat']

# Runs a maxima code, and returns the output,
# if no error occurs.
#
# @param[in]	maximaCode		The maxima code that we run as a string.
#
# return                        List containing all the lines from the output.
def runMaxima(maximaCode):
	try:
		# TODO: What is a good buffer size?
		# Start the maxima as a subprocess.
		process = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		# Run the maxima code. Note that communicate requires the input as bytes.
		output = process.communicate(maximaCode.encode())
		# Check whether there are any errors written in stderr.
		if len(output[1]) > 0:
			# There are errors, so we want to report them. Note that
			# output[1] is in bytes, so we have to decode them to get a string.
			raise Exception(output[1].decode())
		else:
			# No errors, so decode the bytes obtained into a string and split it.
			return output[0].decode().split('\n')
	except Exception as e:
		raise e

# Runs a given maxima code. The input is taken
# as a list of lines of maxima code. This function
# should be the main API (alongside with runMaximaFile)
# to acces runMaxima.
#
# @param[in]	maximaCodeLines
#
# return                      Output of runMaxima that has been filtered to contain only
#                             the expressions of outputlines.
def runMaximaCode(maximaCodeLines):
	try:
		# Convert the lines into a single string. Note that we add ourselves the first
		# maxima command display2d:false, which causes the lines to be written on a single
		# line. This makes filtering a lot easier, but it also causes us the trouble of
		# removing the first line of filtered output.
		maximaCode = 'display2d:false;\r'
		for i in range(len(maximaCodeLines)):
			maximaCode += maximaCodeLines[i]
			if not i == len(maximaCodeLines) - 1:
				# Add \r at the end of each line, except the last line.
				maximaCode += '\r'

		# Run the code.
		output = runMaxima(maximaCode)

		# Since we are running maxima.bat, the output obtained from runMaxima
		# contains plenty of extra stuff that we have to get rid off. This is very
		# dubious thing to do and I am trying to find another way to access maxima.
		# But for now filtering it is.

		# Start filtering by removing all lines without the substring (%o, and also
		# all the lines that contain :=. We also remove here
		# the first outputline, since this contains 'false' from the display2d:false command
		# that we added previously.
		outputLines = [line for line in output if '(%o' in line and not ':=' in line][1:]
		# Then remove remove the prefix which is of the form '(%o',
		# along with additional spaces and \r.
		for i in range(len(outputLines)):
			# First spaces and \r.
			outputLines[i] = outputLines[i].replace(' ','')
			outputLines[i] = outputLines[i].replace('\r','')

			# Then the prefix.
			j = 0
			while outputLines[i][j] != ')':
				j += 1
			outputLines[i] = outputLines[i][j+1:]

		# Return the filtered output.
		return outputLines

	except Exception as e:
		print(Exception.__str__(e))

# Reads a text file containing Maxima code, and runs it
# using runMaximaCode. The output is written on the other given
# text file after it has been filtered with filterMaximaOutput.
#
# @param[in]	inputFile       Path of the inputFile.
# @param[out]	outputFile      Path of the outputFile.
def runMaximaFile(inputFile, outputFile):
	try:
		# Begin by reading the maxima code.
		maximaCodeLines = []
		with open(inputFile) as file:
			maximaCodeLines = file.readlines()

		# Run the code using runMaximaCode and store the filtered output.
		filteredOutput = runMaximaCode(maximaCodeLines)

		# Write the output into the outputFile, each line
		# of the output into a separate line.
		with open(outputFile, 'w') as file:
			for line in filteredOutput:
				file.write(line + '\n')

	except Exception as e:
		print(Exception.__str__(e))
