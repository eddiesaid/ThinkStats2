import nsfg

preg = nsfg.ReadFemPreg()
nsfg.CleanFemPreg(preg)
live = preg[preg.outcome==1]
livemap = nsfg.MakePregMap(live)
diffs = []
for k in livemap.keys():
	if len(livemap[k]) > 1:
		op = []
		for p in livemap[k]:
			if preg.iloc[p].birthord == 1:
				fp = preg.iloc[p].prglngth
			else:
				op.append(preg.iloc[p].prglngth)
		diffs.append(fp - sum(op)/len(op))
print("mean diff:", sum(diffs)/len(diffs))
#mean diff is 0.118
#for populations, mean diff is 0.078