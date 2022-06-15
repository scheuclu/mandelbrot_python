# Mandelbrot visualizer
## Python edition

This is a Python implementaion of the Mandelbrot visualizer.
As you can see, this is significantly simpler. It also runs just as fast, thanks to the inherent vectorization of numpy.

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
  [![IMAGE ALT TEXT HERE](https://img.youtube.com/vi/yVMQ_w54QVE/0.jpg)](https://www.youtube.com/watch?v=yVMQ_w54QVE)

