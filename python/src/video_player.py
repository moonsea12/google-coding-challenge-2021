"""A video player class."""

from .video_library import VideoLibrary
import numpy as np
from random import randint

currently_playing = "no_music"



class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        self._video_library = VideoLibrary()
        self.isPlaying = False
        self.currentlyPlaying = None
        self.isPaused = False
        self.libraryPlaylists = {}

    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        """Returns all videos."""

        """This command will list all available videos in the format:
        “title (video_id) [tags]”. The videos should be shown in lexicographical
        order by title. If there are no tags available, display empty brackets.
        """

        print("Here's a list of all available videos:")
        array = []
        array = self._video_library.get_all_videos()
        array.sort(key=lambda x: x.title)
        for i in range(len(array)):
            print("{0} ({1}) [{2}]".format(array[i].title, array[i].video_id, ' '.join(map(str, list(array[i].tags)))))

    def play_video(self, video_id):
        """Plays the respective video.

        Args:
            video_id: The video_id to be played.
        """

        """Play the specified video. If a video is currently playing, display a
        note that this video will be stopped, even if the same video is already
        playing. If the video doesn’t exist, display a warning message
        (and don’t stop the currently playing video)."""

        video = self._video_library.get_video(video_id)
        try:
            video_title = video.title
            if self.isPlaying == True or self.isPaused == True:
                print("Stopping video: " + self.currentlyPlaying)
            print("Playing video: " + video_title)
            self.currentlyPlaying = video_title
            self.isPlaying = True
            self.isPaused = False
        except:
            print("Cannot play video: Video does not exist")

    def stop_video(self):
        """Stop the current playing video. If no video is currently playing,
        display a warning message “Cannot stop video: No video is currently
        playing” and do nothing."""

        if self.isPlaying == False and self.isPaused == False:
            print("Cannot stop video: No video is currently playing")
        else:
            print("Stopping video: " + self.currentlyPlaying)
            self.isPlaying = False
            self.isPaused = False

    def play_random_video(self):
        """Plays a random video from the video library."""

        """Play a random video. If a video is currently playing, display a note
        that this video will be stopped, even if the same video is already
        playing."""

        try:
            list_videos = self._video_library.get_all_videos()
            random_index = randint(0, len(list_videos)-1)
            video_title = list_videos[random_index].title
            if self.isPlaying == True:
                print("Stopping video: " + self.currentlyPlaying)
            print("Playing video: " + video_title)
            self.currentlyPlaying = video_title
            self.isPlaying = True
            self.isPaused = False
        except:
            print("No videos available.")

    def pause_video(self):
        """Pauses the current video."""

        try:
            if self.isPaused == True:
                print("Video already paused: " + self.currentlyPlaying)
            elif self.isPlaying == True:
                print("Pausing video: " + self.currentlyPlaying)
                self.isPlaying = False
                self.isPaused = True
            else:
                print("Cannot pause video: No video is currently playing")
        except:
            print("Error")

    def continue_video(self):
        """Resumes playing the current video."""

        try:
            if self.isPaused == True:
                print("Continuing video: " + self.currentlyPlaying)
                self.isPaused = False
                self.isPlaying = True
            elif self.isPlaying == False:
                print("Cannot continue video: No video is currently playing")
            elif self.isPaused == False:
                print("Cannot continue video: Video is not paused")
        except:
            print("Error")

    def show_playing(self):
        """Displays video currently playing."""

        video = None
        array = []
        array = self._video_library.get_all_videos()
        for i in range(len(array)):
            if array[i].title == self.currentlyPlaying:
                video = self._video_library.get_video(array[i].video_id)


        if self.isPaused == True:
            print("Currently playing: {0} ({1}) [{2}] - PAUSED".format(video.title, video.video_id, ' '.join(map(str, list(video.tags)))))
        elif self.isPlaying == False and self.isPaused == False:
            print("No video is currently playing")
        else:
            print("Currently playing: {0} ({1}) [{2}]".format(video.title, video.video_id, ' '.join(map(str, list(video.tags)))))


    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """

        try:
            if len(self.libraryPlaylists) == 0:
                self.libraryPlaylists[playlist_name] = []
                print("Successfully created new playlist: " + playlist_name)
            else:
                dic_lower = [k.lower() for k in self.libraryPlaylists.keys()]
                if playlist_name.lower() in dic_lower:
                    print("Cannot create playlist: A playlist with the same name already exists")
                else:
                    self.libraryPlaylists[playlist_name] = []
                    print("Successfully created new playlist: " + playlist_name)
        except:
            print("Error")

    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """

        """
            if playlist does not exist than display the # WARNING:
            if the video does not exist than display the # WARNING:
            elif check if the video is already in the playlist
                if the video is in the playlist
                    display the # WARNING:
                else
                    add the video
        """

        """Do I need return in each if statement?"""
        try:
            video = self._video_library.get_video(video_id)

            if len(self.libraryPlaylists) == 0:
                print(f"Cannot add video to {playlist_name}: Playlist does not exist")
                return
            else:
                library_playlists_lower = {k.lower():v for k, v in self.libraryPlaylists.items()}
                if playlist_name.lower() not in library_playlists_lower:
                    print(f"Cannot add video to {playlist_name}: Playlist does not exist")
                    return

            if not video:
                print(f"Cannot add video to {playlist_name}: Video does not exist")
                return

            vids = library_playlists_lower[playlist_name.lower()]

            if video_id in vids:
                print(f"Cannot add video to {playlist_name}: Video already added")
                return
            else:
                for name in self.libraryPlaylists.keys():
                    if name.lower() == playlist_name.lower():
                        self.libraryPlaylists[name].append(video_id)
                        print(f"Added video to {playlist_name}: {video.title}")
        except:
            print("Error")

    def show_all_playlists(self):
        """Display all playlists."""

        if not len(self.libraryPlaylists):
            print("No playlists exist yet")
        else:
            playlists = list(self.libraryPlaylists.keys())

            print("")
            print("Showing all playlists:")
            print("\t{}".format(*sorted(playlists)))
            print("")

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """

        """Checking if I can make changes to code and push it to GitHub"""
        print("show_playlist needs implementation")

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        print("remove_from_playlist needs implementation")

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("clears_playlist needs implementation")

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("deletes_playlist needs implementation")

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        print("search_videos needs implementation")

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        print("search_videos_tag needs implementation")

    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        print("flag_video needs implementation")

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        print("allow_video needs implementation")
