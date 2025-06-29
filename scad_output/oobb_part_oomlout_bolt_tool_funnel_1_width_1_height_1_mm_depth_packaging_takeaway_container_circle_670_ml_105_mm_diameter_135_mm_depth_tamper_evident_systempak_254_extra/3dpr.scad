$fn = 50;


difference() {
	union() {
		translate(v = [0, 0, 0]) {
			rotate(a = [0, 0, 0]) {
				difference() {
					union() {
						cylinder(h = 30, r1 = 85.0000000000, r2 = 45.0000000000);
					}
					union() {
						cylinder(h = 30, r1 = 82.0000000000, r2 = 42.0000000000);
					}
				}
			}
		}
		translate(v = [0, 0, 30]) {
			rotate(a = [0, 0, 0]) {
				difference() {
					union() {
						cylinder(h = 20, r = 45.0000000000);
					}
					union() {
						cylinder(h = 20, r = 42.0000000000);
					}
				}
			}
		}
	}
	union();
}