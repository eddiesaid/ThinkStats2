import hinc, hinc2, thinkstats2
from density import *

def Median(xs):
	cdf = thinkstats2.Cdf(xs)
	return cdf.Value(0.5)
	
def RawMoment(xs, k):
	return sum(x**k for x in xs) / len(xs)
	
def CentralMoment(xs, k):
	mean = RawMoment(xs, 1)
	return sum((x - mean)**k for x in xs) / len(xs)
	
def StandardizedMoment(xs, k):
	var = CentralMoment(xs, 2)
	std = math.sqrt(var)
	return CentralMoment(xs, k) / std**k

df = hinc.ReadData()
log_sample = hinc2.InterpolateSample(df, log_upper=6.0)
median = Median(log_sample)
mean = RawMoment(log_sample, 1)
std = math.sqrt(CentralMoment(log_sample, 2))
print("median: ", median)
print("mean: ", mean)
pearson = 3*(mean - median)/std
print("Pearson's skewness: ", pearson)