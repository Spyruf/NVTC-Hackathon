from __future__ import print_function
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap as Basemap
from matplotlib.colors import rgb2hex, Normalize
from matplotlib.patches import Polygon
from matplotlib.colorbar import ColorbarBase
import collections


popdensity = {
'New Jersey':  0.0,
'Rhode Island':   0.0,
'Massachusetts':   0.0,
'Connecticut':	  0.0,
'Maryland':   0.0,
'New York':    0.0,
'Delaware':    0.0,
'Florida':     0.0,
'Ohio':	 0.0,
'Pennsylvania':	 0.0,
'Illinois':    0.0,
'California':  0.0,
'Hawaii':  0.0,
'Virginia':    0.0,
'Michigan':    0.0,
'Indiana':    0.0,
'North Carolina':  0.0,
'Georgia':     0.0,
'Tennessee':   0.0,
'New Hampshire':   0.0,
'South Carolina':  0.0,
'Louisiana':   0.0,
'Kentucky':   0.0,
'Wisconsin':  0.0,
'Washington':  0.0,
'Alabama':     0.0,
'Missouri':    0.0,
'Texas':   0.0,
'West Virginia':   0.0,
'Vermont':     0.0,
'Minnesota':  0.0,
'Mississippi':	 0.0,
'Iowa':	 0.0,
'Arkansas':    0.0,
'Oklahoma':    0.0,
'Arizona':     0.0,
'Colorado':    0.0,
'Maine':  0.0,
'Oregon': 0.0,
'Kansas':  0.0,
'Utah':	 0.0,
'Nebraska':    0.0,
'Nevada':  0.0,
'Idaho':   0.0,
'New Mexico':  0.0,
'South Dakota':	 0.0,
'North Dakota':	 0.0,
'Montana':    0.0,
'Wyoming':    0.0,
'Alaska':    0.0}

popwords = {
'New Jersey':  [],
'Rhode Island':   [],
'Massachusetts':   [],
'Connecticut':	  [],
'Maryland':   [],
'New York':    [],
'Delaware':    [],
'Florida':     [],
'Ohio':	 [],
'Pennsylvania':	 [],
'Illinois':    [],
'California':  [],
'Hawaii':  [],
'Virginia':    [],
'Michigan':    [],
'Indiana':    [],
'North Carolina':  [],
'Georgia':     [],
'Tennessee':   [],
'New Hampshire':   [],
'South Carolina':  [],
'Louisiana':   [],
'Kentucky':   [],
'Wisconsin':  [],
'Washington':  [],
'Alabama':     [],
'Missouri':    [],
'Texas':   [],
'West Virginia':   [],
'Vermont':     [],
'Minnesota':  [],
'Mississippi':	 [],
'Iowa':	 [],
'Arkansas':    [],
'Oklahoma':    [],
'Arizona':     [],
'Colorado':    [],
'Maine':  [],
'Oregon': [],
'Kansas':  [],
'Utah':	 [],
'Nebraska':    [],
'Nevada':  [],
'Idaho':   [],
'New Mexico':  [],
'South Dakota':	 [],
'North Dakota':	 [],
'Montana':    [],
'Wyoming':    [],
'Alaska':    []}

st = open('us_states.txt', 'r')
abb_to_state = {}
#state_to_abb = {}
for line in st:
    line = line.strip().split("\t")
    abb_to_state[line[1]] = line[0]
    #state_to_abb[line[0]] = line[1]


raw_file = open('location.txt', 'r')
location_list = []
for line in raw_file:
    line = line.strip()
    if len(line) > 0:
        location_list.append(line)

