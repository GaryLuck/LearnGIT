import numpy as np
import matplotlib.pyplot as plt

def compute_mandelbrot(xmin, xmax, ymin, ymax, width, height, max_iter=100):
    r1 = np.linspace(xmin, xmax, width)
    r2 = np.linspace(ymin, ymax, height)
    X, Y = np.meshgrid(r1, r2)
    c = X + 1j * Y
    z = np.zeros_like(c)
    mandelbrot = np.zeros(c.shape, dtype=int)

    mask = np.ones(c.shape, dtype=bool)

    for i in range(max_iter):
        z[mask] = z[mask]**2 + c[mask]
        diverged = np.abs(z[mask]) > 2

        mask_diverged = mask.copy()
        mask_diverged[mask] = diverged

        mandelbrot[mask_diverged] = i
        mask[mask_diverged] = False

    mandelbrot[mask] = max_iter
    return mandelbrot

def main():
    width, height = 1820, 980
    dpi = 100
    fig, ax = plt.subplots(figsize=(width/dpi, height/dpi), dpi=dpi)

    xmin, xmax, ymin, ymax = -2.0, 1.0, -1.5, 1.5

    mandelbrot = compute_mandelbrot(xmin, xmax, ymin, ymax, width, height)

    img = ax.imshow(mandelbrot, extent=[xmin, xmax, ymin, ymax], cmap='viridis', origin='lower')
    ax.set_title("Mandelbrot Set (Use Matplotlib Toolbar to Zoom/Pan)")

    is_updating = False

    def on_lims_change(event_ax):
        nonlocal xmin, xmax, ymin, ymax, is_updating

        if is_updating:
            return

        new_xmin, new_xmax = event_ax.get_xlim()
        new_ymin, new_ymax = event_ax.get_ylim()

        # Check if limits actually changed
        if (new_xmin, new_xmax, new_ymin, new_ymax) != (xmin, xmax, ymin, ymax):
            is_updating = True

            xmin, xmax, ymin, ymax = new_xmin, new_xmax, new_ymin, new_ymax

            # Recalculate
            new_mandelbrot = compute_mandelbrot(xmin, xmax, ymin, ymax, width, height)

            # Update the image
            img.set_data(new_mandelbrot)
            img.set_extent([xmin, xmax, ymin, ymax])
            fig.canvas.draw_idle()

            is_updating = False

    ax.callbacks.connect('xlim_changed', on_lims_change)
    ax.callbacks.connect('ylim_changed', on_lims_change)

    plt.show()

if __name__ == "__main__":
    main()
