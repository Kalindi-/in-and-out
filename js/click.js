
// some click functionalities

/*********************************************************************************/

function whereFrom() {
	$.getJSON("http://freegeoip.net/json/", function (data) {
    var country_on_load = data.country_name;
    console.log(country_on_load)
    $.post( "/", { country: country_on_load } );
  });

}
window.addEventListener('load', whereFrom);
