# geoni0n
Union of geometric shapes in the form of WKTs.

This app check a .csv file that has one column (without a header) of geometry shapes. It will process that
file checking if it's an actual shape and not a line or a point and then if the shape is valid, if not it tries to fix it
using the buffer method. After all is done, it will give back the convex hull union of the shapes.