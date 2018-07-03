from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
import numpy as np

app = Flask(__name__)
api = Api(app)

TODOS = {
    'todo1': {'task': 'build an API'},
    'todo2': {'task': '?????'},
    'todo3': {'task': 'profit!'},
}


def abort_if_todo_doesnt_exist(todo_id):
    if todo_id not in TODOS:
        abort(404, message="Todo {} doesn't exist".format(todo_id))

parser = reqparse.RequestParser()
parser.add_argument('task')


# Todo
# shows a single todo item and lets you delete a todo item
class Todo(Resource):
    def get(self, todo_id):
        abort_if_todo_doesnt_exist(todo_id)
        return TODOS[todo_id]

    def delete(self, todo_id):
        abort_if_todo_doesnt_exist(todo_id)
        del TODOS[todo_id]
        return '', 204

    def put(self, todo_id):
        args = parser.parse_args()
        task = {'task': args['task']}
        TODOS[todo_id] = task
        return task, 201


# TodoList
# shows a list of all todos, and lets you POST to add new tasks
class TodoList(Resource):
    def get(self):
        return TODOS

    def post(self):
        args = parser.parse_args()
        ''' args = '{'task': '2,4.5,6.4'}' '''
        print(args)
        myvinit = str(args)
        print(myvinit[10:len(myvinit)-2])
        '''print(args.partition(','))'''
        ''' print(args.keys().lstrip('{')) '''
        todo_id = int(max(TODOS.keys()).lstrip('todo')) + 1
        todo_id = 'todo%i' % todo_id

        myv = myvinit[10:len(myvinit)-2]
        v1,v2,v3 = myv.split(',')
        

        ''' task=2;4;6.1 '''
        ''' myv = args[5:] '''
        '''v1,v2,v3 = myv.split(';')'''

        ''' task=2,4,6.1 '''
        '''print(args)'''
        '''myv = args.lstrip('task=')'''
        '''myv=eval('[' + myv + ']')'''

        '''for x in list(myv.items())[:3]:'''
        '''    print(x)'''

        '''vfinal=float(v1)+float(v2)+float(v3)'''
        '''v1 = 0.1
        v2 = 0.4
        v3 = 0.6'''

        vfinal = float(v1) + float(v2) + float(v3)

        TODOS[todo_id] = {'task': args['task'] + '=' + str(vfinal)}
        return TODOS[todo_id], 201

