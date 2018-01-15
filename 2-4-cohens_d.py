import os
import numpy as np
from pandas import Series

import matplotlib as mpl
mpl.use('TkAgg')
import matplotlib.pyplot as plt


try:
	import nsfg, first #, thinkstats2
except ImportError:
	# ROOT_DIR = os.getcwd()
	# DATA_DIR = "ThinkStats2/code"
	# os.chdir(os.path.join(ROOT_DIR, DATA_DIR))
	# import nsfg
	# import thinkstats2s
	pass


def cohens_d(g1, g2):
	"""
	input: g1 and g2 are numpy 1-d arrays or equivalent
	(pandas Series or Dataframe column)
	return: Cohen's D, computed as difference between group means
	divided by the square root of the pooled variance
	"""
	try:
		# convert to Series so ignore NaNs for np.mean and variance & Series.count()
		g1, g2 = Series(g1), Series(g2)
	except TypeError:
		raise

	# difference between group means
	diff_means = np.mean(g1) - np.mean(g2)

	# pooled_variance
	n1, n2 = g1.count(), g2.count()  # ignore NaNs; AttributeError if ndarray.count()
	var1, var2 = np.var(g1), np.var(g2)
	pooled_var = (n1 * var1 + n2 * var2) / (n1 + n2)

	return diff_means / np.sqrt(pooled_var)


# Set directory & Import Data
ROOT_DIR = os.getcwd()
DATA_DIR = "ThinkStats2/code/"
os.chdir(os.path.join(ROOT_DIR, DATA_DIR))
print("current directory", os.getcwd())

# preg = nsfg.ReadFemResp()
# print("outcome" in preg)
# live = preg.loc[preg.outcome == 1]
#
# # birth order `birthord`
# firsts = live.loc[live.birthord == 1]
# others = live.loc[live.birthord != 1]

# import first
live, firsts, others = first.MakeFrames()


# birth weight: `totalwgt_lb` (`birthwgt_lb` + `birthwgt_oz`)
firsts_wgt = firsts.totalwgt_lb
others_wgt = others.totalwgt_lb

# pregnancy length: prglngth
first_prglen = firsts.prglngth
others_prglen = others.prglngth

print("Problem 1: Are first babies (birthord) heavier or lighter (totalwgt_lb)?")

# mean weight
first_mean_wgt = np.round(np.mean(firsts_wgt), 3)
others_mean_wgt = np.round(np.mean(others_wgt), 3)

if first_mean_wgt > others_mean_wgt:
	print("On average first born children are heavier")
else:
	print("On average, first born children are lighter")

print("Mean weight for first borns ({} lbs) vs others ({} lbs).".format(
		first_mean_wgt, others_mean_wgt))

print("Problem 2: Compute Cohen's d for firstborns vs others for birth weight (totalwgt_lb).")

d_birth_weight = round(cohens_d(firsts_wgt, others_wgt), 3)
print("The difference in means for total birth weight \
for firstborns vs others is {} standard deviations".format(d_birth_weight))


print("Problem 3: Compute Cohen's d for firstborns vs others for pregnancy length.")
d_preg_length = cohens_d(first_prglen, others_prglen)
print("Cohen's d for pregnancy length: {} standard deviations".format(d_preg_length))



