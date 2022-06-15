
import numpy as np
from PIL import Image

  
PI=3.14159265359
def iter2color(val):
   frac=val/val.max() #sqrt
   #frac=val/255 #sqrt
   r = (frac+0.2*np.sin(frac*2*PI))
   g = (frac+0.2*np.sin(frac*4*PI))
   b = (frac+0.2*np.sin(frac*6*PI))
   return np.stack([r,g,b, b*0+1], axis=-1)

def create_frame(
    center=(-0.7451580000099, 0.11257483),
    w=1.92*.0002,
    h=1.08*.0002,
    nw=192*2,
    nh=108*2,
    suffix=1):
  
    Z=np.zeros(shape=(nh,nw), dtype=complex)
    x = np.linspace(center[0]-w/2, center[0]+w/2, nw)
    y = np.linspace(center[1]-h/2, center[1]+h/2, nh)
    Y, X = np. meshgrid(x, y)
    C=X*complex(0,1)+Y

    Z_final=np.zeros(shape=(nh,nw), dtype=int)
    for i in range(255):
        Z=Z**2+C
        Z_final += np.isnan(Z).astype('int')

    colors = iter2color(Z_final)
    img = Image.fromarray(np.uint8(colors*255))
    return img

def main():
    center = (-0.7450450892059, 0.1126120218022)
    N = 5
    # w=1.92*0.00000000000002
    # h=1.08*0.00000000000002
    w = 1.92 * 2.0000000000000
    h = 1.08 * 2.0000000000000
    nw = 192 * 20
    nh = 108 * 20
    suffix = 1

    for i in range(N):
        create_frame(
            center=center,
            w=w,
            h=h,
            nw=nw,
            nh=nh,
            suffix=i)
        w*=0.98
        h*=0.98
        print(i, center, (w,h))


if __name__ == "__main__":
    main()