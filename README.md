# Processamento de Vídeo em Lote

Este script permite que você processe vídeos em lote de acordo com três opções:

1. Acelerar o vídeo
2. Converter o vídeo para 720p (se a resolução for maior que 720p) e aplicar compressão
3. Acelerar o vídeo, converter para 720p (se a resolução for maior que 720p) e aplicar compressão

## Pré-requisitos

- Python 3.x
- FFmpeg

## Como instalar o FFmpeg

1. Baixe o FFmpeg do [site oficial](https://www.ffmpeg.org/download.html).
2. Extraia o conteúdo do arquivo zip para um diretório de sua escolha, por exemplo, `C:\path\ffmpeg`.
3. Adicione `C:\path\ffmpeg\bin` às variáveis de ambiente do sistema.

## Como executar o script

1. Coloque o script `video_processing.py` na pasta contendo os vídeos que você deseja processar.
2. Abra um prompt de comando ou terminal e navegue até a pasta contendo o script e os vídeos.
3. Execute o script com o comando `python video_processing.py`.
4. Selecione a opção desejada (1, 2 ou 3) conforme as instruções exibidas no prompt de comando ou terminal.

## Bibliotecas Python necessárias

Instale as bibliotecas Python necessárias com o comando:


\`bash
pip install ffmpeg-python 
\`

## Observações

    O script processará todos os vídeos na pasta atual e em suas subpastas.
    O script cria novos arquivos de vídeo com sufixos específicos (_accelerated, _cvt720p, _accelerated_cvt720p) para indicar as operações realizadas em cada vídeo.
    Certifique-se de ter espaço suficiente no disco para os novos arquivos de vídeo gerados.
