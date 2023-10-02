import os
import time
import ffmpeg
from multiprocessing import Pool, cpu_count

def process_video(args):
    file, root, option = args
    input_path = os.path.join(root, file)
    output_suffix = ""

    probe = ffmpeg.probe(input_path)
    video_stream = next(stream for stream in probe['streams'] if stream['codec_type'] == 'video')
    height = video_stream['height']

    vf_filter = ''
    af_filter = ''

    if option == '1' or option == '3':
        vf_filter = 'setpts=0.5*PTS'
        af_filter = 'atempo=2'
        output_suffix = "_accelerated"

    if (option == '2' or option == '3') and height >= 1080:
        vf_filter = f'{vf_filter},scale=-1:720' if vf_filter else 'scale=-1:720'
        output_suffix = f'{output_suffix}_cvt720p' if output_suffix else '_cvt720p'

    filter_complex = f'{vf_filter};{af_filter}'

    ffmpeg.input(input_path).output(
        input_path.replace('.mp4', f'{output_suffix}.mp4'),
        filter_complex=filter_complex,
        vcodec='libx265',
        preset='ultrafast',
        crf='25',
        acodec='aac',
        ab='128k',
        threads='4'
    ).overwrite_output().run()

if __name__ == '__main__':
    try:
        choice = input("Escolha uma opção (1, 2 ou 3):\n"
                       "1. Acelerar vídeos\n"
                       "2. Converter vídeos para 720p\n"
                       "3. Acelerar e converter vídeos para 720p\n"
                       "Opção: ")

        if choice not in ['1', '2', '3']:
            print("Opção inválida. Por favor, escolha novamente.")
        else:
            start_time = time.time()
            base_path = os.getcwd()
            all_files = []
            for root, dirs, files in os.walk(base_path):
                for file in files:
                    if file.endswith(".mp4"):
                        all_files.append((file, root, choice))

            # Use 75% dos cores disponíveis para evitar sobrecarregar o sistema
            with Pool(int(cpu_count() * 0.75)) as pool:
                pool.map(process_video, all_files)

            end_time = time.time()
            elapsed_time = end_time - start_time
            processed_files = len(all_files)

            print(f"Processamento concluído. {processed_files} arquivos processados em {elapsed_time:.2f} segundos.")
            print(f"Processo iniciado na pasta: {base_path}")
    finally:
        # Isso garantirá que a pool seja fechada e todos os recursos sejam liberados após a conclusão
        pool.close()
        pool.join()
