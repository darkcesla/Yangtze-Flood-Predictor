from flask import Flask, render_template, request
from datetime import datetime
import locale

app = Flask(__name__)

class PrediksiBanjir:
    def __init__(self, data):
        self.data = data
        self.results = {}

    def phi(self, Q_t_d1, R_t_d2, E_t_d3):
        return Q_t_d1 + 0.8 * R_t_d2 + 0.5 * E_t_d3

    def prediksi_banjir(self, area, Q_t_d1, R_t_d2, E_t_d3, hari_tanggal):
        heuristik = self.phi(Q_t_d1, R_t_d2, E_t_d3)

        if heuristik > 500:
            self.results[area] = f"Prediksi banjir di {area} pada {hari_tanggal}! Heuristik: {heuristik}"
        else:
            self.results[area] = f"Tidak ada prediksi banjir di {area} pada {hari_tanggal}."

    def backtracking_search(self, area_terpilih=None):
        if area_terpilih is None:
            area_terpilih = []

        for area in self.data:
            if area not in area_terpilih:
                Q_t_d1 = self.data[area].get('Q(t-d1+1)', 0)
                R_t_d2 = self.data[area].get('R(t-d2+1)', 0)
                E_t_d3 = self.data[area].get('E(t-d3+1)', 0)

                area_terpilih.append(area)

                hari_tanggal = datetime.now().strftime("%A, %d %B %Y")
                self.prediksi_banjir(area, Q_t_d1, R_t_d2, E_t_d3, hari_tanggal)

                self.backtracking_search(area_terpilih)

                area_terpilih.remove(area)

    def hasil_prediksi(self):
        return self.results

locale.setlocale(locale.LC_TIME, 'id_ID.utf8')

data_dummy_yangtze = {
    'Pingshan': {'Q(t-d1+1)': 1000, 'R(t-d2+1)': 1150, 'E(t-d3+1)': 1130},
    'Gaochang': {'Q(t-d1+1)': 120, 'R(t-d2+1)': 55, 'E(t-d3+1)': 35},
    'Lijiawan': {'Q(t-d1+1)': 110, 'R(t-d2+1)': 60, 'E(t-d3+1)': 40},
    'Beibei': {'Q(t-d1+1)': 1195, 'R(t-d2+1)': 1148, 'E(t-d3+1)': 2228},
    'Wulong': {'Q(t-d1+1)': 130, 'R(t-d2+1)': 45, 'E(t-d3+1)': 33}
}

prediksi_yangtze = PrediksiBanjir(data_dummy_yangtze)

@app.route('/', methods=['GET', 'POST'])
def index():
    results = None

    if request.method == 'POST':
        prediksi_yangtze.backtracking_search()
        results = prediksi_yangtze.hasil_prediksi()

    return render_template('index.html', results=results)

if __name__ == '__main__':
    app.run(debug=True)
