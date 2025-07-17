$fn = 50;


difference() {
	union() {
		translate(v = [0, 0, 0]) {
			rotate(a = [0, 0, 0]) {
				difference() {
					union() {
						cylinder(h = 75, r1 = 110.0000000000, r2 = 37.5000000000);
					}
					union() {
						cylinder(h = 75, r1 = 108.0000000000, r2 = 35.5000000000);
					}
				}
			}
		}
		translate(v = [0, 0, 75]) {
			rotate(a = [0, 0, 0]) {
				difference() {
					union() {
						cylinder(h = 20, r = 37.5000000000);
					}
					union() {
						cylinder(h = 20, r = 35.5000000000);
					}
				}
			}
		}
	}
	union();
}