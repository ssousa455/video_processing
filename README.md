# Video Processing Scripts

Este repositório contém scripts para processar vídeos de maneiras diferentes, dependendo da escolha do usuário. Há scripts tanto em Batch quanto em Python que oferecem as seguintes funcionalidades:

1. Acelerar vídeos em 2x.
2. Compactar vídeos para 720p com crf 25 usando libx265.
3. Acelerar vídeos em 2x e compactar para 720p com crf 25 usando libx265.

## Pré-requisitos

Para o script Python:
- Python 3.x instalado.
- Biblioteca moviepy: `pip install moviepy`.

Para o script Batch:
- ffmpeg instalado e configurado no PATH do sistema.

## Como usar

### Script Python

1. Salve o script `video_processing.py` em seu computador.
2. Abra um terminal ou prompt de comando.
3. Navegue até o diretório onde você salvou `video_processing.py`.
4. Execute o script com o comando `python video_processing.py`.
5. O script solicitará que você escolha uma opção. Digite `1`, `2`, ou `3` e pressione Enter para continuar.

### Script Batch

1. Salve o script `video_processing.bat` em seu computador.
2. Clique duas vezes no script para executá-lo ou abra um prompt de comando e navegue até o diretório onde você salvou `video_processing.bat`, e então digite `video_processing.bat` e pressione Enter.
3. O script solicitará que você escolha uma opção. Digite `1`, `2`, ou `3` e pressione Enter para continuar.

## Funcionalidades

- **Acelerar Vídeos**: A opção 1 acelera todos os vídeos no diretório atual e subdiretórios em 2x.
- **Compactar Vídeos**: A opção 2 compacta todos os vídeos no diretório atual e subdiretórios para 720p usando libx265.
- **Acelerar e Compactar Vídeos**: A opção 3 acelera e compacta todos os vídeos no diretório atual e subdiretórios em 2x e para 720p usando libx265.

Ao final do processamento, o script fornecerá estatísticas sobre quantos arquivos foram processados, quanto tempo levou e em qual diretório o processo foi iniciado.
