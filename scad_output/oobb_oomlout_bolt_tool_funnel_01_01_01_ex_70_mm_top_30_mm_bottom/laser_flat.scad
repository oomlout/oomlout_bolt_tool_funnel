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
										cylinder(h = 30, r1 = 35.0000000000, r2 = 15.0000000000);
									}
									union() {
										cylinder(h = 30, r1 = 34.0000000000, r2 = 14.0000000000);
									}
								}
							}
						}
						translate(v = [0, 0, 30]) {
							rotate(a = [0, 0, 0]) {
								difference() {
									union() {
										cylinder(h = 10, r = 15.0000000000);
									}
									union() {
										cylinder(h = 10, r = 14.0000000000);
									}
								}
							}
						}
						*color(alpha = 1.0000000000, c = "gray") {
							translate(v = [0, 14, 0]) {
								linear_extrude(height = 1) {
									text(font = "Arial:style=Bold", halign = "center", size = 4.5000000000, text = "COMMENT description oobb_cylinder_hollow_shape_p_type_all_save_type_1_width_1_height_1_thickness_70_mm_top_30_mm_bottom_extra_35.0_r1_15.0_r2_1_wall_thickness_30_h", valign = "center");
								}
							}
						}
						*color(alpha = 1.0000000000, c = "gray") {
							translate(v = [0, 14, 30]) {
								linear_extrude(height = 1) {
									text(font = "Arial:style=Bold", halign = "center", size = 4.5000000000, text = "COMMENT description oobb_cylinder_hollow_shape_p_type_0_0_30_pos_all_save_type_1_width_1_height_1_thickness_70_mm_top_30_mm_bottom_extra_15.0_r_1_wall_thickness_10_h", valign = "center");
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