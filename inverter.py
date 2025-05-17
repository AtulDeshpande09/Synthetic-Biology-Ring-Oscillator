class ProteinGenerator:
    def __init__(self,PoPS,t_half):
        self.p_in = PoPS
        self.production_rate = 1
        self.t_half = 10 # minutes
        self.k_d = 0.69/t_half
        self.time = 5*60

    def __repr__(self):
        return f"Protein Generator : \n\tPoPS : {self.p_in}"
    def generate_protein(self):
        # concentration of repressor protein 
        # we will start with 0
        R = 0
        dt = 0.5
        steps = int(self.time/dt)
        R_over_time = []
        # some magic and few calculations
        for _ in range(steps):
            dR_dt = self.production_rate*self.p_in - self.k_d*R
            # update R using Euler method
            R += dR_dt*dt
            R_over_time.append(R)
        return R,R_over_time
        

class PoPSRegulator:
    def __init__(self , R ):
        self.R = R
        self.k_on = 1
        self.k_off = 1
        self.k_D = self.k_off/self.k_on
        self.p_max = 70    # max output if R is not present
        self.D = None      # DNA concetration
    
    def regulate_PoPS(self):

        p_out = self.p_max*self.k_D/(self.k_D+self.R)
        return p_out

class Inverter:
    def __init__(self , PoPS , t_half):
        self.p_in = PoPS
        self.half_life = t_half
        #Protein Generator
        self.pg = ProteinGenerator(PoPS , t_half)
        self.protein = self.pg.generate_protein()
        self.R = self.protein[0]
        self.R_over_time = self.protein[1]
        
        #PoPS regulator
        self.pr = PoPSRegulator(self.R)
        self.p_out = self.pr.regulate_PoPS()

    def output_signal(self):
        return self.p_out
    def get_protein(self):
        return self.R
    def simulate(self):
        print(f"Input Signal : {self.p_in} PoPS")
        print(f"Output Signal : {self.p_out} PoPS")
        print("\n")
        print(f"Repressor Protein : {self.R}")

if __name__ =='__main__':

    pg = ProteinGenerator(70,10)
    conc = pg.generate_protein()
    print(f"Protein Concentration : {conc[0]}")
    
    pr = PoPSRegulator(conc[0])
    p_out = pr.regulate_PoPS()

    print(f"PoPS output : {p_out}")
    print("*-----*-----*")
    inverter = Inverter(70,10)
    inverter.simulate()
