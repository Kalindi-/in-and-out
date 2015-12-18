var $mouseX = 0, $mouseY = 0;
var $xp = -10, $yp = 50;

$(document).mousemove( function(e){
    $mouseX = e.pageX;
    $mouseY = e.pageY;
});

var $loop = setInterval( function(){
	$xp += (($mouseX - $xp)/100);
	$yp += (($mouseY - $yp)/100);
	$("#follow").css({left:$xp +'px', top:$yp +'px'});
	var offset = $("#follow").offset();

	function mouse(evt) {
	    var center_x = (offset.left) + ($("#follow").width()/2);
	    var center_y = (offset.top) + ($("#follow").height()/2);
	    var radians = Math.atan2($mouseX - center_x, $mouseY - center_y);
	    var degree = (radians * (180 / Math.PI) * -1) - 90;

        // commented code makes chick flip, when mouse is on the other side,
        // but I like making it go round and round. But, I leave it here, for info, and future.
	    //if ($mouseX > center_x) {
	    	$("#follow").css('-webkit-transform', 'rotate('+degree+'deg) scale(1,-1)');
	    	$("#follow").css('-ms-transform', 'rotate('+degree+'deg) scale(1,-1)');
	    	$("#follow").css('transform', 'rotate('+degree+'deg) scale(1,-1)');
		//} else {
	    //	  $("#follow").css('-webkit-transform', 'rotate('+degree+'deg) scale(1,1)');
	    //	  $("#follow").css('-ms-transform', 'rotate('+degree+'deg) scale(1,1)');
	 	//    $("#follow").css('transform', 'rotate('+degree+'deg) scale(1,1)');
		//}
	}
	$(document).mousemove(mouse);
}, 30);



// thanks to
// http://stackoverflow.com/questions/3385936/jquery-follow-the-cursor-with-a-div/19708460#19708460
// http://stackoverflow.com/questions/9972449/rotating-an-element-based-on-cursor-position-in-a-separate-element/10235298#10235298
