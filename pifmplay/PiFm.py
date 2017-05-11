#!/usr/bin/python

from subprocess import call


def play_sound( filename ):
   call(["./fm_transmitter", filename])
   return