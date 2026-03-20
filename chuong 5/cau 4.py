import pandas as pd
import matplotlib.pyplot as plt
data = {
    'city': ['Los Angeles', 'San Diego', 'San Jose', 'San Francisco', 'Fresno',
             'Sacramento', 'Long Beach', 'Oakland', 'Bakersfield', 'Anaheim'],
    'area_total_km2': [1302, 964, 469, 600, 298, 259, 133, 202, 389, 131]
}
df = pd.DataFrame(data)
df = df.sort_values(by='area_total_km2', ascending=False)
plt.barh(df['city'], df['area_total_km2'], color='orange')
plt.xlabel('Diện tích (km²)')
plt.ylabel('Thành phố')
plt.title('Top 10 thành phố lớn nhất California theo diện tích')
plt.gca().invert_yaxis()
plt.show()