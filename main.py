import random
import os

from art import text2art

from moviepy.editor import (
    AudioFileClip, VideoFileClip, concatenate_audioclips, concatenate_videoclips, CompositeAudioClip
)


class VidioMaker:
    """
    Класс для составления видио клипа.
    """

    VIDIO_DURATION_IN_SECONDS = 2

    def __init__(self, path_vidio1, path_vidio2, path_audio):
        self.__path_vidio1 = path_vidio1
        self.__path_vidio2 = path_vidio2
        self.__path_audio = path_audio

    def __get_audio_file(self) -> AudioFileClip:
        """
        Возвращает аудио клип состоящий из музыки в папке с аудио.
        """

        audio_list = os.listdir(self.__path_audio)
        all_audios = []

        while audio_list:
            all_audios.append(AudioFileClip(
                os.path.join(self.__path_audio, audio_list.pop()))
            )

        final_audio = concatenate_audioclips(all_audios)
        return final_audio

    def __get_first_video_file(self) -> VideoFileClip:
        """
        Возвращает первый видиоклип.
        """

        first_video_list = os.listdir(self.__path_vidio1)
        first_video_file = VideoFileClip(
            os.path.join(self.__path_vidio1, random.choice(first_video_list))
        )
        return first_video_file

    def __get_second_video_file(self) -> VideoFileClip:
        """
        Возвращает второй видиоклип.
        """

        second_video_list = os.listdir(self.__path_vidio2)
        second_video_file = VideoFileClip(
            os.path.join(self.__path_vidio2, random.choice(second_video_list))
        )
        return second_video_file

    def wright_new_vidio(self) -> None:
        """
        Записывает новое видио с названием 'New_vidio.mp4'
        """

        try:
            audio = CompositeAudioClip([self.__get_audio_file()])
            first_vidio = self.__get_first_video_file()
            second_vidio = self.__get_second_video_file()

            final_vidio = concatenate_videoclips([first_vidio, second_vidio])
            final_vidio.audio = audio

            final_vidio = final_vidio.subclip(0, self.VIDIO_DURATION_IN_SECONDS)
            final_vidio.write_videofile('New_vidio.mp4')

            print(text2art('Success'))
        except Exception as ex:
            print('что то пошло не так...\n', ex)


def main():
    print(text2art('Vidio Maker\n'))
    vidio1 = input('Напишете путь до первой папки с видио\n')
    vidio2 = input('Напишете путь до второй папки с видио\n')
    auduo = input('Напишете путь до папки с аудио\n')
    vidiomaker = VidioMaker(
        path_vidio1=vidio1,
        path_vidio2=vidio2,
        path_audio=auduo,
    )
    vidiomaker.wright_new_vidio()


if __name__ == "__main__":
    main()
