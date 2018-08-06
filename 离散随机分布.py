import numpy as np
from matplotlib.pyplot import plot,show,hist
cash=np.zeros(10000)
cash[0]=1000
outcome=np.random.binomial(9,0.5,size=len(cash))
for i in range(1,len(cash)):
    if outcome[i] < 5:
        cash[i] = cash[i - 1] - 1
    elif outcome[i] < 10:
        cash[i] = cash[i - 1] + 1
    else:
        raise AssertionError("Unexcrpted outcome" + outcome)

print(outcome.min(), outcome.max())
plot(np.arange(len(cash)), cash)
show()


N=10000
normal_values=np.random.normal(size=N)
dummy,bins,dummy=hist(normal_values,int(np.sqrt(N)),normed=True,lw=1)
print(bins)
sigma=1
mu=0
plot(bins,1/(sigma*np.sqrt(2*np.pi))*np.exp(-(bins-mu)**2/(2*sigma**2)),lw=2)
show()



