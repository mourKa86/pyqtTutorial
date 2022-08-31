import os

def editSVGStyle(iconsPath):
    import_path = os.path.join(iconsPath)
    file_list = sorted(os.listdir(import_path))
    svg_list = [item for item in file_list if item.endswith('.svg')]

    for svg_file in svg_list:
        svg_path = os.path.join(import_path, svg_file)

        fin = open(svg_path, "rt")
        data = fin.read()
        data = data.replace('stroke="currentColor"','stroke="white"')
        fin.close()

        fin = open(svg_path, "wt")
        fin.write(data)
        fin.close()


editSVGStyle('white\\')