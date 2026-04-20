# ⚽ Football Analysis System with Computer Vision

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![YOLOv8](https://img.shields.io/badge/YOLOv8-Object%20Detection-green)
![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-red)
![Machine Learning](https://img.shields.io/badge/Sklearn-KMeans%20Clustering-orange)

## 📖 O projekcie

**Football Analysis System** to zaawansowane narzędzie oparte na uczeniu maszynowym i wizji komputerowej, służące do automatycznej analizy meczów piłkarskich. System przetwarza surowy materiał wideo, aby wykrywać i śledzić graczy, sędziów oraz piłkę, a następnie generuje zaawansowane statystyki i wizualizacje taktyczne.

Projekt rozwiązuje problem przekształcania nieustrukturyzowanych danych wideo w ustrukturyzowane dane analityczne, wykorzystując techniki takie jak **Object Detection**, **Optical Flow**, **Homography Transformation** oraz **Clustering**.

## 🚀 Główne funkcjonalności

* **Wykrywanie i śledzenie obiektów:** Wykorzystanie modelu **YOLOv8** oraz algorytmu **ByteTrack** do precyzyjnego śledzenia graczy, bramkarzy, sędziów i piłki.
* **Estymacja ruchu kamery:** Stabilizacja obrazu i kompensacja ruchu kamery przy użyciu **Optical Flow (Lucas-Kanade)**, co pozwala na dokładne określenie pozycji graczy względem boiska.
* **Transformacja perspektywy (Homografia):** Mapowanie pikseli z wideo na rzeczywiste współrzędne boiska (2D) przy użyciu wykrywania punktów kluczowych boiska.
* **Przydział drużyn:** Automatyczne klasyfikowanie graczy do drużyn na podstawie kolorów koszulek przy użyciu algorytmu **K-Means Clustering**.
* **Analiza posiadania piłki:** Logika określająca, który gracz i która drużyna kontroluje piłkę w danej klatce.
* **Statystyki fizyczne:** Obliczanie przebytego dystansu oraz prędkości graczy w czasie rzeczywistym.
* **Wizualizacje taktyczne:**
    * **Mapa 2D boiska:** Odzwierciedlenie pozycji graczy na wirtualnym boisku.
    * **Diagram Woronoja:** Analiza kontroli przestrzeni przez poszczególne drużyny.

## 📊 Przykładowe wizualizacje

| Analiza Wideo (Tracking + Statystyki) | Diagram Woronoja (Kontrola Przestrzeni) |
| :---: | :---: |
| ![Tracking Animation](assets/output_videos.gif) | ![Voronoi Animation](assets/voronoi_diagram.gif) |

## 🛠️ Technologie i Biblioteki

Projekt został zrealizowany w języku **Python** z wykorzystaniem wiodących bibliotek Data Science i Computer Vision:

* **Ultralytics YOLO:** Detekcja obiektów.
* **Supervision:** Obsługa annotacji i śledzenia obiektów.
* **OpenCV:** Przetwarzanie obrazu, operacje morfologiczne, transformacje geometryczne.
* **Roboflow:** Pobieranie modelu do detekcji punktów kluczowych boiska.
* **Scikit-learn:** Klasteryzacja kolorów (K-Means).
* **NumPy & Pandas:** Obliczenia numeryczne i analiza danych.

## ⚙️ Jak to działa? (Pipeline)

1.  **Ingestia Wideo:** Wczytanie materiału źródłowego.
2.  **Detekcja i Tracking:** Wykrycie obiektów w każdej klatce i nadanie im unikalnych ID.
3.  **Ekstrakcja Cech:** Pobranie kolorów strojów i przypisanie graczy do drużyn.
4.  **Korekcja Ruchu:** Obliczenie przesunięcia kamery i dostosowanie pozycji obiektów.
5.  **Transformacja:** Przekształcenie widoku z kamery na płaski model boiska (Bird's Eye View).
6.  **Analiza:** Obliczenie prędkości, dystansu i posiadania piłki.
7.  **Rendering:** Generowanie wyjściowych plików wideo z nałożonymi warstwami analitycznymi.

## Roboflow API

Projekt korzysta z modelu Roboflow do wykrywania punktów kluczowych boiska.
Klucz API powinien być ustawiony lokalnie, a nie wpisany na sztywno w kodzie.

1. Skopiuj `.env.example` do `.env`.
2. Ustaw `ROBOFLOW_API_KEY` w pliku `.env` albo w zmiennych środowiskowych.
3. Uruchom projekt lub notebook ponownie.

Przykład:

```bash
ROBOFLOW_API_KEY=your_roboflow_api_key_here
```

## 📂 Struktura Projektu

```bash
Football-Players-Detection/
├── camera_movement_estimator/ # Moduł estymacji ruchu kamery
├── development_and_analysis/  # Notebooki Jupyter (eksperymenty)
├── homography_transformer/    # Transformacja perspektywy na współrzędne boiska
├── models/                    # Wagi modeli YOLO
├── output_videos/             # Wygenerowane wizualizacje
├── pitch_visualization/       # Rysowanie mapy 2D i diagramów Woronoja
├── player_ball_assigner/      # Logika przypisania piłki do gracza
├── speed_and_distance_estimator/ # Obliczanie metryk fizycznych
├── stubs/                     # Pliki cache (pickle) dla przyspieszenia działania
├── team_assigner/             # Klastrowanie kolorów drużyn
├── trackers/                  # Wrapper na YOLO i ByteTrack
├── utils/                     # Funkcje pomocnicze
├── view_transformer/          # Prosta transformacja perspektywy
├── voronoi_diagram/           # Generator diagramów przestrzennych
└── main.py                    # Główny skrypt uruchomieniowy
