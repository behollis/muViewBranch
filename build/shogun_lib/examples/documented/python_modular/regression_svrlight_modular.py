# In this example a support vector regression algorithm is trained on a
# real-valued toy data set. The underlying library used for the SVR training is
# SVM^light. The SVR is trained with regularization parameter C=1 and a gaussian
# kernel with width=2.1. The the label of both the train and the test data are
# fetched via svr.classify().get_labels().
# 
# For more details on the SVM^light see
#  T. Joachims. Making large-scale SVM learning practical. In Advances in Kernel
#  Methods -- Support Vector Learning, pages 169-184. MIT Press, Cambridge, MA USA, 1999.

###########################################################################
# svm light based support vector regression
###########################################################################
from numpy import array
from numpy.random import seed, rand
from tools.load import LoadMatrix
lm=LoadMatrix()

traindat = lm.load_numbers('../data/fm_train_real.dat')
testdat = lm.load_numbers('../data/fm_test_real.dat')
label_traindat = lm.load_labels('../data/label_train_twoclass.dat')

parameter_list = [[traindat,testdat,label_traindat,1.2,1,1e-5,1e-2,1],[traindat,testdat,label_traindat,2.3,0.5,1e-5,1e-6,1]]

def regression_svrlight_modular(fm_train=traindat,fm_test=testdat,label_train=label_traindat, \
				    width=1.2,C=1,epsilon=1e-5,tube_epsilon=1e-2,num_threads=3):


	from shogun.Features import RegressionLabels, RealFeatures
	from shogun.Kernel import GaussianKernel
	try:
		from shogun.Regression import SVRLight
	except ImportError:
		print('No support for SVRLight available.')
		return

	feats_train=RealFeatures(fm_train)
	feats_test=RealFeatures(fm_test)

	kernel=GaussianKernel(feats_train, feats_train, width)

	labels=RegressionLabels(label_train)

	svr=SVRLight(C, epsilon, kernel, labels)
	svr.set_tube_epsilon(tube_epsilon)
	svr.parallel.set_num_threads(num_threads)
	svr.train()

	kernel.init(feats_train, feats_test)
	out = svr.apply().get_labels()
	
	return out, kernel 

if __name__=='__main__':
	print('SVRLight')
	regression_svrlight_modular(*parameter_list[0])