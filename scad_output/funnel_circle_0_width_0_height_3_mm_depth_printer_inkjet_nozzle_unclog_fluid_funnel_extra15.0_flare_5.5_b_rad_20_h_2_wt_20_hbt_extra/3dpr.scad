$fn = 50;


difference() {
	union() {
		translate(v = [0, 0, 0]) {
			rotate(a = [0, 0, 0]) {
				difference() {
					union() {
						cylinder(h = 20, r1 = 20.5000000000, r2 = 5.5000000000);
					}
					union() {
						cylinder(h = 20, r1 = 18.5000000000, r2 = 3.5000000000);
					}
				}
			}
		}
		translate(v = [0, 0, 20]) {
			rotate(a = [0, 0, 0]) {
				difference() {
					union() {
						cylinder(h = 20, r = 5.5000000000);
					}
					union() {
						cylinder(h = 20, r = 3.5000000000);
					}
				}
			}
		}
	}
	union();
}