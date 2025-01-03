$fn = 50;


difference() {
	union() {
		translate(v = [0, 0, 0]) {
			rotate(a = [0, 0, 0]) {
				difference() {
					union() {
						hull() {
							translate(v = [-15.0000000000, 15.0000000000, 0]) {
								cylinder(h = 25, r = 5, r1 = 30.0000000000, r2 = 5);
							}
							translate(v = [15.0000000000, 15.0000000000, 0]) {
								cylinder(h = 25, r = 5, r1 = 30.0000000000, r2 = 5);
							}
							translate(v = [-15.0000000000, -15.0000000000, 0]) {
								cylinder(h = 25, r = 5, r1 = 30.0000000000, r2 = 5);
							}
							translate(v = [15.0000000000, -15.0000000000, 0]) {
								cylinder(h = 25, r = 5, r1 = 30.0000000000, r2 = 5);
							}
						}
					}
					union() {
						hull() {
							translate(v = [-14.0000000000, 14.0000000000, 0]) {
								cylinder(h = 25, r = 5, r1 = 29.0000000000, r2 = 4);
							}
							translate(v = [14.0000000000, 14.0000000000, 0]) {
								cylinder(h = 25, r = 5, r1 = 29.0000000000, r2 = 4);
							}
							translate(v = [-14.0000000000, -14.0000000000, 0]) {
								cylinder(h = 25, r = 5, r1 = 29.0000000000, r2 = 4);
							}
							translate(v = [14.0000000000, -14.0000000000, 0]) {
								cylinder(h = 25, r = 5, r1 = 29.0000000000, r2 = 4);
							}
						}
					}
				}
			}
		}
		translate(v = [0, 0, 25]) {
			rotate(a = [0, 0, 0]) {
				difference() {
					union() {
						hull() {
							translate(v = [-15.0000000000, 15.0000000000, 0]) {
								cylinder(h = 25, r = 5);
							}
							translate(v = [15.0000000000, 15.0000000000, 0]) {
								cylinder(h = 25, r = 5);
							}
							translate(v = [-15.0000000000, -15.0000000000, 0]) {
								cylinder(h = 25, r = 5);
							}
							translate(v = [15.0000000000, -15.0000000000, 0]) {
								cylinder(h = 25, r = 5);
							}
						}
					}
					union() {
						hull() {
							translate(v = [-14.0000000000, 14.0000000000, 0]) {
								cylinder(h = 25, r = 5);
							}
							translate(v = [14.0000000000, 14.0000000000, 0]) {
								cylinder(h = 25, r = 5);
							}
							translate(v = [-14.0000000000, -14.0000000000, 0]) {
								cylinder(h = 25, r = 5);
							}
							translate(v = [14.0000000000, -14.0000000000, 0]) {
								cylinder(h = 25, r = 5);
							}
						}
					}
				}
			}
		}
	}
	union();
}