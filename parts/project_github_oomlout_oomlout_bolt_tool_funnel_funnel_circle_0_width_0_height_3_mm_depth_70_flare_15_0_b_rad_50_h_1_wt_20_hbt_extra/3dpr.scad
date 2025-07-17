$fn = 50;


difference() {
	union() {
		translate(v = [0, 0, 0]) {
			rotate(a = [0, 0, 0]) {
				difference() {
					union() {
						cylinder(h = 50, r1 = 85.0000000000, r2 = 15.0000000000);
					}
					union() {
						cylinder(h = 50, r1 = 84.0000000000, r2 = 14.0000000000);
					}
				}
			}
		}
		translate(v = [0, 0, 50]) {
			rotate(a = [0, 0, 0]) {
				difference() {
					union() {
						cylinder(h = 20, r = 15.0000000000);
					}
					union() {
						cylinder(h = 20, r = 14.0000000000);
					}
				}
			}
		}
	}
	union();
}