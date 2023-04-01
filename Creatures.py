import numpy as np
class Creature:
    bones = []
    """
    list of bones, bone : list [int ind1, int ind2, float l] (unités du système internationnal), the bones are solid
    """
    joints = []
    """
    list of joints
    joint : list [np.array pos, np.array vel, np.array acc, float a0, float angle, 
    float couple, float dcouple]
    a0 : angle au repos
    angle : angle effectif par rapport au repos
    """

    maxcouple = 1 #(N.m) couple maximal des joints, en valeur absolue
    minl, maxl = 1, 
    m, ml = 1, 1 #masse d'un joint, masse linéique d'un os
    def __main__(self):
        return
    
    def set_to_random_creature(self, n):
        """
        n : number of joints
        """
        for i in range(n):
            b=Creature.random_bone(n)
            self.bones.append(b)
        
        js = {} #dic of joints : {nb : joint}
        for i in range(n):
            
            self.bones.append(b)
            
        
    def random_bone(self, n):
        """
        generates a new bone
        nombre de joints disponibles
        """
        a, b = int(np.random()*n),int(np.random()*n) #dans [0, n-1]
        l = self.minl + np.random()*(self.maxl - self.minl)
        
        assert a<n and b<n
        return [a, b, l]
    def new_joint(self, x, y):
        """
        generates a new joint
        """
        pos, vel, acc = [x, y],[0, 0],[0, 0]
        a0 = np.random()* np.pi*2
        return [pos, vel, acc, a0, 0, 0, 0]
        