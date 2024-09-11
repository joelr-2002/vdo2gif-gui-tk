#!/usr/bin/env python3
import argparse
from moviepy.editor import VideoFileClip, sys
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image

def main():
    root = tk.Tk()
    root.title("Video to GIF Converter")

    def browse_input():
        input_path.set(filedialog.askopenfilename(filetypes=[("Video files", "*.mp4;*.avi;*.mov")]))

    def browse_output():
        output_path.set(filedialog.asksaveasfilename(defaultextension=".gif", filetypes=[("GIF files", "*.gif")]))

    def convert_video():
        inputdir = input_path.get()
        outputdir = output_path.get()
        resize = resize_scale.get()
        speed = speed_scale.get()
        framerate = int(fps_entry.get())
        engine = engine_var.get()
        start_time = start_time_entry.get()
        end_time = end_time_entry.get()

        if not inputdir or not outputdir:
            messagebox.showerror("Error", "Input and output paths are required.")
            return

        startTime = start_time.split(':') if start_time else None
        endTime = end_time.split(':') if end_time else None

        clip = None

        if startTime and endTime:
            if len(startTime) != 3 or len(endTime) != 3:
                messagebox.showerror("Error", "Time format should be hr:min:sec.")
                return
            clip = (VideoFileClip(inputdir).subclip((float(startTime[0]),float(startTime[1]),float(startTime[2])),(float(endTime[0]),float(endTime[1]),float(endTime[2]))).resize(resize).speedx(speed))

        if not startTime and not endTime:
            clip = VideoFileClip(inputdir).resize(resize).speedx(speed)

        clip.write_gif(outputdir, fps=framerate, program=engine)
        messagebox.showinfo("Success", "GIF conversion completed successfully!")

    input_path = tk.StringVar()
    output_path = tk.StringVar()
    resize_scale = tk.DoubleVar(value=1.0)
    speed_scale = tk.DoubleVar(value=1.0)
    fps_entry = tk.StringVar(value="25")
    engine_var = tk.StringVar(value="ffmpeg")
    start_time_entry = tk.StringVar()
    end_time_entry = tk.StringVar()

    tk.Label(root, text="Input Video File:").grid(row=0, column=0, padx=10, pady=5)
    tk.Entry(root, textvariable=input_path, width=50).grid(row=0, column=1, padx=10, pady=5)
    tk.Button(root, text="Browse", command=browse_input).grid(row=0, column=2, padx=10, pady=5)

    tk.Label(root, text="Output GIF File:").grid(row=1, column=0, padx=10, pady=5)
    tk.Entry(root, textvariable=output_path, width=50).grid(row=1, column=1, padx=10, pady=5)
    tk.Button(root, text="Browse", command=browse_output).grid(row=1, column=2, padx=10, pady=5)

    tk.Label(root, text="Resize (0-1):").grid(row=2, column=0, padx=10, pady=5)
    tk.Scale(root, variable=resize_scale, from_=0, to=1, resolution=0.01, orient=tk.HORIZONTAL).grid(row=2, column=1, padx=10, pady=5)

    tk.Label(root, text="Speed (0-1):").grid(row=3, column=0, padx=10, pady=5)
    tk.Scale(root, variable=speed_scale, from_=0, to=1, resolution=0.01, orient=tk.HORIZONTAL).grid(row=3, column=1, padx=10, pady=5)

    tk.Label(root, text="FPS:").grid(row=4, column=0, padx=10, pady=5)
    tk.Entry(root, textvariable=fps_entry, width=5).grid(row=4, column=1, padx=10, pady=5)

    tk.Label(root, text="Engine:").grid(row=5, column=0, padx=10, pady=5)
    tk.OptionMenu(root, engine_var, "ffmpeg", "imageio").grid(row=5, column=1, padx=10, pady=5)

    tk.Label(root, text="Start Time (hr:min:sec):").grid(row=6, column=0, padx=10, pady=5)
    tk.Entry(root, textvariable=start_time_entry).grid(row=6, column=1, padx=10, pady=5)

    tk.Label(root, text="End Time (hr:min:sec):").grid(row=7, column=0, padx=10, pady=5)
    tk.Entry(root, textvariable=end_time_entry).grid(row=7, column=1, padx=10, pady=5)

    tk.Button(root, text="Convert", command=convert_video).grid(row=8, column=1, padx=10, pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