lost = 0
for element in location_list:
    hit = 0
    sep = element.split(",")
    bio = []
    if sep[-1] != "none":
        bio = sep[-1].split(" ")
    element = element.strip(" |.,/")
    if element.title() in popdensity:                                     #IF LOCATION IS DIRECTLY STATED (i.e. "Virginia")
        popdensity[element.title()] = popdensity[element.title()] + 1
        if len(bio) > 0:
            for word in bio:
                (popwords[element.title()]).append(word)
        hit = 1
    elif "," in element:                                                  #IF LOCATION IS GIVEN WITH COMMAS (i.e. "Charlottesville, VA")
        element = element.split(",")
        for e in element:
            e = e.strip()
            if e.title() in popdensity:
                popdensity[e.title()] = popdensity[e.title()] + 1
                if len(bio) > 0:
                    for word in bio:
                        (popwords[e.title()]).append(word)
                hit = 1
            elif e.upper() in abb_to_state:
                state = abb_to_state[e.upper()]
                popdensity[state.title()] = popdensity[state.title()] + 1
                if len(bio) > 0:
                    for word in bio:
                        (popwords[state.title()]).append(word)
                hit = 1
    elif " " in element:                                                 #IF LOCATION IS GIVEN WITH SPACE (i.e. "Charlottesville VA")
        element = element.split(" ")
        for e in element:
            e = e.strip()
            if e.title() in popdensity:
                popdensity[e.title()] = popdensity[e.title()] + 1
                if len(bio) > 0:
                    for word in bio:
                        (popwords[e.title()]).append(word)
                hit = 1
            elif e.upper() in abb_to_state:
                state = abb_to_state[e.upper()]
                popdensity[state.title()] = popdensity[state.title()] + 1
                if len(bio) > 0:
                    for word in bio:
                        (popwords[state.title()]).append(word)
                hit = 1
    elif element.upper() in abb_to_state:                                       #IF LOCATION IS GIVEN WITH ABB (i.e. "VA")
        state = abb_to_state[element.upper()]
        popdensity[state.title()] = popdensity[state.title()] + 1
        if len(bio) > 0:
            for word in bio:
                (popwords[state.title()]).append(word)
        hit = 1
    elif "/" in element:                                                  #IF LOCATION IS GIVEN WITH COMMAS (i.e. "Charlottesville/VA")
        element = element.split("/")
        for e in element:
            e = e.strip()
            if e.title() in popdensity:
                popdensity[e.title()] = popdensity[e.title()] + 1
                if len(bio) > 0:
                    for word in bio:
                        (popwords[e.title()]).append(word)
                hit = 1
            elif e.upper() in abb_to_state:
                state = abb_to_state[e.upper()]
                popdensity[state.title()] = popdensity[state.title()] + 1
                if len(bio) > 0:
                    for word in bio:
                        (popwords[state.title()]).append(word)
                hit = 1
    if hit == 0:
        lost = lost + 1
        #print("LOSING DATA,:", element)

failure = round(lost/(len(location_list))*100, 2)
print(str(lost) + " datapoints lost, therefore " + str(failure) + "% data lost")
success = round((len(location_list)-lost)/(len(location_list))*100, 2)
print(str(len(location_list)-lost) + " datapoints plotted successfully, therefore " + str(success) + "% data collected")
#print("Reliable data using 85% identification success rate is: " + str(round(success*.85, 2)) + "%")

fig, ax = plt.subplots()

m = Basemap(llcrnrlon=-119, llcrnrlat=20, urcrnrlon=-64, urcrnrlat=49, projection='lcc', lat_1=33, lat_2=45, lon_0=-95)  # Lambert Conformal map of lower 48 states.

m_ = Basemap(llcrnrlon=-190, llcrnrlat=20, urcrnrlon=-143, urcrnrlat=46, projection='merc', lat_ts=20)                   # Mercator projection, for Alaska and Hawaii

shp_info = m.readshapefile('st99_d00', 'states',drawbounds=True, linewidth=0.45, color='gray')
shp_info_ = m_.readshapefile('st99_d00', 'states', drawbounds=False)


