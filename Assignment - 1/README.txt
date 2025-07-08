==================================================
         	Assignment 1
==================================================

PART 1: 2D ISOCONTOUR EXTRACTION
PART 2: 3D VOLUME RENDERING

Output Files:
    - iso_surface.vtp (Part 1)
    - Rendered window from VTK viewer (Part 2)

==================================================
               REQUIREMENTS
==================================================

- Python 3.x
- VTK Python module


==================================================
                PART 1: 2D ISOLINE EXTRACTION
==================================================

Description:
------------
This script reads a 2D scalar field from a VTK `.vti` file (structured ImageData),
and extracts isolines for a user-specified isovalue. It:
- Identifies grid cells where the scalar crosses the isovalue
- Uses inverse interpolation to compute edge-crossing points
- Stores each isoline segment as a polyline in a `.vtp` file

===========================
    Input Requirements
===========================

- A 2D `.vti` file (e.g., `Isabel_2D.vti`)
- Scalar field array named `'Pressure'`

You may update the filename and array name:

    reader.SetFileName('Isabel_2D.vti')
    data = data.GetPointData().GetArray('Pressure')

===========================
    Running the Script
===========================

1. Place your `.vti` file in the appropriate directory.
2. Run the script:

       python isocontour.py

3. Enter the isovalue when prompted:

       Enter isovalue: -1200.0

4. The script creates:

       iso_surface.vtp

===========================
    Visualizing the Output
===========================

Open the `.vtp` file in ParaView:

1. Launch ParaView
2. Open `iso_surface.vtp`
3. Click **"Apply"**
4. Set Representation to **"Wireframe"** for clear isoline viewing
5. Increase the Line width to 5 to see it the isocontour clearly
6. Adjust camera/axes as needed
7. Also load the "Isabel_2D.vti to visualise better

==================================================
        PART 2: 3D VOLUME RENDERING (with Phong Shading)
==================================================

Description:
------------
This script renders a 3D `.vti` volume using colour transfer and opacity transfer functions,
with optional Phong shading and an outline box.


===========================
    Input Requirements
===========================

- A 3D `.vti` file, e.g.:

       Isabel_3D.vti

===========================
    Running the Script
===========================

1. Ensure the `.vti` file exists at the correct path
2. Run:

       python render_volume.py

3. You will be prompted:

       Do you want to use Phong shading? Type 0 for no, 1 for yes:

   - Enter `1` for Phong shading (adds lighting realism)
   - Enter `0` to skip it

4. A VTK render window will appear with:
   - Colored volume rendering
   - Adjustable 3D interaction (rotate, zoom, pan)
   - White outline showing volume boundary

To change the file path:

   reader.SetFileName("Isabel_3D.vti") -> reader.SetFileName("your file path")

==================================================
              END OF README
==================================================
