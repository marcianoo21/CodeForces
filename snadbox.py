import matplotlib.pyplot as plt

# Dane dla wykresu 1: Produkcja piwa (mln hl)
labels = ['Mahou-San Miguel', 'Damm (Estrella Damm)', 'Heineken España', 'Estrella Galicia']
sizes = [12.81, 11.34, 10.07, 4.81]
percentages = [33, 28, 24, 12]
colors = ['#FF6F61', '#6B7280', '#10B981', '#FBBF24']
explode = (0, 0, 0, 0)  # Brak "eksplozji" segmentów

# Wykres 1: Kołowy
plt.figure(figsize=(8, 6))
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.0f%%', startangle=90)
plt.title('Produkcja piwa w Hiszpanii (mln hl)')
plt.axis('equal')  # Równy okrąg
plt.show()

# Dane dla wykresu 2: Średnie ceny (€, puszka 33 cl)
brands = ['Heineken', 'Mahou 5 Estrellas', 'Estrella Damm']
prices = [0.785, 0.67, 0.69]  # Średnie z przedziałów
colors_bar = ['#10B981', '#FF6F61', '#6B7280']

# Wykres 2: Słupkowy
plt.figure(figsize=(8, 6))
plt.bar(brands, prices, color=colors_bar)
plt.title('Średnie ceny piwa (puszka 33 cl)')
plt.ylabel('Cena (€)')
plt.ylim(0, 1)  # Skala od 0 do 1 dla lepszej czytelności
plt.grid(axis='y', linestyle='--', alpha=0.7)
for i, v in enumerate(prices):
    plt.text(i, v + 0.02, f'€{v:.3f}', ha='center', fontweight='bold')
plt.show()