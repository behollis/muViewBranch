# This example demonstrates how to load string features from files.
# We cover two cases: First, we show how to obtain StringCharFeatues
# from a directory of text files (particularly useful in computational biology)
# and second, we demonstrate how to load StringCharFeatues from one (multi-line) file. 
# 

parameter_list=[[".", "features_string_char_modular.py"]]

def features_string_file_modular(directory, fname):
	from shogun.Features import StringCharFeatures, RAWBYTE
	from shogun.IO import AsciiFile

	# load features from directory
	f=StringCharFeatures(RAWBYTE)
	f.load_from_directory(directory)

	#and output several stats
	#print("max string length", f.get_max_vector_length())
	#print("number of strings", f.get_num_vectors())
	#print("length of first string", f.get_vector_length(0))
	#print("str[0,0:3]", f.get_feature(0,0), f.get_feature(0,1), f.get_feature(0,2))
	#print("len(str[0])", f.get_vector_length(0))
	#print("str[0]", f.get_feature_vector(0))

	#or load features from file (one string per line)
	fil=AsciiFile(fname)
	f.load(fil)
	#print(f.get_features())

	#or load fasta file
	#f.load_fasta('fasta.fa')
	#print(f.get_features())
	return f.get_features(), f

if __name__=='__main__':
	print('StringWordFeatures')
	features_string_file_modular(*parameter_list[0])