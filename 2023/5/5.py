def extract_map(texts):
    ends = list()
    maps = list(list())
    mapsNumber = list(list())
    ends.append(0)
    mapId = 0
    for id_, line in enumerate(texts):
        if line == '\n':
            ends.append(id_)
            maps.append(texts[ends[-2]+2:ends[-1]])
    mapText = [[0]]
    for id_, map_ in enumerate(maps):
        for lines in map_:
            mapText[id_].append(re.findall("\d+", lines))
        mapText.append(list())
    mapText = mapText[1:-1]

    mapValueX = list()
    mapValueY = list()
    for id1, map_ in enumerate(mapText):
        print(id1)
        #mapValue.append(np.arange(10000000000))
        mapValueX.append(list())
        mapValueY.append(list())
        for id2, value in enumerate(map_):
            value = [ int(x) for x in value ]
            #mapValue[-1][value[1]:value[1]+value[2]] = np.linspace(value[0],value[2]+value[0]-1, value[2])
            mapValueX[-1].append([value[1], value[1]+value[2]-1])
            mapValueY[-1].append([value[0], value[0]+value[2]-1])
    return ends, maps, mapText, mapValueX, mapValueY

import scipy
def get_transformation(mapValueXX, mapValueYY, number):
    new = number
    for id_ in range(len(mapValueXX)):
        new[new == mapValueXX[id_][0]] = mapValueYY[id_][0]
        new[new == mapValueXX[id_][1]] = mapValueYY[id_][1]
        toInterp =  (new > mapValueXX[id_][0]) & (new < mapValueYY[id_][1])
        f = scipy.interpolate.interp1d(mapValueXX[id_], mapValueYY[id_], "linear")
        new2 = new
        new2[toInterp] = f(new[toInterp])
        new[toInterp] = new2[toInterp]
    return new


import re
import numpy as np

with open('test.txt') as f:
    texts = list(list())
    for line in f:
        texts.append(line)
seedsOld = re.findall("\d+", texts[0])
seedsOld = [int(x) for x in seedsOld]

seeds = np.array([])
for id_ in range(int(np.floor(len(seedsOld) / 2))):
    print(id_)
    seeds = np.concatenate((seeds, np.arange(seedsOld[2 * id_], seedsOld[2 * id_] + seedsOld[2 * id_ + 1])))

seedTransformation = list()
seedsTab = np.zeros((len(seeds),7))
seedsTab[:,0] = seeds

ends, maps, mapText,  mapValueX, mapValueY = extract_map(texts)

seedTransformation = list()
seedsTab = np.zeros((len(seeds),7))

for idMap in range(7):
    seedsTab[:,idMap] = get_transformation(mapValueX[idMap],
                                           mapValueY[idMap],
                                           seedsTab[:,idMap-1])