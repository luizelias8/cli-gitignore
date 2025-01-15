import os # Importa o módulo para manipulação de diretórios e caminhos
import requests # Importa o módulo para realizar requisições HTTP
import argparse # Importa o módulo para análise de argumentos de linha de comando

# Função para baixar o arquivo .gitignore
def baixar_gitignore(linguagem):
    """Baixa o arquivo .gitignore da linguagem especificada."""

    # Definir a URL base do repositório no GitHub onde os .gitignore estão armazenados
    url_base = 'https://raw.githubusercontent.com/github/gitignore/main'

    # Construir a URL completa do arquivo .gitignore para a linguagem especificada
    url_gitignore = f'{url_base}/{linguagem.capitalize()}.gitignore' # Capitaliza a primeira letra da linguagem

    try:
        # Informa o usuário que o download do .gitignore está sendo iniciado
        print(f'Baixando .gitignore para a linguagem: {linguagem}...')

        # Realiza a requisição HTTP GET para obter o conteúdo do arquivo .gitignore
        resposta = requests.get(url_gitignore)

        # Verifica se a requisição foi bem-sucedida (status code 200)
        resposta.raise_for_status()

        # Define o caminho do arquivo .gitignore a ser salvo no diretório atual
        caminho_arquivo = os.path.join(os.getcwd(), '.gitignore')

        # Abre o arquivo para escrita no diretório atual e salva o conteúdo
        with open(caminho_arquivo, 'w') as arquivo:
            arquivo.write(resposta.text)

        # Informa o sucesso do salvamento do arquivo .gitignore
        print(f'.gitignore salvo com sucesso em: {caminho_arquivo}')

    # Trata erros específicos de resposta HTTP
    except requests.exceptions.HTTPError as erro_http:
        print(f'Erro ao baixar o arquivo .gitignore: {erro_http}')

     # Trata erros gerais, como problemas de conexão ou leitura do arquivo
    except Exception as erro:
        print(f'Ocorreu um erro: {erro}')

# Função principal para analisar os argumentos da linha de comando
def main():
    # Cria o analisador de argumentos (parser)
    parser = argparse.ArgumentParser(description='Baixar o arquivo .gitignore para uma linguagem específica.')

    # Define o argumento 'linguagem', que especifica o nome da linguagem para o .gitignore
    parser.add_argument('linguagem', help='Nome da linguagem para o .gitignore (ex: Python, Node, etc.)')

    # Adiciona o argumento de versão
    parser.add_argument('--version', action='version', version='gitignore 1.0.0', help='Exibe a versão do CLI')

    # Faz a análise dos argumentos passados na linha de comando
    args = parser.parse_args()

    # Chama a função para baixar o .gitignore utilizando a linguagem informada
    baixar_gitignore(args.linguagem)

# Verifica se o script está sendo executado diretamente
if __name__ == '__main__':
    main() # Executa a função main