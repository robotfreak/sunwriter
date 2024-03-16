diameter=3330;
height=7000;
mirror_side=2250;
mirror_height=mirror_side/2*sqrt(3);
mon_width=2170;
mon_height=1220;
$fn=100;

module mirrors(h, s) {
    polygon(points=[[h/2,0], [-h/2,s/2], [-h/2,-s/2]], paths=[[0,1,2]]);
}

module monitor() {
    color("blue") cube([mon_width,mon_height,10], center=true);
    color("grey") translate([0,mon_height/2+75,250]) cube([1000,100,500], center=true);
}

module beamer() {
    color("blue") cube([mon_width,mon_height,10], center=true);
    color("grey") translate([0,mon_height/2+75,250]) cube([1000,100,500], center=true);
}

// Aussenhülle
difference() {
    cylinder(d=diameter, h=height);
    cylinder(d=diameter-50, h=height);
}

// Spiegel
difference() {
    linear_extrude(height) mirrors(mirror_height+30, mirror_side+30);
    linear_extrude(height) mirrors(mirror_height, mirror_side);
}

// 2x 98" Monitore
translate([0,mon_height/2+10,height]) monitor();
translate([0,-(mon_height/2+10),height]) rotate([0,0,180]) monitor();