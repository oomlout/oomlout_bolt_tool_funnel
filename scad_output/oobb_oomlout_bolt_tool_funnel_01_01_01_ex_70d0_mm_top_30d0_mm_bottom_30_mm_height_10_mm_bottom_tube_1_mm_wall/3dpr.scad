$fn = 50;


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
	}
	union();
}