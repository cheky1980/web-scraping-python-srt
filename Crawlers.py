links_https = []   # Lista vacía

for t in tags:
    link = t.get("href")
    if link and link.startswith("https"):
        print("URL:", link)
        links_https.append(link)   # Agrego el enlace a la lista

print('\n')
print("Cantidad de enlaces https:", len(links_https))
