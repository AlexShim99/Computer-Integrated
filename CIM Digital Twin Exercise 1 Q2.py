import bpy

# Set the sizes of the boxes
sizes = [(2.0, 2.0, 2.0),
         (2.5, 2.5,2.5),
         (3.0, 3.0, 3.0)]

# Create a loop to create multiple boxes with different sizes
for i in range(len(sizes)):
    size = sizes[i]
    
    # Create a mesh
    mesh = bpy.data.meshes.new("BoxMesh")

    # Create vertices
    width, height, depth = size
    half_width = width / 2.0
    half_height = height / 2.0
    half_depth = depth / 2.0
    verts = [
        (-half_width, -half_height, -half_depth),
        (-half_width, half_height, -half_depth),
        (half_width, half_height, -half_depth),
        (half_width, -half_height, -half_depth),
        (-half_width, -half_height, half_depth),
        (-half_width, half_height, half_depth),
        (half_width, half_height, half_depth),
        (half_width, -half_height, half_depth),
    ]

    # Create edges
    edges = [(0, 1), (1, 2), (2, 3), (3, 0),
             (4, 5), (5, 6), (6, 7), (7, 4),
             (0, 4), (1, 5), (2, 6), (3, 7)]

    # Create faces
    faces = [(0, 1, 2, 3),
             (4, 5, 6, 7),
             (0, 1, 5, 4),
             (1, 2, 6, 5),
             (2, 3, 7, 6),
             (3, 0, 4, 7)]

    # Assign vertices, edges and faces to the mesh
    mesh.from_pydata(verts, edges, faces)

    # Create a new object and link it to the scene
    obj = bpy.data.objects.new("Box{}".format(i+1), mesh)
    bpy.context.scene.collection.objects.link(obj)

    # Position and scale the object
    obj.location = (i * width * 3.0, 0, 0)
    obj.scale = size
