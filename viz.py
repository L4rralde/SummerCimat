import trimesh
import pyrender
import trimesh
import numpy as np

# Load the GLB file
glb_file = "data/vggt_output/input_images_20250622_102110_094677/glbscene_50_All_maskbFalse_maskwFalse_camTrue_skyFalse_predDepthmap_and_Camera_Branch.glb"

# Load the GLB file
data = trimesh.load(glb_file)

# Create Pyrender scene
scene = pyrender.Scene()

for name, geometry in data.geometry.items():
    if isinstance(geometry, trimesh.Trimesh):
        scene.add(pyrender.Mesh.from_trimesh(geometry))
    elif isinstance(geometry, trimesh.points.PointCloud):
        points = geometry.vertices
        colors = geometry.colors if hasattr(geometry, 'colors') else np.ones((len(points), 3)) * 128
        scene.add(pyrender.Mesh.from_points(points, colors=colors.astype(np.uint8)))

# Add lighting
scene.add(pyrender.DirectionalLight(color=[1.0, 1.0, 1.0], intensity=2.0))

# Render
pyrender.Viewer(scene, use_raymond_lighting=True)