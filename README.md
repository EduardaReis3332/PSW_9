# Passo a Passo

### Aqui está uma explicação simples, passo a passo de como configurar o ambiente para criar o projeto:

## 1. Criar o Ambiente Virtual

Antes de começar a trabalhar com Django, é importante criar um ambiente virtual. Esse ambiente separa as bibliotecas do seu projeto, evitando conflitos com outras instalações no sistema.

- No **Linux**, usamos o comando:
  ```bash
  python3 -m venv venv
  ```
- No **Windows**, usamos:
  ```bash
  python -m venv venv
  ```

## 2. Ativar o Ambiente Virtual

Depois de criar o ambiente, é preciso ativá-lo para usar as bibliotecas específicas dele.

- No **Linux**, ativamos assim:
  ```bash
  source venv/bin/activate
  ```
- No **Windows**, ativamos assim:
  ```bash
  venv\Scripts\Activate
  ```

## 3. Corrigir Erros de Permissão (Windows)

Caso ocorra algum erro de permissão ao ativar o ambiente virtual no Windows, você pode rodar o comando abaixo para resolver o problema:
```bash
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
```

## 4. Instalar Django e Bibliotecas

Agora que o ambiente está ativo, podemos instalar as bibliotecas necessárias para o projeto. Usamos o comando `pip` para instalar o Django e outras bibliotecas, como o **Pillow** (usada para trabalhar com imagens):
```bash
pip install django
pip install pillow
```

## Rodar o Servidor
```bash
python manage.py runserver
```

Com isso, o ambiente está pronto para iniciar o desenvolvimento com Django!