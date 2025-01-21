import os # Importa o módulo para manipulação de diretórios e caminhos
import requests # Importa o módulo para realizar requisições HTTP
import argparse # Importa o módulo para análise de argumentos de linha de comando

# Função para baixar o arquivo .gitignore
def baixar_gitignore(tecnologias):
    """Baixa o arquivo .gitignore com base nas tecnologias especificadas."""

    # URL base do serviço Toptal para .gitignore
    url_base = 'https://www.toptal.com/developers/gitignore/api'

    # Concatena as tecnologias separadas por vírgula
    tecnologias_formatadas = ','.join(tecnologias)

    # Constrói a URL completa para a requisição
    url_gitignore = f'{url_base}/{tecnologias_formatadas}'

    try:
        # Informa o usuário que o download do .gitignore está sendo iniciado
        print(f'Baixando .gitignore para as tecnologias: {", ".join(tecnologias)}...')

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
    parser = argparse.ArgumentParser(description='Baixar o arquivo .gitignore para tecnologias específicas.')

    # Define o argumento 'tecnologias', permitindo múltiplos valores
    parser.add_argument('tecnologias', nargs='+', help='Lista de tecnologias para o .gitignore (ex: python node visualstudiocode)')

    # Adiciona o argumento de versão
    parser.add_argument('--version', action='version', version='gitignore 2.0.0', help='Exibe a versão do CLI')

    # Faz a análise dos argumentos passados na linha de comando
    args = parser.parse_args()

    # Chama a função para baixar o .gitignore com as tecnologias informadas
    baixar_gitignore(args.tecnologias)

# Verifica se o script está sendo executado diretamente
if __name__ == '__main__':
    main() # Executa a função main
