$fn = 50;


difference() {
	union() {
		translate(v = [0, 0, 0]) {
			rotate(a = [0, 0, 0]) {
				difference() {
					union() {
						cylinder(h = 20, r1 = 27.5000000000, r2 = 7.5000000000);
					}
					union() {
						cylinder(h = 20, r1 = 25.5000000000, r2 = 5.5000000000);
					}
				}
			}
		}
		translate(v = [0, 0, 20]) {
			rotate(a = [0, 0, 0]) {
				difference() {
					union() {
						cylinder(h = 15, r = 7.5000000000);
					}
					union() {
						cylinder(h = 15, r = 5.5000000000);
					}
				}
			}
		}
	}
	union();
}