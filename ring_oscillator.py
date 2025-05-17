from inverter import Inverter


class RingOscillator:
    def __init__(self,no_inverters):
        self.no_inverters = no_inverters
        self.inverter_list = []
        self.p_out_list = None
        self.protein = None
    
    def make_inverters(self):
        p_in = 70 #int(input("Enter PoPS Input : "))
        print("\n")
        half_life = 10 # int(input("Enter Half life (minutes) : "))
        print('\n')
        p_out_list = []
        protein_list = []
        
        for i in range(self.no_inverters):
            if i-1 != -1:
                inverter = Inverter(p_out_list[i-1], half_life)
                self.inverter_list.append(inverter)
                p_out_list.append(inverter.output_signal())
                protein_list.append(inverter.get_protein())
            else:
                inverter = Inverter(p_in,half_life)
                self.inverter_list.append(inverter)
                p_out_list.append(inverter.output_signal())
                protein_list.append(inverter.get_protein())
        
        self.p_out_list = p_out_list
        self.protein = protein_list
        return p_out_list

    def simulate(self):
        p_out_list = self.make_inverters()
        for value in p_out_list:
            print(f"Output : {value} \n")

        print("\n")
        print("These are One Cycle Outputs")
        print("Protein R created : ",self.protein)


if __name__ == '__main__':
    ro = RingOscillator(9)
    ro.simulate()