# -------- choose a color for each state based on population density. -------
colors = {}
statenames = []
cmap = plt.cm.Blues  # use 'reversed hot' colormap
vmin = 0    # lower bound
vmax = popdensity[max(popdensity, key=popdensity.get)]  # set range.
norm = Normalize(vmin=vmin, vmax=vmax)
for shapedict in m.states_info:
    statename = shapedict['NAME']
    if statename not in ['District of Columbia', 'Puerto Rico']:
        pop = popdensity[statename]

        # calling colormap with value between 0 and 1 returns
        # rgba value.  Invert color range (hot colors are high
        # population), take sqrt root to spread out colors more.

        colors[statename] = cmap(np.sqrt((pop-vmin)/(vmax-vmin)))[:3]
    statenames.append(statename)

# ---------  cycle through state names, color each one.  --------------------
for nshape,seg in enumerate(m.states):
    # skip DC and Puerto Rico.
    if statenames[nshape] not in ['Puerto Rico', 'District of Columbia']:
        color = rgb2hex(colors[statenames[nshape]])
        poly = Polygon(seg, facecolor=color, edgecolor=color)
        ax.add_patch(poly)

AREA_1 = 0.005  # exclude small Hawaiian islands that are smaller than AREA_1
AREA_2 = AREA_1 * 30.0  # exclude Alaskan islands that are smaller than AREA_2
AK_SCALE = 0.19  # scale down Alaska to show as a map inset
HI_OFFSET_X = -1900000  # X coordinate offset amount to move Hawaii "beneath" Texas
HI_OFFSET_Y = 250000    # similar to above: Y offset for Hawaii
AK_OFFSET_X = -250000   # X offset for Alaska (These four values are obtained
AK_OFFSET_Y = -750000   # via manual trial and error, thus changing them is not recommended.)

for nshape, shapedict in enumerate(m_.states_info):  # plot Alaska and Hawaii as map insets
    if shapedict['NAME'] in ['Alaska', 'Hawaii']:
        seg = m_.states[int(shapedict['SHAPENUM'] - 1)]
        if shapedict['NAME'] == 'Hawaii' and float(shapedict['AREA']) > AREA_1:
            seg = [(x + HI_OFFSET_X, y + HI_OFFSET_Y) for x, y in seg]
            color = rgb2hex(colors[statenames[nshape]])
        elif shapedict['NAME'] == 'Alaska' and float(shapedict['AREA']) > AREA_2:
            seg = [(x*AK_SCALE + AK_OFFSET_X, y*AK_SCALE + AK_OFFSET_Y)\
                   for x, y in seg]
            color = rgb2hex(colors[statenames[nshape]])
        poly = Polygon(seg, facecolor=color, edgecolor='gray', linewidth=.45)
        ax.add_patch(poly)

ax.set_title('Veteran Population by State on Twitter')

# ---------  Plot bounding boxes for Alaska and Hawaii insets  --------------
light_gray = [0.8]*3  # define light gray color RGB
x1, y1 = m_([-190, -183, -180, -180, -175, -171, -171], [29, 29, 26, 26, 26, 22, 20])
x2, y2 = m_([-180, -180, -177], [26, 23, 20])  # these numbers are fine-tuned manually
m_.plot(x1, y1, color=light_gray, linewidth=0.8)  # do not change them drastically
m_.plot(x2, y2, color=light_gray, linewidth=0.8)

# ---------   Show color bar  ---------------------------------------
ax_c = fig.add_axes([0.9, 0.1, 0.03, 0.8])
cb = ColorbarBase(ax_c, cmap=cmap, norm=norm, orientation='vertical',
                  label=r'[population per state] ')

def on_plot_hover(event):
    for curve in ax.get_lines():
        if curve.contains(event)[0]:
            print("over %s" % curve.get_gid())
fig.canvas.mpl_connect('motion_notify_event', on_plot_hover)
succ = "90% confidence"
plt.annotate(succ, xy=(-29, 0), xycoords='axes fraction', size=10)
plt.show()
