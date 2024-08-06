# C0DEX SECURITY

## Descrição

O C0dex Security é uma ferramenta que utiliza a API do VirusTotal para verificar a segurança de URLs. Ele oferece uma interface gráfica simples usando Tkinter, onde os usuários podem inserir uma URL e receber informações sobre possíveis ameaças.

## Funcionalidades

- Verificação de URLs usando a API do VirusTotal.
- Interface gráfica amigável com Tkinter.

## Pré-requisitos

- Python 3.x
- Bibliotecas Python: `requests`, `tkinter`
- Chaves de API do VirusTotal

## Instalação

1. Clone o repositório:

   ```sh
   git clone https://github.com/kayquec0dex/codex-security.git
   cd codex-security
   ```

2. Instale as dependências:

   ```sh
   pip install requests
   pip install tkinter
   ```

3. Adicione suas chaves de API ao arquivo `config.json`:

   ```json
   {
     "API_KEY_VIRUSTOTAL": "SUA_API_KEY_VIRUSTOTAL"
   }
   ```

## Uso

1. Execute o script principal:

   ```sh
   python main.py
   ```

2. Digite a URL que deseja verificar na interface gráfica e clique em "Verificar".

## Estrutura do Projeto

```plaintext
codex-security/
│
├── config.json
├── icon.png
├── main.py
└── README.md
```
