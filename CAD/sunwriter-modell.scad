diameter=570;
height=1300;
top_diameter=685;
top_height=100;

mirror_side=340;
mirror_height=mirror_side/2*sqrt(3);
mirror_thick=6;
mon_width=535;
mon_height=315;
glass_width=550;
glass_height=400;
$fn=100;

module mirrors(h, s, t) {
    difference() {
         linear_extrude(height) polygon(points=[[h/2+t,0], [-(h/2+t),s/2+t], [-(h/2+t),-(s/2+t)]], paths=[[0,1,2]]);
         translate([-2,0,-5]) linear_extrude(height+10)  polygon(points=[[h/2,0], [-h/2,s/2], [-h/2,-s/2]], paths=[[0,1,2]]);
    }
}

module monitor() {
    color("blue") cube([mon_width,mon_height,10], center=true);
    color("yellow") translate([0,-40,-10]) cube([glass_width,glass_height,10], center=true);
    color("green") translate([0,-(mon_height/2+20),0]) cube([mon_width,40,10], center=true);
    color("grey") translate([0,-(mon_height/2+60),-40]) cube([200,40,100], center=true);
}

module beamer() {
    color("blue") cube([mon_width,mon_height,10], center=true);
    color("grey") translate([0,mon_height/2+95,250]) cube([1000,100,500], center=true);
}

translate([0,0,0]) mirrors(mirror_height, mirror_side, mirror_thick);

// Tophuelle
translate([-40,0,height]) difference() {
    cylinder(d=top_diameter, h=top_height);
    translate([0,0,-5]) cylinder(d=top_diameter-16, h=top_height+10);
}

// Aussenhuelle
translate([-40,0,0]) difference() {
    cylinder(d=diameter, h=height);
    translate([0,0,-5]) cylinder(d=diameter-16, h=height+10);
}

// Spiegel
//translate([47.7,-73,0]) rotate([0,0,-30]) difference() {
    //linear_extrude(height) mirrors(mirror_height+16, mirror_side+16);
//    mirrors(mirror_height, mirror_side);
//}

// 1x24" Monitore
translate([0,0,height+5]) rotate([0,0,-90]) monitor();
