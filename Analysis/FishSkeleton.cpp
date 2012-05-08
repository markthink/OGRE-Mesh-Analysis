OGRE骨骼解析 - 2011年4月12日
参考OgreResource.cpp(239) ->OgreSkeletonSerializer.cpp(108)
对应的骨骼文件参见：ogre_src_v1-7-2\Samples\Media\models\fish.skeleton.

00 10 									SKELETON_HEADER						unsigned short
5B 53 65 72 69 61 6C 69 7A 65 72 5F 76 31 2E 31 30 5D 	char* version		[Serializer_v1.10]	char[18]
0A 																			/n

00 20 									SKELETON_BONE						unsigned short
24 00 00 00 							LENGTH								unsigned int
7A 7A 77 78 79							char* name		zzwxy				char[5]
0A																			/n
00 00									handle								unsigned short 
										Vector3 Position 					float[3] (x,y,z)
00 00 00 00 
00 00 00 00
00 00 00 00 
										Quaternion orientation				float[4](x,y,z,w)
00 00 00 00
00 00 00 00
00 00 00 00 
00 00 80 3F
{
0020
24 00 00 00 
42 6F 6E 65 30 31 											Bone01
0A 
01 00 

0A DC 7C C0 
00 00 00 00 
12 22 2E 3B 

09 05 35 BF 
00 00 00 80
00 00 00 80
DE 04 35 3F
-----------------------
00 20 
24 00 00 00
42 6F 6E 65 30 32 											Bone02
0A 
02 00 

B8 CC 3D 40
4D EA 95 BC 
00 00 00 00

00 00 00 80
00 00 00 80
EE 69 2D 3E 
67 4D 7C 3F
------------------------
00 20 
24 00 00 00 
42 6F 6E 65 30 33 											Bone03
0A 
03 00 

D7 DD 32 40 
0E A1 04 B5 
00 00 00 00

00 00 00 80 
00 00 00 80
48 C6 1B 3E
42 05 7D 3F
--------------------------
00 20 
24 00 00 00 
42 6F 6E 65 30 34 											Bone04
0A 
04 00

F3 1F AA 3F
EC B8 41 34
00 00 00 00

00 00 00 00 
00 00 00 00
00 00 00 00 
00 00 80 3F 
}

00 30									SKELETON_BONE_PARENT				unsigned short
0A 00 00 00 							LENGTH								unsigned int
00 00 									handle								unsigned short 
01 00 									parentHandle						unsigned short 
{
00 30 
0A 00 00 00 
02 00 
01 00 
------
00 30 
0A 00 00 00 
03 00 
02 00
------
00 30 
0A 00 00 00
04 00 
03 00 
}

00 40 									SKELETON_ANIMATION					unsigned short			
8D 01 00 00 							LENGTH								unsigned int
73 77 69 6D 							char* name			swim			char[4]
0A 																			/n
00 00 00 40 							length								float

00 41									SKELETON_ANIMATION_TRACK 			unsigned short
2E 00 00 00 							LENGTH								unsigned int
00 00 									boneIndex 							unsigned short

10 41									SKELETON_ANIMATION_TRACK_KEYFRAME	unsigned short
26 00 00 00								LENGTH								unsigned int
00 00 00 00 							time								float				
										Quaternion rotate					float[4]
00 00 00 00		
00 00 00 00 
00 00 00 00
00 00 80 3F
										Vector3 translate						float[3]
00 00 00 00
00 00 00 00 
00 00 00 00

{
00 41 								
2E 00 00 00 							
01 00 								
--------------
10 41 								
26 00 00 00 							
00 00 00 00 

00 00 00 00 
00 00 00 00 
00 00 00 00 
00 00 80 3F 

00 00 00 00
00 00 00 00 
00 00 00 00 
==================
00 41 
7A 00 00 00 
02 00 
-------------
10 41 
26 00 00 00 
00 00 00 00

00 00 00 00
00 00 00 00 
00 00 00 00 
00 00 80 3F

00 00 00 00 
00 00 00 00 
00 00 00 00 
------------
10 41 
26 00 00 00
00 00 80 3F 

00 00 00 80
00 00 00 80 
B5 E8 AA BE
F5 50 71 3F 

00 00 00 00 
00 00 00 00
00 00 00 00 
-------------
10 41
26 00 00 00 
00 00 00 40 

00 00 00 00
00 00 00 00 
00 00 00 00
00 00 80 3F 

00 00 00 00
00 00 00 00 
00 00 00 00 
=====================
00 41 
7A 00 00 00
03 00
-------------
10 41 
26 00 00 00 
00 00 00 00 

00 00 00 00 
00 00 00 00
00 00 00 00 
00 00 80 3F

00 00 00 00
00 00 00 00 
00 00 00 00 
--------------
10 41 
26 00 00 00 
00 00 80 3F

00 00 00 80
00 00 00 80
18 F6 99 BE 
CC 26 74 3F

00 00 00 00
00 00 00 00
00 00 00 00 
--------------
10 41 
26 00 00 00
00 00 00 40 

00 00 00 80
00 00 00 80 
00 00 00 80 
00 00 80 3F 

00 00 00 00
00 00 00 00
00 00 00 00 
=====================
00 41 
2E 00 00 00 
04 00 
--------------
10 41 
26 00 00 00
00 00 00 00 

00 00 00 00 
00 00 00 00 
00 00 00 00
00 00 80 3F

00 00 00 00 
00 00 00 00 
00 00 00 00
}