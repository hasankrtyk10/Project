import gtts
import os


baslik = "Konusan robot"

data = gtts(text="Merhaba dunya", lang="tr")
data.save(baslik+".mp3")