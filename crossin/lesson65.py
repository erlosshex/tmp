import pickle

test_data=['save me',123.456,True]

f=file('test.data','w')
pickle.dump(test_data,f)
f.close()

f=file('test.data')
tes_data=pickle.load(f)
f.close()

print tes_data
