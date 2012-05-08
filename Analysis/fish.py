from struct import *

fish=open('fish.mesh','rb')

HEADER_STREAM_ID=unpack('H',fish.read(2))
HEADER_VERSION=unpack('22s',fish.read(22))
unpack('c',fish.read(1))
HEADER_MESH=unpack('H',fish.read(2))
unpack('I',fish.read(4))
SkeletallyAnimated=unpack('?',fish.read(1))
SUBMESH=unpack('H',fish.read(2))
unpack('I',fish.read(4))
materialName=unpack('13s',fish.read(13))
unpack('c',fish.read(1))
useSharedVertices=unpack('?',fish.read(1))
indexCount=unpack('I',fish.read(4))
idx32bit=unpack('?',fish.read(1))

indexCountInt=int(indexCount[0])
for i in range(int(indexCountInt/3)):
    a=unpack('3H',fish.read(6))
    #print(a)

M_GEOMTERY=unpack('H',fish.read(2))
unpack('I',fish.read(4))
VertexCount=unpack('I',fish.read(4))
M_GEOMTRY_VERTEX_DECLARATION=unpack('H',fish.read(2))
unpack('I',fish.read(4))

M_GEOMTRY_VERTEX_ELEMENT=unpack('H',fish.read(2))
unpack('I',fish.read(4))
source=unpack('H',fish.read(2))
ftype=unpack('H',fish.read(2))
semantic=unpack('H',fish.read(2))
offset=unpack('H',fish.read(2))
index=unpack('H',fish.read(2))

M_GEOMTRY_VERTEX_ELEMENT=unpack('H',fish.read(2))
unpack('I',fish.read(4))
source=unpack('H',fish.read(2))
ftype=unpack('H',fish.read(2))
semantic=unpack('H',fish.read(2))
offset=unpack('H',fish.read(2))
index=unpack('H',fish.read(2))

M_GEOMTRY_VERTEX_ELEMENT=unpack('H',fish.read(2))
unpack('I',fish.read(4))
source=unpack('H',fish.read(2))
ftype=unpack('H',fish.read(2))
semantic=unpack('H',fish.read(2))
offset=unpack('H',fish.read(2))
index=unpack('H',fish.read(2))

M_GEOMTRY_VERTEX_BUFFER_DATA=unpack('H',fish.read(2))
unpack('I',fish.read(4))
bindIndex=unpack('H',fish.read(2))
vertexSize=unpack('H',fish.read(2))

M_GEOMTRY_VERTEX_BUFFER_DATA=unpack('H',fish.read(2))
unpack('I',fish.read(4))

print(fish.tell())
#print(int(VertexCount[0]))
for i in range(int(VertexCount[0])):
    x,y,z=unpack('3f',fish.read(12))
    #fish.seek(12,1)
    nx,ny,nz=unpack('3f',fish.read(12))
    print(x,y,z)
    #print(nx,ny,nz)

M_GEOMTRY_VERTEX_BUFFER_DATA=unpack('H',fish.read(2))
unpack('I',fish.read(4))
bindIndex=unpack('H',fish.read(2))
vertexSize=unpack('H',fish.read(2))

M_GEOMTRY_VERTEX_BUFFER_DATA=unpack('H',fish.read(2))
unpack('I',fish.read(4))

for i in range(int(VertexCount[0])):
    u,v=unpack('2f',fish.read(8))

    #print(u,v)

M_SUBMESH_OPERATION=unpack('H',fish.read(2))
unpack('I',fish.read(4))

operationType=unpack('H',fish.read(2))

#wb->weight bone
wb=0x4100
my=int(unpack('H',fish.read(2))[0])
while wb==my:
    M_SUBMESH_BONE_ASSIGNMENT=wb
    unpack('I',fish.read(4))
    VertexIndex=unpack('I',fish.read(4))
    boneIndex=unpack('H',fish.read(2))
    weight=unpack('I',fish.read(4))

    my=int(unpack('H',fish.read(2))[0])
    #print(M_SUBMESH_BONE_ASSIGNMENT)
    #print(VertexIndex)
    #print(boneIndex)
    #print(weight)
else:
    M_MESH_SKELETON_LINK=my
    
#M_MESH_SKELETON_LINK=unpack('H',fish.read(2))
unpack('I',fish.read(4))

skeletonName=unpack('13s',fish.read(13))
unpack('c',fish.read(1))

M_MESH_BOUNDS=unpack('H',fish.read(2))
unpack('I',fish.read(4))

minX=unpack('I',fish.read(4))
minY=unpack('I',fish.read(4))
minZ=unpack('I',fish.read(4))
maxX=unpack('I',fish.read(4))
maxY=unpack('I',fish.read(4))
maxZ=unpack('I',fish.read(4))
radius=unpack('I',fish.read(4))

M_SUBMESH_NAME_TABLE=unpack('H',fish.read(2))
unpack('I',fish.read(4))

M_EDGE_LISTS=unpack('H',fish.read(2))
unpack('I',fish.read(4))

M_EDGE_LIST_LOD=unpack('H',fish.read(2))
unpack('I',fish.read(4))

lodIndex=unpack('H',fish.read(2))
isManual=unpack('?',fish.read(1))
isClosed=unpack('?',fish.read(1))

numTriangles=unpack('L',fish.read(4))
numEdgeGroups=unpack('L',fish.read(4))

for i in range(int(numTriangles[0])):
    indexSet=unpack('L',fish.read(4))
    vertexSet=unpack('L',fish.read(4))
    vertIndex=unpack('3L',fish.read(12))
    sharedVertIndex=unpack('3L',fish.read(12))
    normal=unpack('4f',fish.read(16))
    #print(normal)

M_EDGE_GROUP=unpack('H',fish.read(2))
unpack('I',fish.read(4))

vertexSet=unpack('I',fish.read(4))
triStart=unpack('I',fish.read(4))
triCount=unpack('I',fish.read(4))
numEdges=unpack('I',fish.read(4))
print(numEdges)
for i in range(int(numEdges[0])):
    triIndex=unpack('2L',fish.read(8))
    vertIndex=unpack('2L',fish.read(8))
    sharedVertIndex=unpack('2L',fish.read(8))
    degenerate=unpack('?',fish.read(1))
    #print(triIndex)
    #print(vertIndex)
    #print(sharedVertIndex)
    #print(degenerate)

#Determine the end of file
#print(fish.tell())
fish.close()

