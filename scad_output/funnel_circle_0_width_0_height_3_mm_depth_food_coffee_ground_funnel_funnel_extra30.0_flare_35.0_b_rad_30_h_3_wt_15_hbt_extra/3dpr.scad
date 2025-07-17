$fn = 50;


difference() {
	union() {
		translate(v = [0, 0, 0]) {
			rotate(a = [0, 0, 0]) {
				difference() {
					union() {
						cylinder(h = 30, r1 = 65.0000000000, r2 = 35.0000000000);
					}
					union() {
						cylinder(h = 30, r1 = 62.0000000000, r2 = 32.0000000000);
					}
				}
			}
		}
		translate(v = [0, 0, 30]) {
			rotate(a = [0, 0, 0]) {
				difference() {
					union() {
						cylinder(h = 15, r = 35.0000000000);
					}
					union() {
						cylinder(h = 15, r = 32.0000000000);
					}
				}
			}
		}
	}
	union();
}