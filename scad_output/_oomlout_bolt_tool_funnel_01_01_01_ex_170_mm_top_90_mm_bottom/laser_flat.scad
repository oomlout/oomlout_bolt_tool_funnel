$fn = 50;


union() {
	translate(v = [0, 0, 0]) {
		projection() {
			intersection() {
				translate(v = [-500, -500, 1.0000000000]) {
					cube(size = [1000, 1000, 0.1000000000]);
				}
				difference() {
					union() {
						translate(v = [0, 0, 0]) {
							rotate(a = [0, 0, 0]) {
								difference() {
									union() {
										cylinder(h = 50, r1 = 85.0000000000, r2 = 45.0000000000);
									}
									union() {
										cylinder(h = 50, r1 = 84.0000000000, r2 = 44.0000000000);
									}
								}
							}
						}
						translate(v = [0, 0, 50]) {
							rotate(a = [0, 0, 0]) {
								difference() {
									union() {
										cylinder(h = 50, r = 45.0000000000);
									}
									union() {
										cylinder(h = 50, r = 44.0000000000);
									}
								}
							}
						}
						*color(alpha = 1.0000000000, c = "gray") {
							translate(v = [0, 14, 0]) {
								linear_extrude(height = 1) {
									text(font = "Arial:style=Bold", halign = "center", size = 4.5000000000, text = "COMMENT description oobb_cylinder_hollow_shape_p_type_all_save_type_1_width_1_height_1_thickness_170_mm_top_90_mm_bottom_extra_85.0_r1_45.0_r2_1_wall_thickness_50_h", valign = "center");
								}
							}
						}
						*color(alpha = 1.0000000000, c = "gray") {
							translate(v = [0, 14, 50]) {
								linear_extrude(height = 1) {
									text(font = "Arial:style=Bold", halign = "center", size = 4.5000000000, text = "COMMENT description oobb_cylinder_hollow_shape_p_type_0_0_50_pos_all_save_type_1_width_1_height_1_thickness_170_mm_top_90_mm_bottom_extra_45.0_r_1_wall_thickness_50_h", valign = "center");
								}
							}
						}
					}
					union();
				}
			}
		}
	}
}