var $mouseX = 0, $mouseY = 0;
var $xp = -10, $yp = 50;

$(document).mousemove(function(e){
    $mouseX = e.pageX;
    $mouseY = e.pageY;
});

var $loop = setInterval(function(){
	$xp += (($mouseX - $xp)/100);
	$yp += (($mouseY - $yp)/100);
	$("#follow").css({left:$xp +'px', top:$yp +'px'});
	var offset = $("#follow").offset();
	function mouse(evt){
	    var center_x = (offset.left) + ($("#follow").width()/2);
	    var center_y = (offset.top) + ($("#follow").height()/2);
	    var radians = Math.atan2($mouseX - center_x, $mouseY - center_y);
	    var degree = (radians * (180 / Math.PI) * -1) - 90;

	    $("#follow").css('-moz-transform', 'rotate('+degree+'deg)');
	    $("#follow").css('-webkit-transform', 'rotate('+degree+'deg)');
	    $("#follow").css('-o-transform', 'rotate('+degree+'deg)');
	    $("#follow").css('-ms-transform', 'rotate('+degree+'deg)');
	}
	$(document).mousemove(mouse);
}, 30);


// TODO: make chick flip depending on the part of the page it is on.

// thanks to
// http://stackoverflow.com/questions/3385936/jquery-follow-the-cursor-with-a-div/19708460#19708460
// http://stackoverflow.com/questions/9972449/rotating-an-element-based-on-cursor-position-in-a-separate-element/10235298#10235298