class myGA():
    def dec2bin(x):
        return bin(x)[2:] # x int, return as a string
    def bin2dec(x):
        return int(x, 2) # x string, return as a int
    def MyFx(x):
        return ((-np.math.pow(x, 2)) + (14 * x)) - 13;
    def OneCutPointCrossover(x):        
        size=np.shape(x)
        Pop_Size = int(size[0])
        StringLenChromosome = int(size[1])
        hasil= np.empty((2,StringLenChromosome)) # inisialisasi
        hasilcek= np.empty((2,StringLenChromosome)) # inisialisasi

        # // Menentukan PosisiOneCutPoint secara random
        BatasBawahRand = 1; BatasAtasRand = StringLenChromosome - 1
        lower=BatasBawahRand; upper=BatasAtasRand
        mbaris=1;nkolom=1
        PosisiOneCutPoint_init = myGA.myrandint(mbaris,nkolom,lower,upper) # berupa array[1x1]
        PosisiOneCutPoint = int(''.join(map(str,PosisiOneCutPoint_init[0]))) # convert array[1x1] ke scalar
        print("PosisiOneCutPoint= " + str(PosisiOneCutPoint))

        # // memilih 2 parent secara random 
        P1=np.empty((1,StringLenChromosome)) # inisialisasi Parent ke-1
        P2=np.empty((1,StringLenChromosome)) # inisialisasi Parent ke-2
        BatasBawahRand = 0; BatasAtasRand = Pop_Size - 1
        flag = True
        IndexP1 = 0; IndexP2 = 0
        while flag:
            IndexP1=myGA.myrandintscalar(BatasBawahRand,BatasAtasRand)
            IndexP2=myGA.myrandintscalar(BatasBawahRand,BatasAtasRand)
            if IndexP1 !=IndexP2:
                flag=False

        print("Index P1 = " + str(IndexP1 + 1) + ", Index P2 = " + str(IndexP2 + 1))
        # // menampilkan hasil induk terpilih
        print("P1= ")
        print(x[IndexP1])
        print("")
        print("P2= ")
        print(x[IndexP2])

        # copy array
        P1=x[IndexP1]
        #print(P1)
        hasil[0]=x[IndexP1]
        hasil=hasil.astype(int)
        #print(hasil[0])
        hasilcek[0]=x[IndexP1]
        hasilcek=hasilcek.astype(int)
        #print(hasilcek[0])

        P2=x[IndexP2]
        #print(P2)
        hasil[1]=x[IndexP2]
        #print(hasil[1])
        hasilcek[1]=x[IndexP2]
        #print(hasilcek[1])



        # cara 1 // melakukan proses pindah silang P1 dan P2
        hasil[0,PosisiOneCutPoint:StringLenChromosome]=P2[PosisiOneCutPoint:StringLenChromosome]
        hasil[1,PosisiOneCutPoint:StringLenChromosome]=P1[PosisiOneCutPoint:StringLenChromosome]

        # atau dengan for
        # cara 2 // melakukan proses pindah silang P1 dan P2
        for i in range(PosisiOneCutPoint,StringLenChromosome):
            hasilcek[0][i]=P2[i]
            hasilcek[1][i]=P1[i]

        #print("Cek:")
        #print(hasil)
        #print(hasilcek)

        return hasil,hasilcek
    def RandomMutasi(x):
        size=np.shape(x)
        Pop_Size = int(size[0])
        StringLenChromosome = int(size[1])
        hasil= np.empty((1,StringLenChromosome)) # inisialisasi

        # // Menentukan PosisiPointRandom secara random
        BatasBawahRand = 1; BatasAtasRand = StringLenChromosome      
        PosisiPointRandom = myGA.myrandintscalar(BatasBawahRand,BatasAtasRand)
        print("")
        print("PosisiPointRandom= " + str(PosisiPointRandom))

        # // memilih 1 parent secara random 
        P1=np.empty((1,StringLenChromosome)) # inisialisasi 1 Parent
        BatasBawahRand = 0; BatasAtasRand = Pop_Size - 1
        IndexP1 = myGA.myrandintscalar(BatasBawahRand,BatasAtasRand)

        print("Index P1 = " + str(IndexP1 + 1))
        # // menampilkan hasil induk terpilih
        print("P1= ")
        print(x[IndexP1])
        print("")

        # copy array
        P1=x[IndexP1]
        #print(P1)
        hasil=x[IndexP1]
        hasil=hasil.astype(int)
        #print(hasil)

        # // melakukan proses random mutasi
        if(hasil[PosisiPointRandom-1]==0):
            hasil[PosisiPointRandom-1]=1
        else:
            hasil[PosisiPointRandom-1]=0

        print(hasil)
        return hasil
    def myrand(mbaris,nkolom,lower,upper):        
        BatasRANDplusOne=10000
        #mbaris=10
        #nkolom=4
        Rand_Sample=np.random.randint(BatasRANDplusOne,size=(mbaris,nkolom))
        min_Rand_Sample = 0
        max_Rand_Sample = BatasRANDplusOne - 1
        upper_boundary= upper
        lower_boundary= lower
        normalize_Rand_Sample_minMax=(((Rand_Sample-min_Rand_Sample)/(max_Rand_Sample-min_Rand_Sample))*(upper_boundary-lower_boundary))+lower_boundary
        #print(normalize_Rand_Sample_minMax)
        #x = normalize_Rand_Sample_minMax
        return normalize_Rand_Sample_minMax
    def myrandint(mbaris,nkolom,lower,upper):        
        BatasRANDplusOne=1000
        #mbaris=10
        #nkolom=4
        Rand_Sample=np.random.randint(BatasRANDplusOne,size=(mbaris,nkolom))
        min_Rand_Sample = 0
        max_Rand_Sample = BatasRANDplusOne - 1
        upper_boundaryinit= 1
        lower_boundaryinit= 0
        randbilrealmulainolsampaisatu=(((Rand_Sample-min_Rand_Sample)/(max_Rand_Sample-min_Rand_Sample))*(upper_boundaryinit-lower_boundaryinit))+lower_boundaryinit
        upper_boundary= upper
        lower_boundary= lower
        normalize_Rand_Sample_minMax = lower_boundary+(randbilrealmulainolsampaisatu*(upper_boundary-lower_boundary))
        x =np.round(normalize_Rand_Sample_minMax,0)
        x=x.astype(int)
        return x
    def myrandintscalar(lower,upper):        
        BatasRANDplusOne=1000
        mbaris=1
        nkolom=1
        Rand_Sample=np.random.randint(BatasRANDplusOne,size=(mbaris,nkolom))
        min_Rand_Sample = 0
        max_Rand_Sample = BatasRANDplusOne - 1
        upper_boundaryinit= 1
        lower_boundaryinit= 0
        randbilrealmulainolsampaisatu=(((Rand_Sample-min_Rand_Sample)/(max_Rand_Sample-min_Rand_Sample))*(upper_boundaryinit-lower_boundaryinit))+lower_boundaryinit
        upper_boundary= upper
        lower_boundary= lower
        normalize_Rand_Sample_minMax = lower_boundary+(randbilrealmulainolsampaisatu*(upper_boundary-lower_boundary))
        x =np.round(normalize_Rand_Sample_minMax,0)
        x=x.astype(int)

        ## konversi ke scalar
        # yinit=''.join(str(i) for i in x[0]) # atau dengan
        yinit = ''.join(map(str,x[0]))
        y=int(yinit) # y string, return as a int
        return y
