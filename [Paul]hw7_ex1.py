#This program estimates the x coordinate where some particle decay occurs by fitting a line to 2 sets of particle detector coordinates given by a txt file.  Calculated x coordinates are compared to an actual value for each decay and the difference is plotted on a histogram.
import numpy as np
import matplotlib.pyplot as plt

#Coordinates follow [X0 Y0 y00 y01 y02 y03 y10 y11 y12 y13] format
#X0, Y0 are true point of coordinates Y0 = 0
#yij, i = track number, j = detector number
#detector numbers j: 0 = 2cm, 1 = 3cm, 2 = 5cm, 3 = 7cm
tracks = np.loadtxt("straightTracks.txt")

#This list represents the true x origin coordinates for each array
x0s = []

#These lists are our estimates for the x origin coordinate
x1s = []
x2s = []
xaves = []

#These are the coordinates of each detector along the x axis
dcoords = [2, 3, 5, 7]

#This for loop process takes the individual y coordinates for the 2 tracks of each array in the text file and appends the true x origin coordinate to our x0s list.  We then fit the coordinates of the 2 tracks using np.polyfit to extract 2 estimated x coordinates which we append to the x1s and x2s lists.
for track in tracks:
	x0s.append(track[0])
	track_1 = []
	track_2 = []
	for i in range(2, 6):
		track_1.append(track[i])
		track_2.append(track[i+4])
	poly_track_1 = np.polyfit(dcoords, track_1, 1)
	poly_track_2 = np.polyfit(dcoords, track_2, 1)
	x1s.append(poly_track_1[1])
	x2s.append(poly_track_2[1])

#We define a function for calculating the average between the two estimated x coordinates for each track
def xave(x1, x2):
	return (x1+x2)/2

#We iterate through our x1s and x2s lists to produce a list of the average between each pair of x1s and x2s
for i in range(0, len(x1s)):
	xaves.append(xave(x1s[i], x2s[i]))

#Finally we create 3 lists which represent the differences between each of the 3 estimated x origin values with the true x origin value
difx1_x0 = []
difx2_x0 = []
difxave_x0 = []
for i in range(0, len(x0s)):
	difx1_x0.append(x1s[i]-x0s[i])
	difx2_x0.append(x2s[i]-x0s[i])
	difxave_x0.append(xaves[i]-x0s[i])

#Histograms are printed to the screen to neatly represent our lists of differences. Lower bound is set to -500um = -0.05 cm. Upper bound set to 500um = 0.05cm. 
low = -0.05
high = 0.05
nbins = 100
bins = np.linspace(low, high, nbins+1)

#Code for plotting
fig, (ax1,ax2) = plt.subplots(2, 1, sharey = True)

#Figure 1 plots x1-x0 and x2-x0 on the same histogram
contents, binEdges, _ = ax1.hist(difx1_x0, bins, histtype='step', log = False, color = 'blue', label = 'X1-X0')
contents, binEdges, _ = ax1.hist(difx2_x0, bins, histtype='step', log = False, color = 'red', label = 'X2-X0')
ax1.set_xlim(binEdges[0], binEdges[-1])
ax1.set_ylim(0, 1.4*np.max(contents))
ax1.tick_params("both", direction = 'in', length=10, right=True)
ax1.set_xlabel("Difference in x coords cm")
ax1.legend()


#Figure 2 plots xave - x0
contents, binEdges, _ = ax2.hist(difxave_x0, bins, histtype='step', log = False, color = 'purple', label = "Xave - X0")
ax2.set_xlim(binEdges[0], binEdges[-1])
ax2.set_ylim(0, 1.4*np.max(contents))
ax2.tick_params("both", direction = 'in', length=10, right=True)
ax2.set_xlabel("Difference in x coords cm")
ax2.legend()
fig.show()
input("press enter to exit")
