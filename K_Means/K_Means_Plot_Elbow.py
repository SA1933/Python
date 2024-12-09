from sklearn.cluster import KMeans
from matplotlib.pyplot import plt
from sklearn.preprocessing import StandardScaler

df = ("pastikan berisi kolom non numerik")
df = df.dropna()

X_std = StandardScaler().fit_transform(df)

# Run the Kmeans algorithm and get the index of data points clusters
sse = []
list_k = list(range(1, 10))

for k in list_k:
    km = KMeans(n_clusters=k)
    km.fit(X_std)
    sse.append(km.inertia_)

# Plot sse against k
plt.figure(figsize=(6, 6))
plt.plot(list_k, sse, '-o')
plt.xlabel(r'Number of clusters *k*')
plt.ylabel('Sum of squared distance');