import Dados
from sklearn.neighbors import KNeighborsClassifier

audios = Dados.get_audios()

neigh = KNeighborsClassifier(n_neighbors=3)
#neigh.fit(audios, y)

