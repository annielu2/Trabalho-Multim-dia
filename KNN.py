import Dados
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
import numpy as np

audios, list_emotions = Dados.get_audios()

target = np.array(list_emotions, dtype=object)

data = np.array(audios, dtype=object)

dataset = {'data': audios, 'target': target} 

res = train_test_split(data, target, train_size=0.8, test_size=0.2, random_state=12)
train_data, test_data, train_labels, test_labels = res


knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(train_data, train_labels)

print("Predictions from the classifier:")
test_data_predicted = knn.predict(test_data)
print(test_data_predicted)
print("Target values:")
print(test_labels)


