import pandas as pd
import numpy as np
from scipy.stats import expon

# Cargar datos
df = pd.read_csv('csv/autos_datos.csv')

# Convertir tiempos a segundos
def time_to_seconds(t):
    h, m, s = map(int, t.split(':'))
    return h*3600 + m*60 + s

df['entrada_s'] = df['entrada'].apply(time_to_seconds)
df['salida_s'] = df['salida'].apply(time_to_seconds)
df['tiempo_servicio'] = df['salida_s'] - df['entrada_s']

total_autos = len(df)
for server in sorted(df['server'].unique()):
    tiempos = df[df['server'] == server]['tiempo_servicio'] / 60  # ahora en minutos
    loc, scale = expon.fit(tiempos, floc=0, method="MM")
    mu_min = 1 / scale  # autos por minuto
    proporcion = len(tiempos) / total_autos

# Estimar tasa de llegada usando observaciones de cola
cola = pd.read_csv('csv/observaciones_cola.csv')
def time_to_seconds(t):
    h, m, s = map(int, t.split(':'))
    return h*3600 + m*60 + s

t0 = time_to_seconds(cola['tiempo_registro'].iloc[0])
tf = time_to_seconds(cola['tiempo_registro'].iloc[-1])
tiempo_total_min = 71

cola_inicial = cola['total_cola'].iloc[0]
cola_final = cola['total_cola'].iloc[-1]
llegadas_reales = total_autos + (cola_final - cola_inicial)
print(f"{total_autos} {cola_final} {cola_inicial}")
lambda_est = llegadas_reales / tiempo_total_min

intervalos = 3
cola['segundos'] = cola['tiempo_registro'].apply(time_to_seconds)
t0 = cola['segundos'].iloc[0]
tf = cola['segundos'].iloc[-1]
duracion = tf - t0
puntos_corte = [t0 + i*duracion//intervalos for i in range(intervalos+1)]

for i in range(intervalos):
    ini, fin = puntos_corte[i], puntos_corte[i+1]
    # Autos atendidos en el intervalo
    autos_intervalo = df[(df['salida_s'] >= ini) & (df['salida_s'] < fin)]
    n_autos = len(autos_intervalo)
    minutos = 71
    lambda_est = n_autos / minutos if minutos > 0 else 0

for i in range(intervalos):
    ini, fin = puntos_corte[i], puntos_corte[i+1]
    total_servicio_intervalo = 0
    total_autos_intervalo = 0
    for server in sorted(df['server'].unique()):
        autos_server = df[(df['server'] == server) & (df['salida_s'] >= ini) & (df['salida_s'] < fin)]
        tiempos = autos_server['tiempo_servicio']
        n_autos = len(tiempos)
        total_autos_intervalo += n_autos
        if n_autos > 0:
            loc, scale = expon.fit(tiempos, floc=0)
            mu_seg = 1/scale
            mu_min = mu_seg * 60
            total_servicio_intervalo += mu_min
        else:
            print(f"  Servidor {server}: sin autos atendidos")
    minutos = 71
    lambda_est = total_autos_intervalo / minutos if minutos > 0 else 0

# Tasa de atención total y tasa de llegada total (todo el periodo)
mu_total = 0
lambda_est = llegadas_reales / tiempo_total_min

for server in sorted(df['server'].unique()):
    tiempos = df[df['server'] == server]['tiempo_servicio'] / 60  # ahora en minutos
    if len(tiempos) > 0:
        print(f"Servidor {server}: media = {tiempos.mean():.2f} min, max = {tiempos.max():.2f} min, min = {tiempos.min():.2f} min")
        loc, scale = expon.fit(tiempos, floc=0)
        mu_min = 1 / scale
        mu_total += mu_min

intervalo_min = 10
t0 = cola['segundos'].min()
puntos_corte = np.arange(t0, t0 + 70*60 + 1, intervalo_min*60)

for i in range(1, len(puntos_corte)):
    ini, fin = puntos_corte[i-1], puntos_corte[i]
    # Busca la observación de cola más cercana al inicio y fin
    idx_ini = (np.abs(cola['segundos'] - ini)).idxmin()
    idx_fin = (np.abs(cola['segundos'] - fin)).idxmin()
    c_ini = cola['total_cola'].iloc[idx_ini]
    c_fin = cola['total_cola'].iloc[idx_fin]
    atendidos = df[(df['salida_s'] >= ini) & (df['salida_s'] < fin)].shape[0]
    llegadas = max(0, (c_fin - c_ini) + atendidos)
    minutos = (fin - ini) / 60
    lambda_intervalo = llegadas / minutos if minutos > 0 else 0

print(f"\n{'='*40}\nANÁLISIS EN INTERVALOS DE {intervalo_min} MINUTOS\n{'='*40}")
for i in range(1, len(puntos_corte)):
    ini, fin = puntos_corte[i-1], puntos_corte[i]
    idx_ini = (np.abs(cola['segundos'] - ini)).idxmin()
    idx_fin = (np.abs(cola['segundos'] - fin)).idxmin()
    c_ini = cola['total_cola'].iloc[idx_ini]
    c_fin = cola['total_cola'].iloc[idx_fin]
    atendidos = df[(df['salida_s'] >= ini) & (df['salida_s'] < fin)].shape[0]
    llegadas = max(0, (c_fin - c_ini) + atendidos)
    minutos = (fin - ini) / 60
    lambda_intervalo = llegadas / minutos if minutos > 0 else 0

    print(f"\nIntervalo {i}: {ini//60:.0f} - {fin//60:.0f} min")
    print(f"  Llegadas al sistema: {llegadas}")
    print(f"  Atendidos: {atendidos}")

    mu_total_intervalo = 0
    for server in sorted(df['server'].unique()):
        autos_server = df[(df['server'] == server) & (df['salida_s'] >= ini) & (df['salida_s'] < fin)]
        tiempos = autos_server['tiempo_servicio']
        n_autos = len(tiempos)
        llegadas_server = df[(df['server'] == server) & (df['entrada_s'] >= ini) & (df['entrada_s'] < fin)].shape[0]
        if n_autos > 0:
            loc, scale = expon.fit(tiempos, floc=0)
            mu_seg = 1/scale
            mu_min = mu_seg * 60
            mu_total_intervalo += mu_min
            print(f"    Servidor {server}: mu ≈ {mu_min:.4f} autos/minuto, atendidos = {n_autos}, llegadas = {llegadas_server}")
        else:
            print(f"    Servidor {server}: sin autos atendidos, llegadas = {llegadas_server}")
    print(f"  Tasa de llegada (lambda): {lambda_intervalo:.4f} autos/minuto")
    print(f"  Tasa de atención total (mu): {mu_total_intervalo:.4f} autos/minuto")
    tasa_atencion_efectiva = atendidos / minutos if minutos > 0 else 0
    print(f"  Tasa de atención efectiva: {tasa_atencion_efectiva:.4f} autos/minuto")

print(f"\n{'='*40}\nRESUMEN TOTAL DEL SISTEMA\n{'='*40}")
print(f"Tasa de llegada total estimada (lambda): {lambda_est:.4f} autos/minuto")
print(f"Tasa de atención total del sistema (suma de mu por servidor): {mu_total:.4f} autos/minuto")
total_atendidos = df.shape[0]
print(f"Total autos atendidos: {total_atendidos}")
print(f"Tiempo total observado: {tiempo_total_min:.2f} minutos")
tasa_atencion_efectiva = total_atendidos / tiempo_total_min
print(f"Tasa de atención efectiva (autos atendidos / tiempo): {tasa_atencion_efectiva:.4f} autos/minuto")

