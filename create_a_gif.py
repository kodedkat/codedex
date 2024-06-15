import imageio.v3 as iio

# store images
filenames = ['mr_fresh_stare.jpg', 'mr_fresh_bonk.jpg']
images = []

# read images
for filename in filenames:
    images.append(iio.imread(filename))

iio.imwrite('mr_fresh.gif', images, duration = 500, loop = 0)