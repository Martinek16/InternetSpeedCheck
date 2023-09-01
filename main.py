import speedtest


def preveri_hitrost_interneta():
  st = speedtest.Speedtest()
  st.get_best_server()
  hitrost_prenosa = st.download() / 1_000_000
  hitrost_nalaganja = st.upload() / 1_000_000
  ping = st.results.ping
  return hitrost_prenosa, hitrost_nalaganja, ping


def izpisi_informacije_o_internetu(hitrost_prenosa, hitrost_nalaganja, ping):
  print("Informacije o internetni povezavi:")
  print(f"Hitrost prenosa: {hitrost_prenosa:.2f} Mbps")
  print(f"Hitrost nalaganja: {hitrost_nalaganja:.2f} Mbps")
  print(f"Ping: {ping} ms")
  print("----------------------------------------")


def izracunaj_cas_prenosa(velikost_datoteke_gb, hitrost_prenosa):
  velikost_v_mb = velikost_datoteke_gb * 1024
  cas_v_sekundah = velikost_v_mb / hitrost_prenosa
  return cas_v_sekundah


hitrost_prenosa, hitrost_nalaganja, ping = preveri_hitrost_interneta()
izpisi_informacije_o_internetu(hitrost_prenosa, hitrost_nalaganja, ping)

velikost_datoteke_gb = float(input("Vnesi velikost datoteke (v GB): "))

cas_prenosa = izracunaj_cas_prenosa(velikost_datoteke_gb, hitrost_prenosa)
print(f"Čas prenosa datoteke bo približno: {cas_prenosa:.2f} sekund")
