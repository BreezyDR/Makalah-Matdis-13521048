class GraphA:
    def __init__(self, adjlist):
        self.adjlist = adjlist
    def tetangga(self, kotaseberang):
        # Daftar kota tetangga/adjacent dari kota asal
        return self.adjlist[kotaseberang]
    def heuristic(self, banyakkota):
        # Inisalisasi h(n)
        H = {"Jakarta": 1, "Singapore": 1, "Kuala Lumpur": 1,
            "Hong Kong": 1, "Bangkok": 1, "Tokyo": 1}
        return H[banyakkota]
    def rute_termurah_astar(self, asal, tujuan):
        openlist = [asal]
        closedlist = []
        count = 0
        adjmap = {}
        adjmap[asal] = asal
        harga_terkini = {}
        harga_terkini[asal] = 0
        while len(openlist) > 0:
            n = None
            for kota in openlist:
                if n == None or harga_terkini[kota] + self.heuristic(kota) < harga_terkini[n] + self.heuristic(n):
                    n = kota
            if n == None:
                print("Rute termurah tidak ditemukan.")
                return None
            for (a, bobot) in self.tetangga(n):
                if a not in openlist and a not in closedlist:
                    openlist.append(a)
                    adjmap[a] = n
                    harga_terkini[a] = harga_terkini[n] + bobot
                else:
                    if harga_terkini[a] > harga_terkini[n] + bobot:
                        harga_terkini[a] = harga_terkini[n] + bobot
                        adjmap[a] = n
                        if a in closedlist:
                            closedlist.remove(a)
                            openlist.append(a)
            openlist.remove(n)
            closedlist.append(n)
            if n == tujuan:
                count = harga_terkini[n]
                reconstructPath = []
                while adjmap[n] != n:
                    reconstructPath.append(n)
                    n = adjmap[n]
                reconstructPath.append(asal)
                reconstructPath.reverse()
                print("Biaya penerbangan adalah Rp%d.000" % count)
                print("Rute termurah adalah:", asal, end='')
                for stops in reconstructPath:
                    if stops != asal:
                        print(" -->", stops, end='')
                return reconstructPath
        print("Rute termurah tidak ditemukan.")
        return None


adjacency_list_rute = {
    "Jakarta": [("Kuala Lumpur", 1500), ("Singapore", 1900)],
    "Singapore": [("Bangkok", 1800), ("Hong Kong", 4400)],
    "Kuala Lumpur": [("Bangkok", 1600), ("Tokyo", 5900)],
    "Hong Kong": [("Kuala Lumpur", 5100), ("Tokyo", 7600)],
    "Bangkok": [("Kuala Lumpur", 2100), ("Tokyo", 6000)],
    "Tokyo": [("Singapore", 9800)]
}

print("Masukkan kota asal:")
asal = input()
print("Masukkan kota tujuan:")
tujuan = input()

graflain = GraphA(adjacency_list_rute)
graflain.rute_termurah_astar(asal, tujuan)


        
        
    
