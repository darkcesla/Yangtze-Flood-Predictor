class PrediksiBanjir:
    def __init__(self, data):
        self.data = data
        self.area_terpilih = None
        self.banjir_terjadi = False

    def phi(self, Q_t_d1, R_t_d2, E_t_d3):
        return Q_t_d1 + 0.8 * R_t_d2 + 0.5 * E_t_d3

    def prediksi_banjir(self, area, Q_t_d1, R_t_d2, E_t_d3):
        heuristik = self.phi(Q_t_d1, R_t_d2, E_t_d3)

        if heuristik > 500:
            print(f"Prediksi banjir di {area}! Heuristik: {heuristik}")
            self.banjir_terjadi = True
            self.area_terpilih = area

    def backtracking_search(self, area_terpilih=None):
        if area_terpilih is None:
            area_terpilih = []

        for area in self.data:
            if area not in area_terpilih:
                Q_t_d1 = self.data[area].get('Q(t-d1+1)', 0)  
                R_t_d2 = self.data[area].get('R(t-d2+1)', 0)  
                E_t_d3 = self.data[area].get('E(t-d3+1)', 0)  

                area_terpilih.append(area)
                self.prediksi_banjir(area, Q_t_d1, R_t_d2, E_t_d3)

                if not self.banjir_terjadi:
                    self.backtracking_search(area_terpilih)

                area_terpilih.remove(area)

    def hasil_prediksi(self):
        if self.banjir_terjadi:
            print(f"Banjir terjadi di {self.area_terpilih}.")
        else:
            print("Tidak ada prediksi banjir.")

# Data dummy untuk Sungai Yangtze
data_dummy_yangtze = {
    'Pingshan': {'Q(t-d1+1)': 1000, 'R(t-d2+1)': 1150, 'E(t-d3+1)': 1130},
    'Gaochang': {'Q(t-d1+1)': 120, 'R(t-d2+1)': 55, 'E(t-d3+1)': 35},
    'Lijiawan': {'Q(t-d1+1)': 110, 'R(t-d2+1)': 60, 'E(t-d3+1)': 40},
    'Beibei': {'Q(t-d1+1)': 95, 'R(t-d2+1)': 48, 'E(t-d3+1)': 28},
    'Wulong': {'Q(t-d1+1)': 130, 'R(t-d2+1)': 45, 'E(t-d3+1)': 33}
}

# Membuat objek PrediksiBanjir dan melakukan prediksi
prediksi_yangtze = PrediksiBanjir(data_dummy_yangtze)
prediksi_yangtze.backtracking_search()
prediksi_yangtze.hasil_prediksi()
class PrediksiBanjir:
    def __init__(self, data):
        self.data = data
        self.area_terpilih = None
        self.banjir_terjadi = False

    def phi(self, Q_t_d1, R_t_d2, E_t_d3):
        # Implementasi fungsi phi sesuai dengan karakteristik sistem hidrologi yang sebenarnya
        # Contoh implementasi sederhana, sesuaikan dengan kebutuhan sebenarnya
        return Q_t_d1 + 0.8 * R_t_d2 + 0.5 * E_t_d3

    def prediksi_banjir(self, area, Q_t_d1, R_t_d2, E_t_d3):
        heuristik = self.phi(Q_t_d1, R_t_d2, E_t_d3)

        if heuristik > 500:
            print(f"Prediksi banjir di {area}! Heuristik: {heuristik}")
            self.banjir_terjadi = True
            self.area_terpilih = area

    def backtracking_search(self, area_terpilih=None):
        if area_terpilih is None:
            area_terpilih = []

        for area in self.data:
            if area not in area_terpilih:
                Q_t_d1 = self.data[area].get('Q(t-d1+1)', 0)  # Ganti dengan nilai sebenarnya
                R_t_d2 = self.data[area].get('R(t-d2+1)', 0)  # Ganti dengan nilai sebenarnya
                E_t_d3 = self.data[area].get('E(t-d3+1)', 0)  # Ganti dengan nilai sebenarnya

                area_terpilih.append(area)
                self.prediksi_banjir(area, Q_t_d1, R_t_d2, E_t_d3)

                if not self.banjir_terjadi:
                    self.backtracking_search(area_terpilih)

                area_terpilih.remove(area)

    def hasil_prediksi(self):
        if self.banjir_terjadi:
            print(f"Banjir terjadi di {self.area_terpilih}.")
        else:
            print("Tidak ada prediksi banjir.")

# Data dummy untuk Sungai Yangtze
data_dummy_yangtze = {
    'Pingshan': {'Q(t-d1+1)': 100, 'R(t-d2+1)': 50, 'E(t-d3+1)': 30},
    'Gaochang': {'Q(t-d1+1)': 120, 'R(t-d2+1)': 55, 'E(t-d3+1)': 35},
    'Lijiawan': {'Q(t-d1+1)': 110, 'R(t-d2+1)': 60, 'E(t-d3+1)': 40},
    'Beibei': {'Q(t-d1+1)': 95, 'R(t-d2+1)': 48, 'E(t-d3+1)': 28},
    'Wulong': {'Q(t-d1+1)': 130, 'R(t-d2+1)': 45, 'E(t-d3+1)': 33}
}

# Membuat objek PrediksiBanjir dan melakukan prediksi
prediksi_yangtze = PrediksiBanjir(data_dummy_yangtze)
prediksi_yangtze.backtracking_search()
prediksi_yangtze.hasil_prediksi()