# TodoList
# shows a list of all todos, and lets you POST to add new tasks
class TodoGApp(Resource):
    def get(self):
        return TODOS
    def post(self):
        args = parser.parse_args()
        ''' args = '{'task': '2,4,0.4,0.6'}' '''
        print(".")
        print("..")
        print("POST Awal dari Web PHP ke WebApp RESTful Api Python:")
        print(args)
        myvinit = str(args)

        print(".")
        print("Hasil Ekstrasi POST Awal dari Web PHP ke WebApp RESTful Api Python:")
        print(myvinit[10:len(myvinit)-2])
        '''print(args.partition(','))'''
        ''' print(args.keys().lstrip('{')) '''
        todo_id = int(max(TODOS.keys()).lstrip('todo')) + 1
        todo_id = 'todo%i' % todo_id

        myv = myvinit[10:len(myvinit)-2]
        itermax,popsize,cr,mr = myv.split(',')


        ## //Case : Max, y = f(x) = -x^2 + 14x – 13, 0 ≤ x ≤ 15
        Batas_Min = 0
        Batas_Max = 15

        ## //Cek panjang string dari nilai biner Batas_Max

        vfinal=""
        ## // get atau setting parameter 
        Pop_Size = int(popsize)
        cr_ = float(cr)
        mr_ = float(mr)
        HasilBiner = myGA.dec2bin(Batas_Max)
        StringLenChromosome = len(HasilBiner)
        print(".")
        print("..")
        print("====================================================================")
        print("Start Solving Case : Max, y = f(x) = -x^2 + 14x – 13, 0 ≤ x ≤ 15 :")
        print("====================================================================")
        print("Hasil Biner= "+HasilBiner)
        print("StringLen Chromosome= "+str(StringLenChromosome))

        vfinal=vfinal+".^"+"..^"+"=====================================================^" \
        + "Start Solving Case : Max, y = f(x) = -x*x + 14x - 13, 0 <= x <= 15 :^" \
        + "=====================================================^" \
        + "Hasil Biner= "+HasilBiner + "^StringLen Chromosome= "+str(StringLenChromosome)

        NilaiDec = myGA.bin2dec(HasilBiner)
        print("Hasil Biner2Dec ("+HasilBiner+")= "+str(NilaiDec))
        vfinal=vfinal+"^Hasil Biner2Dec ("+HasilBiner+")= "+str(NilaiDec)

        print("") 
        print("1. generate individu")
        ## 1. generate individu
        ## random code biner
        batasbawahrandd = 0
        batasatasrandd = 1        
        individu = myGA.myrandint(Pop_Size,StringLenChromosome,batasbawahrandd,batasatasrandd)

        ## random code real
        #BatasBawahRandD = 0.1
        #BatasAtasRandD = 0.9
        #individu = myGA.myrand(Pop_Size,StringLenChromosome,BatasBawahRandD,BatasAtasRandD); # atau dengan
        #individu = BatasBawahRandD+np.random.random([Pop_Size,StringLenChromosome])*(BatasAtasRandD-BatasBawahRandD)
        
        ## Menampilkan hasil generate individu        
        print("    Chromosome |    x   |  y=f(x)    ")
        print("================================================")
        vfinal=vfinal+"^^"+"    Chromosome |    x   |  y=f(x)    ^" \
            + "================================================^"

        # indek ii=[lowerloop,upperloop]
        lowerloop=0 # nilai awal untuk index ii
        upperloop=Pop_Size
        for ii in range(lowerloop, upperloop):
            tempind1 = ''.join(str(individu[ii])) # hasil seperti '[1 0 1 1]'
            # atau = ''.join(str(individu[ii,:])) # artinya baris ke-ii semua kolom

            tempind2 = ''.join(map(str,individu[ii])) # hasil seperti '1011'
            # atau = ''.join(map(str,individu[ii,:]))
            xtemp =myGA.bin2dec(tempind2)
            print('P'+str(ii+1)+': '+tempind1 + '  |   ' + str(xtemp) + '\t|  ' + str(myGA.MyFx(xtemp)))
            vfinal=vfinal+ "P"+str(ii+1)+": "+tempind1 + "  |   " + str(xtemp) + " &nbsp &nbsp|  " + str(myGA.MyFx(xtemp))+"^"
        
        
        print()
        print("2. Reproduksi (Crossover dan Mutasi)")
        ## // 2. Reproduksi
        # // start proses crossover
        print("2.1 Crossover")
        # // hitung jumlah offspring atau anak crossover
        byk_anak_crossover = int(np.ceil(cr_ * Pop_Size))
        print("Banyaknya offspring crossover= "+str(byk_anak_crossover))

        # // Proses crossover dilakukan sebanyak (n_crossover)
        n_crossover = int(np.ceil(float(byk_anak_crossover / 2))) # // dibagi 2, krn 1 kali proses crossover akan menghasilkan 2 anak
        print("Proses crossover dilakukan sebanyak = " + str(n_crossover))

        HasilCrossover = np.empty((byk_anak_crossover,StringLenChromosome))  # inisialisasi
        HasilCrossovercek = np.empty((byk_anak_crossover,StringLenChromosome))  # inisialisasi
        HasilCrossoverTemp = np.empty((2,StringLenChromosome))
        HasilCrossoverTempcek = np.empty((2,StringLenChromosome))
        HasilCrossover=HasilCrossover.astype(int)
        HasilCrossovercek=HasilCrossovercek.astype(int)

        loop_anak_crossover = 0
        # // membuat offspring crossover sebanyak byk_anak_crossover
        for i in range(0,n_crossover):
            # //menampung hasil OneCutPointCrossover
            HasilCrossoverTemp,HasilCrossoverTempcek=myGA.OneCutPointCrossover(individu)
            HasilCrossover[loop_anak_crossover]=HasilCrossoverTemp[0]
            HasilCrossovercek[loop_anak_crossover]=HasilCrossoverTempcek[0]

            #print("Cek:")
            #print(HasilCrossoverTemp)
            #print(HasilCrossoverTempcek)
            #print(HasilCrossover)
            #print(HasilCrossovercek)
            loop_anak_crossover = loop_anak_crossover + 1

            if (loop_anak_crossover + 1) > byk_anak_crossover:
                break

            HasilCrossover[loop_anak_crossover]=HasilCrossoverTemp[1]
            HasilCrossovercek[loop_anak_crossover]=HasilCrossoverTempcek[1]

            loop_anak_crossover = loop_anak_crossover + 1

        # // menampilkan hasil crossover 
        print()
        print("Hasil Crossover cara 1:")
        vfinal=vfinal+"^"+"Hasil Crossover:^"
        for ii in range(0, byk_anak_crossover):
            tempind1 = ''.join(str(HasilCrossover[ii])) # hasil seperti '[1 0 1 1]'
            # atau = ''.join(str(HasilCrossover[ii,:])) # artinya baris ke-ii semua kolom

            tempind2 = ''.join(map(str,HasilCrossover[ii])) # hasil seperti '1011'
            # atau = ''.join(map(str,HasilCrossover[ii,:]))
            #print(tempind2)
            xtemp =myGA.bin2dec(tempind2)
            print('C'+str(ii+1)+': '+tempind1 + '  |   ' + str(xtemp) + '\t|  ' + str(myGA.MyFx(xtemp)))
            vfinal=vfinal+ "C"+str(ii+1)+": "+tempind1 + "  |   " + str(xtemp) + " &nbsp &nbsp|  " + str(myGA.MyFx(xtemp))+"^"

        #print("")
        #print("Hasil Crossover cara 2:")
        #for ii in range(0, byk_anak_crossover):
        #    tempind1 = ''.join(str(HasilCrossovercek[ii])) # hasil seperti '[1 0 1 1]'
        #    # atau = ''.join(str(HasilCrossovercek[ii,:])) # artinya baris ke-ii semua kolom

        #    tempind2 = ''.join(map(str,HasilCrossovercek[ii])) # hasil seperti '1011'
        #    # atau = ''.join(map(str,HasilCrossovercek[ii,:]))
        #    xtemp =myGA.bin2dec(tempind2)
        #    print('C'+str(ii+1)+': '+tempind1 + '  |   ' + str(xtemp) + '\t|  ' + str(myGA.MyFx(xtemp)))
        #    vfinal=vfinal+ "C"+str(ii+1)+": "+tempind1 + "  |   " + str(xtemp) + " &nbsp &nbsp|  " + str(myGA.MyFx(xtemp))+"^"
        
        print()
        # // start proses mutasi
        print("2.2 Mutasi")
        # // hitung jumlah offspring mutasi
        byk_anak_mutasi = int(np.ceil(mr_ * Pop_Size))
        print("Banyaknya offspring mutasi= "+str(byk_anak_mutasi))

        # // Proses mutasi dilakukan sebanyak (n_mutasi)
        n_mutasi = byk_anak_mutasi
        print("Proses mutasi dilakukan sebanyak = " + str(n_mutasi))

        HasilMutasi = np.empty((byk_anak_mutasi,StringLenChromosome))  # inisialisasi        
        HasilMutasiTemp = np.empty((1,StringLenChromosome))
        HasilMutasi=HasilMutasi.astype(int)

        # // membuat offspring mutasi sebanyak byk_anak_mutasi
        for i in range(0,n_mutasi):
            # //menampung hasil Random Mutasi
            HasilMutasiTemp=myGA.RandomMutasi(individu)
            #print(HasilMutasiTemp)
            if n_mutasi==1:
                HasilMutasi[i:]=HasilMutasiTemp
            else:
                HasilMutasi[i,:]=HasilMutasiTemp
            #print(HasilMutasi[i:])


        # // menampilkan hasil mutasi 
        print()
        print("Hasil Mutasi:")
        vfinal=vfinal+"^"+"Hasil Mutasi:^"
        for ii in range(0, byk_anak_mutasi):
            tempind1 = ''.join(str(HasilMutasi[ii])) # hasil seperti '[1 0 1 1]'
            # atau = ''.join(str(HasilMutasi[ii,:])) # artinya baris ke-ii semua kolom

            tempind2 = ''.join(map(str,HasilMutasi[ii])) # hasil seperti '1011'
            # atau = ''.join(map(str,HasilMutasi[ii,:]))
            #print(tempind2)
            xtemp =myGA.bin2dec(tempind2)
            print('M'+str(ii+1)+': '+tempind1 + '  |   ' + str(xtemp) + '\t|  ' + str(myGA.MyFx(xtemp)))
            vfinal=vfinal+ "M"+str(ii+1)+": "+tempind1 + "  |   " + str(xtemp) + " &nbsp &nbsp|  " + str(myGA.MyFx(xtemp))+"^"

        # // membuat penampungan populasi induk dan anak (crossover + mutasi)
        Pop_Size_induk_dan_anak = Pop_Size + byk_anak_crossover + byk_anak_mutasi
        IndividuGabungan = np.empty((Pop_Size_induk_dan_anak,StringLenChromosome))
        IndividuGabungan=IndividuGabungan.astype(int)
        IndividuGabunganSort = np.empty((Pop_Size_induk_dan_anak,StringLenChromosome))
        IndividuGabunganSort=IndividuGabunganSort.astype(int)
        fxIndividuGabungan = np.empty((Pop_Size_induk_dan_anak,1),float)
        

        IndividuGabungan[0:Pop_Size,:]=individu
        IndividuGabungan[Pop_Size:Pop_Size + byk_anak_crossover,:]=HasilCrossover
        IndividuGabungan[Pop_Size + byk_anak_crossover:Pop_Size_induk_dan_anak,:]=HasilMutasi

        # // menampilkan hasil individu gabungan
        #print(IndividuGabungan)
        print("")
        print("Hasil Populasi Gabungan induk dan anak (crossover + mutasi):")
        vfinal=vfinal+"^"+"Hasil Populasi Gabungan induk dan anak (crossover + mutasi):^"
        for ii in range(0, Pop_Size_induk_dan_anak):
            tempind1 = ''.join(str(IndividuGabungan[ii])) # hasil seperti '[1 0 1 1]'
            # atau = ''.join(str(IndividuGabungan[ii,:])) # artinya baris ke-ii semua kolom

            tempind2 = ''.join(map(str,IndividuGabungan[ii])) # hasil seperti '1011'
            # atau = ''.join(map(str,IndividuGabungan[ii,:]))
            xtemp = myGA.bin2dec(tempind2)
            fxIndividuGabungan[ii] = myGA.MyFx(xtemp)
            print('G'+str(ii+1)+': '+tempind1 + '  |   ' + str(xtemp) + '\t|  ' + ''.join(map(str,fxIndividuGabungan[ii])))
            vfinal=vfinal+ "G"+str(ii+1)+": "+tempind1 + "  |   " + str(xtemp) + " &nbsp &nbsp|  " + ''.join(map(str,fxIndividuGabungan[ii])) +"^"

        # // Seleksi IndividuGabungan berdasarkan nilai f(x)
        NextIndividu = np.empty((Pop_Size,StringLenChromosome))
        NextIndividu=NextIndividu.astype(int)

        indicesort=fxIndividuGabungan.ravel().argsort()
        for i in range(Pop_Size_induk_dan_anak-1, -1, -1): # [Pop_Size_induk_dan_anak-1, Pop_Size_induk_dan_anak-2,..,0]
            #print(str(i)+'   '+str(Pop_Size_induk_dan_anak-1-i))
            IndividuGabunganSort[i]=IndividuGabungan[indicesort[Pop_Size_induk_dan_anak-1-i]]
            #print(indicesort[i])


        individu = IndividuGabunganSort[0:Pop_Size,:]
        print("")
        vfinal=vfinal+"^"+"Hasil Seleksi untuk Next Generation ke->2:^"
        print("Hasil Seleksi untuk Next Generation ke->2:")
        for ii in range(0, Pop_Size):
            tempind1 = ''.join(str(individu[ii])) # hasil seperti '[1 0 1 1]'
            # atau = ''.join(str(individu[ii,:])) # artinya baris ke-ii semua kolom

            tempind2 = ''.join(map(str,individu[ii])) # hasil seperti '1011'
            # atau = ''.join(map(str,individu[ii,:]))
            xtemp = myGA.bin2dec(tempind2)            
            print('nextG'+str(ii+1)+': '+tempind1 + '  |   ' + str(xtemp) + '\t|  ' + str(myGA.MyFx(xtemp)))
            vfinal=vfinal+ "nextG"+str(ii+1)+": "+tempind1 + "  |   " + str(xtemp) + " &nbsp &nbsp|  " + str(myGA.MyFx(xtemp))+"^"

        vfinalparam=""
        #print(itermax) 
        for i in range(1,int(itermax)+1):
            # print (i)
            if i == int(itermax):
                vfinalparam=vfinalparam+str(i)
            else:
                vfinalparam=vfinalparam+str(i)+"^"
            
            
            


        # vfinal mengambil nilai individu terbaik
        # vfinal = float(v1) + float(v2) + float(v3)
        vfinal=vfinal+"^"+".^"+"Done..! :D^"+"=====================================================^"+"."

        TODOS[todo_id] = {'task': args['task'] + '=' + vfinalparam +"`"+vfinal}

        print("")       
        print(".")       
        print("Done..! :D")
        print("=============================================================")
        print(".")
        
        return TODOS[todo_id], 201

##
## Actually setup the Api resource routing here
##
api.add_resource(TodoGApp, '/ga')
api.add_resource(TodoList, '/todos')
api.add_resource(Todo, '/todos/<todo_id>')


if __name__ == '__main__':
    app.run(debug=True)