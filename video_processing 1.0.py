import os
import time
import ffmpeg

def process_videos(option):
    start_time = time.time()
    processed_files = 0
    base_path = os.getcwd()

    for root, dirs, files in os.walk(base_path):
        for file in files:
            if file.endswith(".mp4"):
                input_path = os.path.join(root, file)
                output_suffix = ""

                if option == '1':
                    output_suffix = "_accelerated"
                    ffmpeg.input(input_path).output(
                        input_path.replace('.mp4', f'{output_suffix}.mp4'),
                        vf='setpts=0.5*PTS',
                        af='atempo=2',
                        vcodec='libx265',
                        preset='ultrafast',
                        crf='25',
                        acodec='aac',
                        ab='128k',
                        threads='4'
                    ).overwrite_output().run()
                    processed_files += 1

                elif option == '2':
                    output_suffix = "_cvt720p"
                    ffmpeg.input(input_path).output(
                        input_path.replace('.mp4', f'{output_suffix}.mp4'),
                        vf='scale=-1:720',
                        vcodec='libx265',
                        preset='ultrafast',
                        crf='25',
                        acodec='aac',
                        ab='128k',
                        threads='4'
                    ).overwrite_output().run()
                    processed_files += 1

                elif option == '3':
                    output_suffix = "_accelerated_cvt720p"
                    temp_output = input_path.replace('.mp4', '_temp_accelerated.mp4')
                    ffmpeg.input(input_path).output(
                        temp_output,
                        vf='setpts=0.5*PTS',
                        af='atempo=2',
                        vcodec='libx265',
                        preset='ultrafast',
                        crf='25',
                        acodec='aac',
                        ab='128k',
                        threads='4'
                    ).overwrite_output().run()

                    ffmpeg.input(temp_output).output(
                        input_path.replace('.mp4', f'{output_suffix}.mp4'),
                        vf='scale=-1:720',
                        vcodec='libx265',
                        preset='ultrafast',
                        crf='25',
                        acodec='aac',
                        ab='128k',
                        threads='4'
                    ).overwrite_output().run()
                    os.remove(temp_output)
                    processed_files += 1

    end_time = time.time()
    elapsed_time = end_time - start_time

    print(f"Processamento concluído. {processed_files} arquivos processados em {elapsed_time:.2f} segundos.")
    print(f"Processo iniciado na pasta: {base_path}")

if __name__ == '__main__':
    choice = input("Escolha uma opção (1, 2 ou 3):\n"
                   "1. Acelerar vídeos\n"
                   "2. Converter vídeos para 720p\n"
                   "3. Acelerar e converter vídeos para 720p\n"
                   "Opção: ")

    if choice not in ['1', '2', '3']:
        print("Opção inválida. Por favor, escolha novamente.")
    else:
        process_videos(choice)
