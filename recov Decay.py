    def recoveryDecayEquation(self,T1,T2,PD,vector,time):
            vector = vector.transpose()
            Decay =np.matrix([[np.exp(-time/T2),0,0],[0,np.exp(-time/T2),0],[0,0,np.exp(-time/T1)]])
            Decay = np.dot(Decay,vector)
        
            Rec= np.dot(np.matrix([[0,0,(1-(np.exp(-time/T1)))]]),PD)
            Rec = Rec.transpose()
            Decay = np.matrix(Decay)
            Rec =  np.matrix(Rec)    
        
            RD  = Decay + Rec
            RD = RD.transpose()
            return RD