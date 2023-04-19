# import Blender Python API
import bpy

# Set the size of the box
size_x = 2.0
size_y = 2.0
size_z = 2.0

# Create a mesh
mesh = bpy.data.meshes.new("BoxMesh")

# Create vertices
verts = [
    (-size_x, -size_y, -size_z),
    (size_x, -size_y, -size_z),
    (size_x, size_y, -size_z),
    (-size_x, size_y, -size_z),
    (-size_x, -size_y, size_z),
    (size_x, -size_y, size_z),
    (size_x, size_y, size_z),
    (-size_x, size_y, size_z)
]

# Create edges
edges = []
for i in range(0, 4):
    edges.append((i, (i + 1) % 4))
    edges.append((i + 4, ((i + 1) % 4) + 4))
    edges.append((i, i + 4))

# Create faces
faces = [
    (0, 1, 2, 3),
    (4, 5, 6, 7),
    (0, 4, 7, 3),
    (1, 5, 6, 2),
    (0, 1, 5, 4),
    (3, 2, 6, 7)
]

# Assign vertices, edges and faces to the mesh
mesh.from_pydata(verts, edges, faces)

# Create a new object and link it to the scene
obj = bpy.data.objects.new("Box", mesh)
bpy.context.scene.collection.objects.link(obj)
