from vtk import *
# Create reader for .vti
reader = vtkXMLImageDataReader()
reader.SetFileName('Isabel_3D.vti') # change path accordingly
reader.Update()

data = reader.GetOutput()

#  Create Color Transfer Function
color_transf_func = vtkColorTransferFunction()
color_transf_func.AddRGBPoint(-4931.54, 0.0, 1.0, 1.0)
color_transf_func.AddRGBPoint(-2508.95, 0.0, 0.0, 1.0)
color_transf_func.AddRGBPoint(-1873.9, 0.0, 0.0, 0.5)
color_transf_func.AddRGBPoint(-1027.16, 1.0, 0.0, 0.0)
color_transf_func.AddRGBPoint(-298.031, 1.0,0.4 , 0.0)
color_transf_func.AddRGBPoint(2594.97, 1.0, 1.0, 0.0)


#  Create  Opacity  Function
opacity_transf_func = vtkPiecewiseFunction()
opacity_transf_func.AddPoint(-4931.54, 1.0)
opacity_transf_func.AddPoint(101.815, 0.002)
opacity_transf_func.AddPoint(2594.97, 0.0)


volume_property = vtkVolumeProperty()
volume_property.SetColor(color_transf_func)
volume_property.SetScalarOpacity(opacity_transf_func)
volume_property.SetInterpolationTypeToLinear()

want_phong = bool(int(input("Do you want to use Phong shading? Type 0 for no, 1 for yes: ")))
if want_phong:
    volume_property.ShadeOn()
    volume_property.SetAmbient(0.5)
    volume_property.SetDiffuse(0.5)
    volume_property.SetSpecular(0.5)

# 5. Smart Volume Mapper

volume_mapper = vtkSmartVolumeMapper()
volume_mapper.SetInputData(data)

volume = vtkVolume()
volume.SetMapper(volume_mapper)
volume.SetProperty(volume_property)


# 6. Add Outline using vtkOutlineFilter

outline_filter = vtkOutlineFilter()
outline_filter.SetInputData(data)

outline_mapper = vtkPolyDataMapper()
outline_mapper.SetInputConnection(outline_filter.GetOutputPort())

outline_actor = vtkActor()
outline_actor.SetMapper(outline_mapper)
outline_actor.GetProperty().SetColor(0, 0, 0)  # black outline

# 7. Renderer and Window

renderer = vtkRenderer()
renderer.SetBackground(1, 1, 1)
renderer.AddVolume(volume)
renderer.AddActor(outline_actor)

render_window = vtkRenderWindow()
render_window.AddRenderer(renderer)
render_window.SetSize(1000, 1000)

interactor = vtkRenderWindowInteractor()
interactor.SetRenderWindow(render_window)

# 8. Render

render_window.Render()
interactor.Start()