from queue import PriorityQueue

class Graph:
    # Pembuatan graf berarah berbobot untuk algoritma Dijkstra
    def __init__(self, simpul):
        self.banyaksimpul = simpul
        # Inisialisasi adjacency matriks dengan nilai -9999: Tidak terhubung sama sekali
        # Nilai matriks adjacency m[i][j] adalah bobot antara kota asal i dan kota tujuan j
        self.sisi = [[-9999 for i in range(simpul)] for j in range(simpul)]
        # Daftar kota yang telah dikunjungi
        self.telah_dikunjungi = []
        # Daftar semua kota dalam graf
        self.daftarkota = []
    def tambah_nama_kota(self, namakota):
        self.daftarkota.append(namakota)    
    def tambah_sisi(self, namaasal, namatujuan, bobot):
        asal = self.daftarkota.index(namaasal)
        tujuan = self.daftarkota.index(namatujuan)
        self.sisi[asal][tujuan] = bobot

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
        openlist = set([asal])
        closedlist = set([])
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
            if n == tujuan:
                reconstructPath = []
                while adjmap[n] != n:
                    reconstructPath.append(n)
                    n = adjmap[n]
                reconstructPath.append(asal)
                reconstructPath.reverse()
                print("Rute termurah adalah:", asal, end='')
                for stops in reconstructPath:
                    if stops != asal:
                        print(" -->", stops, end='')
                return reconstructPath
            for (a, bobot) in self.tetangga(n):
                if a not in openlist and a not in closedlist:
                    openlist.add(a)
                    adjmap[a] = n
                    harga_terkini[a] = harga_terkini[n] + bobot
                else:
                    if harga_terkini[a] > harga_terkini[n] + bobot:
                        harga_terkini[a] = harga_terkini[n] + bobot
                        adjmap[a] = n
                        if a in closedlist:
                            closedlist.remove(a)
                            openlist.add(a)
            openlist.remove(n)
            closedlist.add(n)
        print("Rute termurah tidak ditemukan.")
        return None

            


def penerbangan_termurah_dijkstra(graf, awal, akhir):
    kota_awal = graf.daftarkota.index(awal)
    kota_akhir = graf.daftarkota.index(akhir)
    hash = {i:float(99999999) for i in range(graf.banyaksimpul)}
    hash[kota_awal] = 0

    queue = PriorityQueue()
    queue.put((0, kota_awal))

    while not queue.empty():
        (a, kota_terkini) = queue.get()
        graf.telah_dikunjungi.append(kota_terkini)

        for tetangga in range(graf.banyaksimpul):
            if graf.sisi[kota_terkini][tetangga] != -9999:
                jarak = graf.sisi[kota_terkini][tetangga]
                if tetangga not in graf.telah_dikunjungi:
                    harga_baru = hash[kota_terkini] + jarak
                    harga_lama = hash[tetangga]
                    if harga_baru < harga_lama:
                        queue.put((harga_baru, tetangga))
                        hash[tetangga] = harga_baru
    
    print("Biaya termurah perjalanan dari", awal, "ke", akhir, "adalah:", hash[kota_akhir], "000.")

# Penambahan ke daftar kota harus berurut
rute = Graph(6)
rute.tambah_nama_kota("Jakarta")
rute.tambah_nama_kota("Singapore")
rute.tambah_nama_kota("Kuala Lumpur")
rute.tambah_nama_kota("Hong Kong")
rute.tambah_nama_kota("Bangkok")
rute.tambah_nama_kota("Tokyo")
rute.tambah_sisi("Jakarta", "Kuala Lumpur", 1500)
rute.tambah_sisi("Jakarta", "Singapore", 1900)
rute.tambah_sisi("Singapore", "Bangkok", 1800)
rute.tambah_sisi("Singapore", "Hong Kong", 4400)
rute.tambah_sisi("Kuala Lumpur", "Bangkok", 1600)
rute.tambah_sisi("Kuala Lumpur", "Tokyo", 5900)
rute.tambah_sisi("Hong Kong", "Kuala Lumpur", 5100)
rute.tambah_sisi("Hong Kong", "Tokyo", 7600)
rute.tambah_sisi("Bangkok", "Kuala Lumpur", 2100)
rute.tambah_sisi("Bangkok", "Tokyo", 6000)
rute.tambah_sisi("Tokyo", "Singapore", 9800)

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

penerbangan_termurah_dijkstra(rute, asal, tujuan)
graflain = GraphA(adjacency_list_rute)
graflain.rute_termurah_astar(asal, tujuan)


        
        
    
