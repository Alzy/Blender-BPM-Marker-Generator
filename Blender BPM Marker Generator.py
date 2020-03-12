# BeatMarkers by tumtidum
# Updated for use in Blender 2.83 by alzy

# This script places Markers on the Timeline based on the given Beats Per
# Minute and the current Frame Rate settings. The Markers will be placed
# from the Start to the End of the Playback/Rendering Range.

# NOTE. Markers can only be placed on whole frames (integers), thus when
# a beat's target falls in between frames the nearest frame will be chosen
# to place the marker.
import bpy

# Set the desired BPM value here (min. 1 max. 500). Then Run the script.
bpm = 119

# You can change the beat count here. For example with a value of 4 the
# Markers will be named as such; B1, B2, B3, B4, B1, B2, B3, B4, etc..
count = 4

# Set clear_markers to 1 if you want to remove all current Markers from
# the timeline, if you want to keep them set it to 0.
clear_markers = 1


# Don't modify any of the following code..
scene = bpy.context.scene
# Get current play-head position.
default_frame = scene.frame_current
# Set both the current frame and target to first frame of range.
scene.frame_current = scene.frame_start
target = scene.frame_start

# Check for a valid Beats Per Minute entry.
if 500 >= bpm and bpm >= 1:
    print("---")
    # Calculate the amount of Frames Per Beat and output the value to console.
    fpb = (1 / (bpm / 60)) * scene.render.fps
    print("Frames Per Beat:", fpb)

    # Check whether to clear all current Markers or not.
    if clear_markers == 1:
        scene.timeline_markers.clear()

    # Place markers until the end of the play range.
    counter = 1
    while target <= scene.frame_end:
        scene.timeline_markers.new("B" + str(counter), frame=round(target))
        target = target + fpb
        if counter < count:
            counter = counter + 1
        else:
            counter = 1

else:
    print("No valid BPM value... (min. 1 max. 500)")

# Put back the play-head to it's original position.
scene.frame_current = default_frame
print("+++")
