import moviepy.editor as mp
import os
import time

def process_videos(choice):
    start_time = time.time()
    file_count = 0
    initial_dir = os.getcwd()

    for root, dirs, files in os.walk(initial_dir):
        for file in files:
            if file.endswith(('.mp4', '.ts', '.mkv', '.avi')):
                file_path = os.path.join(root, file)

                # Verifique se o arquivo já foi processado
                if choice == '1' and '_accelerated' in file:
                    continue
                elif choice == '2' and '_cvt720p' in file:
                    continue
                elif choice == '3' and '_accelerated_cvt720p' in file:
                    continue

                video = mp.VideoFileClip(file_path)
                file_count += 1

                if choice == '1':
                    new_file = file_path.replace('.', '_accelerated.')
                    video_speedup = video.fx(mp.vfx.speedx, 2)
                    video_speedup.write_videofile(new_file, codec='libx265', threads=4)

                elif choice == '2':
                    new_file = file_path.replace('.', '_cvt720p.')
                    if video.h > 720:
                        video_resized = video.resize(height=720)
                    else:
                        video_resized = video
                    video_resized.write_videofile(new_file, codec='libx265', threads=4)

                elif choice == '3':
                    new_file = file_path.replace('.', '_accelerated_cvt720p.')
                    video_speedup = video.fx(mp.vfx.speedx, 2)
                    if video.h > 720:
                        video_resized = video_speedup.resize(height=720)
                    else:
                        video_resized = video_speedup
                    video_resized.write_videofile(new_file, codec='libx265', threads=4)

    elapsed_time = time.time() - start_time
    hours, rem = divmod(elapsed_time, 3600)
    minutes, seconds = divmod(rem, 60)

    print(f'Processo concluído.')
    print(f'Arquivos processados: {file_count}')
    print(f'Tempo decorrido: {int(hours)} hora(s), {int(minutes)} minuto(s) e {int(seconds)} segundo(s)')
    print(f'Diretório inicial: {initial_dir}')

if __name__ == '__main__':
    choice = input('Selecione uma opção:\n1 - Acelerar vídeos em 2x\n2 - Compactar em 720p, crf 25 e libx265\n3 - Acelerar e compactar em 720p, crf 25 e libx265\n')
    process_videos(choice)
