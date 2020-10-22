import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
# import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('C:/Users/moon/Documents/final_p/after_submit/구 모음/result_df_T.csv').set_index('Unnamed: 0')
data = np.array(df)

sc = StandardScaler()

X_train_std = sc.fit_transform(data)

cov_mat = np.cov(X_train_std.T)
eigen_vals, eigen_vecs = np.linalg.eig(cov_mat)
eigen_vals

tot = sum(eigen_vals)

var_exp = [(i/tot) for i in sorted(eigen_vals, reverse=True)]
cum_var_exp = np.cumsum(var_exp)

plt.bar(range(1,12), var_exp, alpha = 0.5, align='center', label = 'individual explained variance')
plt.step(range(1,12), cum_var_exp, where='mid', label = 'cumulative explained variance')
plt.ylabel('Explained variance ratio')
plt.xlabel('Principal component index')
plt.legend(loc='best')
plt.tight_layout()
plt.show()

# (고윳값, 고유 벡터) 튜플 리스트 생성
eigen_pairs = [(np.abs(eigen_vals[i]), eigen_vecs[:,i]) for i in range(len(eigen_vals))]

# 내림차순 정렬
eigen_pairs.sort(key=lambda k: k[0], reverse=True)

# 3차원 투영행렬을 만든다.
w = np.hstack((eigen_pairs[0][1][:, np.newaxis],
               eigen_pairs[1][1][:, np.newaxis],
               eigen_pairs[2][1][:, np.newaxis]))
print(w)

X_train_pca = X_train_std.dot(w)
X_train_pca