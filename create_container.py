import os


class Container:
    # Define the class variables
    def __init__(self, file, short, mono, lowrate, subs, out_name):
        self.file = file
        self.short = short
        self.mono = mono
        self.lowrate = lowrate
        self.sub = subs
        self.video = out_name

    # Export all the videos, audio files we will be using to create the container.
    def export(self):
        os.system("ffmpeg -ss 00:00:00 -i " + self.file + " -to 00:01:00 -c copy " + self.short)
        os.system("ffmpeg -i " + self.file + " -ss 00:00:00 -to 00:01:00 -c copy " + self.short)
        os.system("ffmpeg -i " + self.short + " -ab 192k " + self.lowrate)
        os.system("ffmpeg -i " + self.short + " -ss 00:00:00 -t 00:01:00 -map 0:a:0 -ac 1 " + self.mono)

    # Create the subtitled video.
    def subtitled(self):
        out = "subtitled.mp4"
        os.system("ffmpeg -i " + self.short + " -vf subtitles=" + self.sub + " subtitled.mp4")

    # Create the video container. 
    def create_new_container(self):
        self.export()
        os.system("ffmpeg -i " + self.mono + " -i " + self.lowrate + " -i " + self.short + " -i " + self.sub +
                  " -ss 00:00:00 -t 00:01:00 -map 0:a:0 -map 1:a:0 -map 2:v:0 -c:v copy -map 3:s:0 -c:s mov_text "
                  + self.video)

    # Create the function that cheks which codecs are using the container, and whit whom is compatible.
    def compatibility(self):
        # Create codec lists.
        dv3_video = ["mpeg", "h264"]
        dv3_audio = ["aac", "ac3"]
        isdb_astc_video = ["mpeg", "h264"]
        isdb_astc_audio = ["aac"]
        dtmb_video = ["avs", "avs+", "mpeg", "h264"]
        dtmb_audio = ["dra", "aac", "ac3", "mp2", "mp3"]
        # Get the audio and video codecs from the command line.
        video_codec = os.popen("ffprobe -v error -select_streams v:0 -show_entries stream=codec_name -of "
                               "default=noprint_wrappers=1:nokey=1 " + self.video).read()

        audio_codec = os.popen("ffprobe -v error -select_streams a:0 -show_entries stream=codec_name -of "
                               "default=noprint_wrappers=1:nokey=1 " + self.video).read()
        # Print the codecs the container is using.
        print('Containers: '+str(video_codec)[:len(video_codec) - 1], str(audio_codec)[:len(audio_codec) - 1])
        # Check out whit whom is compatible.
        if str(video_codec)[:len(video_codec) - 1] in dtmb_video and str(audio_codec)[
                                                                     :len(audio_codec) - 1] in dtmb_audio:
            print("The container is compatible with DTMB\n")
            if video_codec in dv3_video and audio_codec in dv3_audio:
                print("The container is also compatible with DV3\n")
                if video_codec in isdb_astc_video and audio_codec in isdb_astc_audio:
                    print("The container is also compatible with ISDB and ATSC!\n")
        else:
            print("Error 404, no video codec compatibility found")

    def test(self):

        self.export()
        self.subtitled()
        self.compatibility()

def app():
    in_video = "BBB.mp4"
    short = "BBB_short.mp4"
    mono = "mono_audio_BBB.mp3"
    low_bit = "lowbit_audio_BBB.mp3"
    subs = "subtitles.srt"
    out_name = "new_video.mp4"

    new_video = Container(in_video, short, mono, low_bit, subs, out_name)
    # new_video.create_new_container()
    # new_video.compatibility()
    new_video.test()

if __name__ == '__main__':
    app()
