#!/usr/bin/env python
# coding: utf-8

# ## LINFO1341-PROJET1-2023
# ### Quelques Scripts Python utiles
# 

# In[30]:


from scapy.all import *
from collections import Counter
import matplotlib.pyplot as plt

# Charger le fichier de capture de paquets
packets = rdpcap('Capture scenario 2 home.pcapng')

# Extraire les adresses IP source et destination
src_ips = [pkt[IP].src for pkt in packets if IP in pkt]
dst_ips = [pkt[IP].dst for pkt in packets if IP in pkt]

# Calculer le nombre de paquets envoyés et reçus pour chaque adresse IP
src_counts = Counter(src_ips)
dst_counts = Counter(dst_ips)

# Afficher les résultats
print("Paquets envoyés par adresse IP source:")
print(src_counts)
print("Paquets reçus par adresse IP destination:")
print(dst_counts)

# Tracer un graphique de barres des adresses IP les plus actives
top_src_ips = src_counts.most_common(10)
plt.bar([ip[0] for ip in top_src_ips], [ip[1] for ip in top_src_ips])
plt.title("Top 10 adresses IP source")
plt.xlabel("Adresse IP")
plt.ylabel("Nombre de paquets")
plt.xticks(rotation=90) # Rotation à 90 degrés du texte sur l'axe des x
plt.show()


# In[29]:


# Tracer un graphique de barres des adresses IP les plus actives
top_src_ips = dst_counts.most_common(10)
plt.bar([ip[0] for ip in top_src_ips], [ip[1] for ip in top_src_ips])
plt.title("Top 10 adresses IP destination")
plt.xlabel("Adresse IP")

plt.ylabel("Nombre de paquets")
plt.xticks(rotation=90) # Rotation à 90 degrés du texte sur l'axe des x
plt.show()

