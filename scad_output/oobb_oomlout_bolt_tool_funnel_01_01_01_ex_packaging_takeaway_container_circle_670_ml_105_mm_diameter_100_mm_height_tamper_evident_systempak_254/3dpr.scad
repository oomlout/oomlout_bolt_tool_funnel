$fn = 50;


difference() {
	union() {
		translate(v = [0, 0, 0]) {
			rotate(a = [0, 0, 0]) {
				difference() {
					union() {
						cylinder(h = 30, r1 = 72.5000000000, r2 = 42.5000000000);
					}
					union() {
						cylinder(h = 30, r1 = 70.5000000000, r2 = 40.5000000000);
					}
				}
			}
		}
		translate(v = [0, 0, 30]) {
			rotate(a = [0, 0, 0]) {
				difference() {
					union() {
						cylinder(h = 20, r = 42.5000000000);
					}
					union() {
						cylinder(h = 20, r = 40.5000000000);
					}
				}
			}
		}
	}
	union();
}