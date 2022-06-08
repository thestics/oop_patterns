#!/usr/bin/env python3
# -*-encoding: utf-8-*-
# Author: Danil Kovalenko

import abc


class State:
    
    @staticmethod
    @abc.abstractmethod
    def play(player: "MediaPlayer"):
        pass
    
    @staticmethod
    @abc.abstractmethod
    def pause(player: "MediaPlayer"):
        pass
    
    @staticmethod
    @abc.abstractmethod
    def next(player: "MediaPlayer"):
        pass
    
    @staticmethod
    @abc.abstractmethod
    def prev(player: "MediaPlayer"):
        pass


class NextPrevMixin:
    
    @staticmethod
    def next(player: "MediaPlayer"):
        # do the round-robin as any music player expected
        player.cur_track_num = (player.cur_track_num + 1) % len(player.tracks)
        print(f'Moving forward to {player.tracks[player.cur_track_num]}')

    @staticmethod
    def prev(player: "MediaPlayer"):
        player.cur_track_num = (player.cur_track_num - 1) % len(player.tracks)
        print(f'Moving backward to {player.tracks[player.cur_track_num]}')


class Playing(NextPrevMixin, State):
    
    @staticmethod
    def play(player: "MediaPlayer"):
        pass
    
    @staticmethod
    def pause(player: "MediaPlayer"):
        print(f"Pausing track {player.tracks[player.cur_track_num]}")
        player.state = Paused


class Paused(NextPrevMixin, State):
    
    @staticmethod
    def play(player: "MediaPlayer"):
        print(f"Playing track {player.tracks[player.cur_track_num]}")
        player.state = Playing

    @staticmethod
    def pause(player: "MediaPlayer"):
        pass


class MediaPlayer:
    
    def __init__(self):
        self.tracks = []
        self.state = Paused
        self.cur_track_num = 0
    
    def play(self): return self.state.play(self)
    
    def pause(self): return self.state.pause(self)
    
    def next(self): return self.state.next(self)
    
    def prev(self): return self.state.prev(self)


if __name__ == '__main__':
    p = MediaPlayer()
    p.tracks = ['foo.mp3', 'bar.mp3', 'buzz.mp3']
    p.play()
    p.next()
    p.pause()
    p.next()
    p.next()