# Open3D: www.open3d.org
# The MIT License (MIT)
# See license file or visit www.open3d.org for details

import sys
sys.path.append("../..")
from py3d import *

if __name__ == "__main__":
	mesh = ReadTriangleMesh("../../TestData/knot.ply")
	mesh.ComputeVertexNormals()
	DrawGeometries([mesh])