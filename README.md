# Mandelbrot visualizer
## Python edition

This is a Python implementaion of the Mandelbrot visualizer.
As ypu can see, this is significantly simpler. It also runs just as fast, thanks to the inherent vectorization of numpy.

---

## Setup

```bash
pip install -r requirements.txt
```

## Run
```bash
python main.py
```

## Combine images into a video

```bash
ffmpeg -framerate 30 -pattern_type glob -i 'image_*.png' -c:v libx264 -pix_fmt yuv420p out.mp4
  ```
  ---
  
  **Click to watch the video.**  
  [![IMAGE ALT TEXT](./frame.png)](http://www.youtube.com/watch?v=6KapQf8ZErs)
