from vtk import *

def coord(point1, point2, val1, val2, user_isoval):#returns the coordinates of point having scalar value equal to user_isovalue
                                                    #i.e. the required value corresponding to isosurface(inverse interpolation)
    x1, x2 = point1[0], point2[0]
    y1, y2 = point1[1], point2[1]
    z1, z2 = point1[2], point2[2]
    t = (user_isoval - val1) / (val2 - val1)
    x = x1 + t * (x2 - x1)
    y = y1 + t * (y2 - y1)
    z = z1 + t * (z2 - z1)
    return (x, y, z)

def contour_extraction(user_isoval): # function that returns the iso surface vtp file for the user_isovalue
    reader = vtkXMLImageDataReader()
    reader.SetFileName('Isabel_2D.vti') # change path accordingly
    reader.Update()
    data = reader.GetOutput()
    numCells = data.GetNumberOfCells()  # number 0f cells in dataset
    dims = data.GetDimensions()         # dimensions of 2D - data
    total_points = 0
    points = vtkPoints()
    cells = vtkCellArray()
    pdata = vtkPolyData()
    for i in range(numCells):
        cell = data.GetCell(i)
        # Get cell's point IDs in counter-clockwise sense
        pid1 = cell.GetPointId(0)
        pid2 = cell.GetPointId(1)
        pid3 = cell.GetPointId(3)
        pid4 = cell.GetPointId(2)

        # Get the pressure value for the corresponding cell points
        dataArr = data.GetPointData().GetArray('Pressure')
        val1 = dataArr.GetTuple1(pid1)
        val2 = dataArr.GetTuple1(pid2)
        val3 = dataArr.GetTuple1(pid3)
        val4 = dataArr.GetTuple1(pid4)
        count = 0
        cell_point_ids = []

        # Check edges for crossing the isovalue and compute intersection points
        if (val1 - user_isoval) * (val2 - user_isoval) < 0 and count < 2: #if the product is less than 0 then we can get a point on that edge
            count += 1                                                    # as one value > iso_value and other value < iso_value
            pt = coord(data.GetPoint(pid1), data.GetPoint(pid2), val1, val2, user_isoval)
            points.InsertNextPoint(pt)
            cell_point_ids.append(total_points)
            total_points += 1

        if (val2 - user_isoval) * (val3 - user_isoval) < 0 and count < 2:
            count += 1
            pt = coord(data.GetPoint(pid2), data.GetPoint(pid3), val2, val3, user_isoval)
            points.InsertNextPoint(pt)
            cell_point_ids.append(total_points)
            total_points += 1

        if (val3 - user_isoval) * (val4 - user_isoval) < 0 and count < 2:
            count += 1
            pt = coord(data.GetPoint(pid3), data.GetPoint(pid4), val3, val4, user_isoval)
            points.InsertNextPoint(pt)
            cell_point_ids.append(total_points)
            total_points += 1

        if (val4 - user_isoval) * (val1 - user_isoval) < 0 and count < 2:
            count += 1
            pt = coord(data.GetPoint(pid4), data.GetPoint(pid1), val4, val1, user_isoval)
            points.InsertNextPoint(pt)
            cell_point_ids.append(total_points)
            total_points += 1
        if count == 2:
            polyLine = vtkPolyLine()
            polyLine.GetPointIds().SetNumberOfIds(2)
            polyLine.GetPointIds().SetId(0, cell_point_ids[0])
            polyLine.GetPointIds().SetId(1, cell_point_ids[1])
            cells.InsertNextCell(polyLine)
    
    # Add points and lines to polydata
    pdata.SetPoints(points)
    pdata.SetLines(cells)

    # Write output .vtp file
    writer = vtkXMLPolyDataWriter()
    writer.SetInputData(pdata)
    writer.SetFileName('iso_surface.vtp')
    writer.Write()

user_isoval = float(input("Enter isovalue: "))
contour_extraction(user_isoval)