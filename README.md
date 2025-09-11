## Welding Defect Detection (OpenCV)

Projeto de visão computacional baseado em OpenCV para apoiar a identificação de defeitos em solda em cilindros. O repositório contém utilitários com OpenCV e um conjunto de dados anotado em formato YOLO para experimentos.

### Estrutura
- `src/experiments/utils/open_cv_helper.py`: utilidades com OpenCV.
- `src/datasets/welding_detect_dataset/`: dataset com `train/`, `valid/`, `test/` em formato YOLO (`images/` e `labels/`) e `data.yaml`.
- `requirements.txt`: dependências principais (OpenCV e NumPy).

### Requisitos
- Python 3.9+ (recomendado 3.11)
- Pip recente (`python -m pip install --upgrade pip`)

## Configurando ambiente virtual (venv)

Instalar dependências em um ambiente virtual evita conflitos entre projetos. Abaixo, passos para Ubuntu/Linux, Windows e macOS. Após ativar o ambiente, instale as dependências com `pip install -r requirements.txt`.

### Ubuntu / Linux
```bash
# Na raiz do projeto
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt

# Desativar quando terminar
deactivate
```

### Windows (PowerShell)
```powershell
# Na raiz do projeto
py -3 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt

# Caso a execução de scripts esteja bloqueada (rode como Admin uma vez):
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# Desativar
deactivate
```

### Windows (CMD)
```bat
:: Na raiz do projeto
py -3 -m venv .venv
.\.venv\Scripts\activate.bat
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### macOS (Intel/Apple Silicon)
```bash
# Na raiz do projeto
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### Dica para WSL (Windows Subsystem for Linux)
Se estiver usando WSL, siga as instruções de Ubuntu/Linux dentro do terminal WSL. Para acessar arquivos do Windows no WSL, navegue até `/mnt/c/Users/<seu-usuario>/...`.

## Verificando a instalação do OpenCV
Com o ambiente ativado, execute:
```bash
python -c "import cv2, numpy as np; print('OpenCV:', cv2.__version__); img = np.zeros((100,100,3), dtype=np.uint8); print('OK' if img.shape==(100,100,3) else 'NOK')"
```
Saída esperada inclui a versão do OpenCV e `OK`.

## Próximos passos
- Explore `open_cv_helper.py` para exemplos utilitários.
- Use o dataset em `src/datasets/welding_detect_dataset/` para treinos/validações.

## Licença
Defina aqui a licença do projeto (por exemplo, MIT). 
