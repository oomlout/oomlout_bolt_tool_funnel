$fn = 50;


difference() {
	union() {
		translate(v = [0, 0, 0]) {
			rotate(a = [0, 0, 0]) {
				difference() {
					union() {
						cylinder(h = 30, r1 = 77.5000000000, r2 = 22.5000000000);
					}
					union() {
						cylinder(h = 30, r1 = 76.5000000000, r2 = 21.5000000000);
					}
				}
			}
		}
		translate(v = [0, 0, 30]) {
			rotate(a = [0, 0, 0]) {
				difference() {
					union() {
						cylinder(h = 45, r = 22.5000000000);
					}
					union() {
						cylinder(h = 45, r = 21.5000000000);
					}
				}
			}
		}
	}
	union();
}