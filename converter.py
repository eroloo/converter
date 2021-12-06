import os
import sys
import argparse
import moviepy.editor as mp


def main():
    dbname = os.getcwd()
    my_parser = argparse.ArgumentParser(description="Export music file from video.")

    my_parser.add_argument('--path', '-p',
                           metavar='file',
                           type=str,
                           dest='path',
                           help='Path to video file',
                           )
    my_parser.add_argument('--output', '-o',
                           required=False,
                           metavar='file',
                           default="output.mp3",
                           dest='output',
                           type=str,
                           help="Path of music file to be exported.",
                           )

    my_parser.add_argument('--verbose', '-v',
                           required=False,
                           dest='verbose',
                           const=True,
                           action='store_const',
                           help="Show verbose bar."
                           )

    args = my_parser.parse_args()
    music_path = args.output
    video_path = args.path
    verbose_bool = args.verbose
    
    verbose = 'bar' if verbose_bool else None

    if (not isinstance(music_path, str)) | (not isinstance(video_path, str)):
        raise argparse.ArgumentTypeError("Path\'s must be strings!")

    if video_path[0] == '/':
        video_path = video_path
    else:
        video_path = f"{dbname}/{video_path}"
    if not os.path.isfile(video_path):
        raise Exception("Video file not exists. Please provide a realpath value.")
    my_clip = mp.VideoFileClip(rf"{video_path}")
    try:
        if music_path[0] == "/":  # suppose full path..
            my_clip.audio.write_audiofile(rf"{music_path}", logger=verbose)
        else:
            my_clip.audio.write_audiofile(filename=rf"{dbname}/{music_path}", logger=verbose)
    except ValueError:
        print("Values error. Please provide filenames with extensions.")


if __name__ == '__main__':
    main()
