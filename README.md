# Utwórz środowisko wirtualne: W terminalu przejdź do katalogu, w którym chcesz utworzyć środowisko wirtualne, a następnie uruchom: -->

python -m venv myenv

# Aktywuj środowisko wirtualne: Na systemie Windows, uruchom: -->

.\myenv\Scripts\activate

# przed instalacją warto sprawdzić

python.exe -m pip install --upgrade pip
pip install --upgrade pip setuptools wheel

# Instalacja pakietu crewai za pomocą pip

pip install crewai
 pip install transformer
pip install torch

# Jeśli napotkasz błąd podczas budowania pakietu chroma-hnswlib, zainstaluj Microsoft Visual C++ Build Tools:

https://visualstudio.microsoft.com/visual-cpp-build-tools/
