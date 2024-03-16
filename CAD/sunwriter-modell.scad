diameter=400;
height=840;
mirror_side=335;
mirror_height=mirror_side/2*sqrt(3);
mon_width=519;
mon_height=299;
$fn=100;

module mirrors(h, s) {
    polygon(points=[[h/2,0], [-h/2,s/2], [-h/2,-s/2]], paths=[[0,1,2]]);
}

module monitor() {
    color("blue") cube([mon_width,mon_height,10], center=true);
    color("grey") translate([0,-(mon_height/2+15),50]) cube([600,20,100], center=true);
}

module beamer() {
    color("blue") cube([mon_width,mon_height,10], center=true);
    color("grey") translate([0,mon_height/2+75,250]) cube([1000,100,500], center=true);
}

// Aussenhülle
translate([0,-50,0]) difference() {
    cylinder(d=diameter+16, h=height);
    cylinder(d=diameter, h=height);
}

// Spiegel
translate([44,-73,0]) rotate([0,0,-30]) difference() {
    linear_extrude(height) mirrors(mirror_height+16, mirror_side+16);
    linear_extrude(height) mirrors(mirror_height, mirror_side);
}

// 1x24" Monitore
translate([0,0,height+5]) rotate([0,0,0]) monitor();
