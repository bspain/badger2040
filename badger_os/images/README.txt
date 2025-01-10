Images must be 296x128 pixel JPEGs

Create a new "images" directory via Thonny, and upload your .jpg files there.

## Creating from badges

magick convert -trim -density 1200 -resize 114x114^ -bordercolor white -border 2 -gravity center -monochrome sparkyproto.jpeg sparkyproto_badge.jpg
