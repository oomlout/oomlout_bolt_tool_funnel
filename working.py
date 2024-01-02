import oom_kicad
import oom_markdown
import os
import copy

#process
#  locations set in working_parts.ods 
#  export to working_parts.csv
#  put components on the right side of the board
#  run this script

def main(**kwargs):
    #place_parts(**kwargs)
    #make_readme(**kwargs)
    make_scad(**kwargs)
    
    

def make_readme(**kwargs):
    os.system("generate_resolution.bat")
    oom_markdown.generate_readme_project(**kwargs)
    #oom_markdown.generate_readme_teardown(**kwargs)
    
def make_scad(**kwargs):
    import opsc
    import oobb 
    import oobb_base

    #kwargs["save_type"] = "none"
    kwargs["save_type"] = "all"
    #kwargs["save_type"] = "3dpr"
    
    #kwargs["modes"] = ["3dpr","laser","true"]
    kwargs["modes"] = "3dpr"
    
    kwargs["size"] = "oobb"
    kwargs["type"] = "oomlout_bolt_tool_funnel"
    kwargs["width"] = 1
    kwargs["height"] = 1
    kwargs["thickness"] = 1

   
    # funnel sizes
    funnels = []

    funnel = {}
    funnel["funnel_top_radius"] = 70/2
    funnel["funnel_bottom_radius"] = 30/2
    funnel["funnel_height"] = 30
    funnel["funnel_height_bottom_tube"] = 10
    funnel["funnel_wall_thickness"] = 1
    funnel["funnel_extra"] = "70_mm_top_30_mm_bottom"
    funnels.append(funnel)

    funnel = {}
    funnel["funnel_top_radius"] = 170/2
    funnel["funnel_bottom_radius"] = 90/2
    funnel["funnel_height"] = 50
    funnel["funnel_height_bottom_tube"] = 50
    funnel["funnel_wall_thickness"] = 1
    funnel["funnel_extra"] = "170_mm_top_90_mm_bottom"
    funnels.append(funnel)
    
    #load those values 

    for funnel in funnels:

    # default sets
        width = kwargs.get("width", 3)
        height = kwargs.get("height", 5)
        thickness = kwargs.get("thickness", 3)
        size = kwargs.get("size", "oobb")
        pos = kwargs.get("pos", [0, 0, 0])
        # extra sets
        holes = kwargs.get("holes", True)
        both_holes = kwargs.get("both_holes", True)    
        kwargs["pos"] = pos
        
            


        funnel_top_radius = funnel["funnel_top_radius"]
        funnel_bottom_radius = funnel["funnel_bottom_radius"]
        funnel_height = funnel["funnel_height"]
        funnel_height_bottom_tube = funnel["funnel_height_bottom_tube"]
        funnel_wall_thickness = funnel["funnel_wall_thickness"]
        funnel_extra = funnel["funnel_extra"]
        kwargs["extra"] = funnel_extra

        # get the default thing
        thing = oobb_base.get_default_thing(**kwargs)
        th = thing["components"]
        kwargs.pop("size","")

        p3 = copy.deepcopy(kwargs)
        p3["type"] = "p"   
        p3["shape"] = f"oobb_cylinder_hollow"
        p3["r1"] = funnel_top_radius
        p3["r2"] = funnel_bottom_radius
        p3["wall_thickness"] = funnel_wall_thickness
        p3["h"] = funnel_height
        p3["pos"] = pos
        #p3["m"] = ""  
        oobb_base.append_full(thing,**p3)      
        #th.append(oobb_base.oobb_easy(**p3))
        
        # add bottom tube
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "p"
        p3["shape"] = f"oobb_cylinder_hollow"
        p3["r"] = funnel_bottom_radius
        p3["wall_thickness"] = funnel_wall_thickness
        p3["h"] = funnel_height_bottom_tube
        pos1 = copy.deepcopy(pos)
        pos1[2] = pos1[2] + funnel_height
        p3["pos"] = pos1 
        #p3["m"] = ""
        oobb_base.append_full(thing,**p3)



        ######  save stuff    
            
        save_type = kwargs.get("save_type", "all")
        overwrite = True
        modes = kwargs.get("modes", ["3dpr","laser","true"])
        for mode in modes:
            depth = thing.get(
                "depth_mm", thing.get("thickness_mm", 3))
            height = thing.get("height_mm", 100)
            layers = depth / 3
            tilediff = height + 10
            start = 1.5
            if layers != 1:
                start = 1.5 - (layers / 2)*3
            if "bunting" in thing:
                start = 0.5
            opsc.opsc_make_object(f'scad_output/{thing["id"]}/{mode}.scad', thing["components"], mode=mode, save_type=save_type, overwrite=overwrite, layers=layers, tilediff=tilediff, start=start)
        
 


#take component positions from working_parts.csv and place them in working.kicad_pcb
def place_parts(**kwargs):
    board_file = "kicad/current_version/working/working.kicad_pcb"
    parts_file = "working_parts.csv"
    #load csv file
    import csv
    with open(parts_file, 'r') as f:
        reader = csv.DictReader(f)
        parts = [row for row in reader]


    
    oom_kicad.kicad_set_components(board_file=board_file, parts=parts, corel_pos=True, **kwargs)






if __name__ == '__main__':
    main()