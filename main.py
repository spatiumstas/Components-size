import xml.etree.ElementTree as ET

def parse_sizes_from_xml(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()
    
    components = []
    
    for component in root.findall('component'):
        name_element = component.find('name')
        size_element = component.find('size')
        
        if name_element is not None and size_element is not None:
            module_name = name_element.text
            size_in_bytes = int(size_element.text)
            size_in_mb = size_in_bytes / (1024 * 1024)
            components.append((module_name, size_in_mb))
    
    return components

def main():
    file_path = 'components.xml'
    components = parse_sizes_from_xml(file_path)
    
    components_sorted = sorted(components, key=lambda x: x[1], reverse=True)
    
    for module_name, size in components_sorted:
        print(f"{module_name}: {size:.2f} MB")

if __name__ == "__main__":
    main()
