import seaborn as sns
import matplotlib.pyplot as plt

# memuat dataset bawaan Seaborn yang bernama 'tips' ke dalam variabel data.
data = sns.load_dataset('tips')

# membuat scatter plot menggunakan seaborn
sns.scatterplot(x='total_bill', y='tip', data=data, size='size', hue='sex', style='time')

# memberi judul pada grafik
plt.title('Relationship between Total Bill and Tip')

# memberi label pada sumbu x dan y
plt.xlabel('Total Bill')
plt.ylabel('Tip')

# mengatur tata letak warna
sns.set_style('whitegrid')

# menampilkan hasil plot
plt.show()
