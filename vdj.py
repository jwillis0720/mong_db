import sys
class vdj_dicts():
    def __init__(self):
        
        self.v_dict_full = {"IGHV1-02*01":0,"IGHV1-02*02":0,"IGHV1-02*02nsl":0,"IGHV1-02*03":0,"IGHV1-02*04":0,"IGHV1-03*01":0,"IGHV1-03*02":0,"IGHV1-08*01":0,"IGHV1-12*01":0,
        "IGHV1-12*02":0,"IGHV1-14*01":0,"IGHV1-17*01":0,"IGHV1-17*02":0,"IGHV1-18*01":0,"IGHV1-18*01nsl":0,"IGHV1-18*02":0,"IGHV1-24*01":0,"IGHV1-45*01":0,"IGHV1-45*02":0,"IGHV1-45*03":0,
        "IGHV1-46*01":0,"IGHV1-46*02":0,"IGHV1-46*03":0,"IGHV1-58*01":0,"IGHV1-58*02":0,"IGHV1-67*01":0,"IGHV1-67*02":0,"IGHV1-68*01":0,"IGHV1-69*01":0,"IGHV1-69*02":0,"IGHV1-69*03":0,
        "IGHV1-69*04":0,"IGHV1-69*05":0,"IGHV1-69*06":0,"IGHV1-69*07":0,"IGHV1-69*08":0,"IGHV1-69*09":0,"IGHV1-69*10":0,"IGHV1-69*11":0,"IGHV1-c*01":0,"IGHV1-f*01":0,"IGHV1-f*02":0,
        "IGHV1-NL1":0,"IGHV1/OR15-1":0,"IGHV1/OR15-2":0,"IGHV1/OR15-3":0,"IGHV1/OR15-4":0,"IGHV1/OR15-5":0,"IGHV1/OR15-6":0,"IGHV1/OR15-9":0,"IGHV2-05*01":0,"IGHV2-05*02":0,"IGHV2-05*03":0,
        "IGHV2-05*04":0,"IGHV2-05*05":0,"IGHV2-05*06":0,"IGHV2-05*07":0,"IGHV2-05*08":0,"IGHV2-05*09":0,"IGHV2-05*10":0,"IGHV2-10*01":0,"IGHV2-26*01":0,"IGHV2-70*01":0,"IGHV2-70*02":0,"IGHV2-70*03":0,"IGHV2-70*04":0,
        "IGHV2-70*05":0,"IGHV2-70*06":0,"IGHV2-70*07":0,"IGHV2-70*08":0,"IGHV2-70*09":0,"IGHV2-70*10":0,"IGHV2-70*11":0,"IGHV2-70*12":0,"IGHV2-70*13":0,"IGHV3-06*01":0,"IGHV3-07*01":0,"IGHV3-07*01nsl":0,
        "IGHV3-07*02":0,"IGHV3-09*01":0,"IGHV3-11*01":0,"IGHV3-11*02":0,"IGHV3-11*03":0,"IGHV3-11*03nsl":0,"IGHV3-13*01":0,"IGHV3-13*01nsl":0,"IGHV3-13*02":0,"IGHV3-13*03":0,"IGHV3-15*01":0,"IGHV3-15*02":0,
        "IGHV3-15*03":0,"IGHV3-15*04":0,"IGHV3-15*05":0,"IGHV3-15*06":0,"IGHV3-15*07":0,"IGHV3-15*08":0,"IGHV3-16*01":0,"IGHV3-16*02":0,"IGHV3-19*01":0,"IGHV3-20*01":0,"IGHV3-21*01":0,"IGHV3-21*02":0,"IGHV3-22*01":0,
        "IGHV3-23*01":0,"IGHV3-23*02":0,"IGHV3-23*03":0,"IGHV3-25*01":0,"IGHV3-29*01":0,"IGHV3-30*01":0,"IGHV3-30*02":0,"IGHV3-30*03":0,"IGHV3-30*04":0,"IGHV3-30*05":0,"IGHV3-30*06":0,"IGHV3-30*07":0,"IGHV3-30*08":0,
        "IGHV3-30*09":0,"IGHV3-30*10":0,"IGHV3-30*11":0,"IGHV3-30*12":0,"IGHV3-30*13":0,"IGHV3-30*14":0,"IGHV3-30*15":0,"IGHV3-30*16":0,"IGHV3-30*17":0,"IGHV3-30*18":0,"IGHV3-30*19":0,"IGHV3-30-3*01":0,"IGHV3-30-3*02":0,
        "IGHV3-32*01":0,"IGHV3-33*01":0,"IGHV3-33*02":0,"IGHV3-33*03":0,"IGHV3-33*04":0,"IGHV3-33*05":0,"IGHV3-35*01":0,"IGHV3-36*01":0,"IGHV3-37*01":0,"IGHV3-37*02":0,"IGHV3-38*01":0,"IGHV3-38*02":0,"IGHV3-41*01":0,"IGHV3-42*01":0,
        "IGHV3-43*01":0,"IGHV3-43*02":0,"IGHV3-47*01":0,"IGHV3-47*02":0,"IGHV3-47*03":0,"IGHV3-48*01":0,"IGHV3-48*02":0,"IGHV3-48*03":0,"IGHV3-49*01":0,"IGHV3-49*02":0,"IGHV3-49*02nsl":0,"IGHV3-49*03":0,"IGHV3-49*03nsl":0,"IGHV3-52*01":0,
        "IGHV3-52*02":0,"IGHV3-53*01":0,"IGHV3-53*01nsl-A":0,"IGHV3-53*01nsl-B":0,"IGHV3-53*01nsl-C":0,"IGHV3-53*02":0,"IGHV3-53*03":0,"IGHV3-54*01":0,"IGHV3-57*01":0,"IGHV3-60*01":0,"IGHV3-62*01":0,"IGHV3-63*01":0,"IGHV3-64*01":0,"IGHV3-64*02":0,
        "IGHV3-64*03":0,"IGHV3-64*04":0,"IGHV3-64*05":0,"IGHV3-64*05nsl-A":0,"IGHV3-64*05nsl-B":0,"IGHV3-64*05nsl-C":0,"IGHV3-65*01":0,"IGHV3-66*01":0,"IGHV3-66*02":0,"IGHV3-66*03":0,"IGHV3-66*04":0,"IGHV3-72*01":0,"IGHV3-72*02":0,"IGHV3-73*01":0,
        "IGHV3-73*02":0,"IGHV3-74*01":0,"IGHV3-74*02":0,"IGHV3-74*03":0,"IGHV3-75*01":0,"IGHV3-76*01":0,"IGHV3-d*01":0,"IGHV3-g*01":0,"IGHV3-h*01":0,"IGHV3/OR15-7":0,"IGHV4-04*01":0,"IGHV4-04*02":0,"IGHV4-04*03":0,"IGHV4-04*04":0,"IGHV4-04*05":0,"IGHV4-04*06":0,
        "IGHV4-04*07":0,"IGHV4-28*01":0,"IGHV4-28*02":0,"IGHV4-28*03":0,"IGHV4-28*04":0,"IGHV4-28*05":0,"IGHV4-30-2*01":0,"IGHV4-30-2*02":0,"IGHV4-30-2*03":0,"IGHV4-30-2*04":0,"IGHV4-30-4*01":0,"IGHV4-30-4*02":0,"IGHV4-30-4*03":0,"IGHV4-30-4*04":0,"IGHV4-30-4*05":0,
        "IGHV4-30-4*06":0,"IGHV4-31*01":0,"IGHV4-31*02":0,"IGHV4-31*03":0,"IGHV4-31*04":0,"IGHV4-31*05":0,"IGHV4-31*06":0,"IGHV4-31*07":0,"IGHV4-31*08":0,"IGHV4-31*09":0,"IGHV4-31*10":0,"IGHV4-34*01":0,"IGHV4-34*02":0,"IGHV4-34*03":0,"IGHV4-34*04":0,"IGHV4-34*05":0,
        "IGHV4-34*06":0,"IGHV4-34*07":0,"IGHV4-34*08":0,"IGHV4-34*09":0,"IGHV4-34*10":0,"IGHV4-34*11":0,"IGHV4-34*12":0,"IGHV4-34*13":0,"IGHV4-39*01":0,"IGHV4-39*02":0,"IGHV4-39*03":0,"IGHV4-39*04":0,"IGHV4-39*05":0,"IGHV4-39*06":0,"IGHV4-55*01":0,"IGHV4-55*02":0,
        "IGHV4-59*01":0,"IGHV4-59*01nsl":0,"IGHV4-59*02":0,"IGHV4-59*03":0,"IGHV4-59*04":0,"IGHV4-59*05":0,"IGHV4-59*06":0,"IGHV4-59*07":0,"IGHV4-59*08":0,"IGHV4-59*09":0,"IGHV4-59*10":0,"IGHV4-61*01":0,"IGHV4-61*02":0,"IGHV4-61*03":0,"IGHV4-61*04":0,"IGHV4-61*05":0,
        "IGHV4-61*06":0,"IGHV4-61*07":0,"IGHV4-61*08":0,"IGHV4-b*01":0,"IGHV4-b*02":0,"IGHV4/OR15-8":0,"IGHV5-51*01":0,"IGHV5-51*02":0,"IGHV5-51*03":0,"IGHV5-51*04":0,"IGHV5-51*05":0,"IGHV5-78*01":0,"IGHV5-a*01":0,"IGHV5-a*02":0,"IGHV5-a*03":0,"IGHV5-a*04":0,
        "IGHV6-01*01":0,"IGHV6-01*02":0,"IGHV7-04-1*01":0,"IGHV7-04-1*02":0,"IGHV7-04-1*03":0,"IGHV7-27*01":0,"IGHV7-40*01":0,"IGHV7-56*01":0,"IGHV7-81*01":0}
       
        self.d_full_dict = {"IGHD1-01*01":0,"IGHD1-01*01R":0,"IGHD1-07*01":0,"IGHD1-07*01R":0,"IGHD1-14*01":0,"IGHD1-14*01R":0,"IGHD1-20*01":0,"IGHD1-20*01R":0,"IGHD1-26*01":0,"IGHD1-26*01R":0,"IGHD2-02*01":0,"IGHD2-02*01R":0,"IGHD2-02*02":0,"IGHD2-02*02R":0,
        "IGHD2-02*03":0,"IGHD2-02*03R":0,"IGHD2-08*01":0,"IGHD2-08*01R":0,"IGHD2-08*02":0,"IGHD2-08*02R":0,"IGHD2-15*01":0,"IGHD2-15*01R":0,"IGHD2-21*01":0,"IGHD2-21*01R":0,"IGHD2-21*02":0,"IGHD2-21*02R":0,"IGHD3-03*01":0,"IGHD3-03*01R":0,"IGHD3-03*02":0,"IGHD3-03*02R":0,
        "IGHD3-09*01":0,"IGHD3-09*01R":0,"IGHD3-10*01":0,"IGHD3-10*01R":0,"IGHD3-10*02":0,"IGHD3-10*02R":0,"IGHD3-16*01":0,"IGHD3-16*01R":0,"IGHD3-16*02":0,"IGHD3-16*02R":0,"IGHD3-22*01":0,"IGHD3-22*01R":0,"IGHD4-04*01":0,"IGHD4-04*01R":0,"IGHD4-11*01":0,"IGHD4-11*01R":0,
        "IGHD4-17*01":0,"IGHD4-17*01R":0,"IGHD4-23*01":0,"IGHD4-23*01R":0,"IGHD5-05*01":0,"IGHD5-05*01R":0,"IGHD5-12*01":0,"IGHD5-12*01R":0,"IGHD5-18*01":0,"IGHD5-18*01R":0,"IGHD5-24*01":0,"IGHD5-24*01R":0,"IGHD6-06*01":0,"IGHD6-06*01R":0,"IGHD6-13*01":0,"IGHD6-13*01R":0,
        "IGHD6-19*01":0,"IGHD6-19*01R":0,"IGHD6-25*01":0,"IGHD6-25*01R":0,"IGHD7-27*01":0,"IGHD7-27*01R":0,"IGHDIR*01":0,"IGHDIR*01R":0,"IGHDIR1*01":0,"IGHDIR1*01R":0,"IGHDIR2*01":0,"IGHDIR2*01R":0,"IGHD1/OR15-1":0,"IGHD1/OR15-1R":0,"IGHD2/OF15-2":0,"IGHD2/OR15-2R":0,
        "IGHD3/OR15-3":0,"IGHD3/OR15-3R":0,"IGHD4/OR15-4":0,"IGHD4/OR15-4R":0,"IGHD5/OR15-5":0,"IGHD5/OR15-5R":0}

        self.j_dict_full = {"IGHJ1*01":0,"IGHJ2*01":0,"IGHJ3*01":0,"IGHJ3*02":0,"IGHJ4*01":0,"IGHJ4*02":0,"IGHJ4*03":0,
        "IGHJ5*01":0,"IGHJ5*02":0,"IGHJ6*01":0,"IGHJ6*02":0,"IGHJ6*03":0}
     
        self.d_family = {"1":0,"2":0,"3":0,"4":0,"5":0,"6":0,"7":0}
        self.v_family = {"1":0,"2":0,"3":0,"4":0,"5":0,"6":0,"7":0}
        self.j_family = {"1":0,"2":0,"3":0,"4":0,"5":0,"6":0}
     
        self.d_gene = {"1-01":0, "1-07":0, "1-14":0, "1-20":0, "1-26":0, "2-02":0, "2-08":0, "2-15":0, "2-21":0, "3-03":0, "3-09":0, 
        "3-10":0, "3-16":0, "3-22":0, "4-04":0, "4-17":0, "4-23":0, "5-05":0, "5-12":0, "5-24":0, "6-06":0, "6-13":0, "6-19":0, "6-25":0, 
        "7-27":0}
    
    def get_full_d_dict(self):
        return self.d_full_dict
    
    def fill_d_dict(self,query):
        #result = query['result']
        for i in query['result']:
            gene = i['_id'] 
            if gene in self.d_full_dict.keys():
                self.d_full_dict[gene] = i['sum']

    def fill_v_dict(self,query):
        for i in query['result']:
            gene = i['_id']
            if gene in self.v_dict_full.keys():
                self.v_dict_full[gene] = i['sum']

    def fill_j_dict(self,query):
        for i in query['result']:
            gene = i['_id']
            if gene in self.j_dict_full.keys():
                self.j_dict_full[gene] = i['sum']
    
    def get_v_family(self):
        sum = 0.0
        for gene in self.v_dict_full:
            family = gene[4]
            amount = self.v_dict_full[gene]
            sum += amount
            if family in self.v_family.keys():
                self.v_family[family] += amount

        for i in self.v_family:
            self.v_family[i] = (self.v_family[i]/sum)*100
        return self.v_family


    def get_d_family(self):
        sum = 0.0
        for gene in self.d_full_dict:
            family = gene[4]
            amount = self.d_full_dict[gene]
            sum += amount
            if family in self.d_family.keys():
                self.d_family[family] += amount

        for i in self.d_family:
            self.d_family[i] = (self.d_family[i]/sum)*100
        return self.d_family

    def get_j_family(self):
        sum = 0.0
        for gene in self.j_dict_full:
            family = gene[4]
            amount = self.j_dict_full[gene]
            sum += amount
            if family in self.j_family.keys():
                self.j_family[family] += amount

        for i in self.j_family:
            self.j_family[i] = (self.j_family[i]/sum)*100
        return self.d_family
    
    def get_d_gene(self):
        sum = 0.0
        for gene in self.d_full_dict:
            family = gene[4:gene.find('*')]
            amount = int(self.d_full_dict[gene])
            sum += amount
            if family in self.d_gene.keys():
                self.d_gene[family] += amount
        for gene in self.d_gene:
            self.d_gene[gene] = (self.d_gene[gene]/sum)*100

        return self.d_gene
