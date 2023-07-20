class Audio:
    def __init__(self, z_c_r, energy, mfcc):
        self.z_c_r = z_c_r
        self.energy = energy
        self.mfcc = mfcc
    
    def get_energy(self):
        return self.energy