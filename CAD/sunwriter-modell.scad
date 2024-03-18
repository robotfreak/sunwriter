diameter=408;
height=840;
mirror_side=340;
mirror_height=mirror_side/2*sqrt(3);
mirror_thick=6;
mon_width=519;
mon_height=299;
$fn=100;

module mirrors(h, s, t) {
    linear_extrude(height) {
        difference() {
            polygon(points=[[h/2+t,0], [-(h/2+t),s/2+t], [-(h/2+t),-(s/2+t)]], paths=[[0,1,2]]);
            translate([-2,0,0]) polygon(points=[[h/2,0], [-h/2,s/2], [-h/2,-s/2]], paths=[[0,1,2]]);
        }
    }
}

module monitor() {
    color("blue") cube([mon_width,mon_height,10], center=true);
    color("brown") translate([0,-(mon_height/2+15),75]) cube([650,20,150], center=true);
    color("grey") translate([0,-(mon_height/2+45),75]) cube([200,40,100], center=true);
}

module beamer() {
    color("blue") cube([mon_width,mon_height,10], center=true);
    color("grey") translate([0,mon_height/2+95,250]) cube([1000,100,500], center=true);
}

mirrors(mirror_height, mirror_side, mirror_thick);


// Aussenhülle
translate([-50,0,0]) difference() {
    cylinder(d=diameter+16, h=height);
    cylinder(d=diameter, h=height);
}

// Spiegel
//translate([47.7,-73,0]) rotate([0,0,-30]) difference() {
    //linear_extrude(height) mirrors(mirror_height+16, mirror_side+16);
//    mirrors(mirror_height, mirror_side);
//}

// 1x24" Monitore
translate([0,0,height+5]) rotate([0,0,-90]) monitor();
