import numpy as np
import matplotlib.pyplot as plt
def farAway(r1, r2, Lx, Ly):
    r12 = np.linalg.norm(r1-r2)
    if r12 > Lx/2 or r12 > Ly/2:
        return True
    else:
        return False
def plotPair(k1,k2,N1,N2):
    c = 'firebrick'
    #head_width: float or None (default: 3*width)
    #head_length: float or None (default: 1.5 * head_width)
    
    hw=0.05*3.5
    hl=0.1*3
    if np.min(np.linalg.norm(allK-k1,axis=1))<1e-1 and np.min(np.linalg.norm(allK-k2,axis=1))<1e-1 and not farAway(k1,k2,N1,N2):
        plt.arrow(k1[0],k1[1],k2[0]-k1[0],k2[1]-k1[1],length_includes_head=True,fc=c, ec='k',width=0.05)

    else:
        c = 'firebrick'
        plt.arrow(k1[0],k1[1],k2[0]-k1[0],k2[1]-k1[1],length_includes_head=True,fc=c, ec='k',width=0.05,alpha=0.4,clip_on = False)
        
a1 = np.array([1,0])
a2 = np.array([1/2,np.sqrt(3)/2])
basis = [np.array([0,0]),np.array([0,1/np.sqrt(3)])]
zhat = np.array([0.0,0.0,1.0])
a1_3D = np.array([a1[0],a1[1],0.0])
a2_3D = np.array([a2[0],a2[1],0.0])
b1 = -2*np.pi*np.cross(zhat,a2_3D)[:2] /np.linalg.norm(np.cross(a1,a2))
b2 = 2*np.pi*np.cross(zhat,a1_3D)[:2] /np.linalg.norm(np.cross(a1,a2))

def momentumLabels(N1,N2):
    return [((p,q),orb) for p in range(N1) for q in range(N2)  for orb in range(len(basis))  ]
def momentumLabelToK(l,N1,N2):
    return (l[0][0])*b1/N1+(l[0][1])*b2/N2 #+ basis[l[1]]

plt.figure(figsize=(10,10))

N1=6
N2=6
ks = momentumLabels(N1,N2)
allK = np.array([momentumLabelToK(l,N1,N2) for l in ks])
for l in ks[::2]:
    phase = 1.
    spot = l[0]
    ab = (((l[0][0]+1),(l[0][1])),0)
    k1,k2 = momentumLabelToK(l,N1,N2),momentumLabelToK(ab,N1,N2)
    plt.plot([k1[0]],[k1[1]],'oC0',ms=10)
    
    plotPair(k1,k2,N1,N2)
    l=ab
    ab = (((l[0][0]),(l[0][1]-1)),0)
    k1,k2 = momentumLabelToK(l,N1,N2),momentumLabelToK(ab,N1,N2)
    plotPair(k1,k2,N1,N2)

    l=ab
    ab = (((l[0][0]-1),(l[0][1])),0)
    k1,k2 = momentumLabelToK(l,N1,N2),momentumLabelToK(ab,N1,N2)
    eps = np.array([0,0.09])
    plotPair(k1+eps,k2+eps,N1,N2)
    
    l=ab
    ab = (((l[0][0]),(l[0][1]+1)),0)
    k1,k2 = momentumLabelToK(l,N1,N2),momentumLabelToK(ab,N1,N2)
    eps = np.array([0.07,0])
    plotPair(k1+eps,k2+eps,N1,N2)
    
    #l=ls[LabelToIndex(ab)]
    #assert(l[0]==spot)

# plt.xlim(-0.5,5.5) 
# plt.ylim(-3.2,6.3) 
plt.xlabel("kx",fontsize=14)
plt.ylabel("ky",fontsize=14)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.savefig("Berry4.png",bbox_inches='tight')
plt.show()
