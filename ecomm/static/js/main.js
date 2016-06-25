jQuery(document).ready(function($){
	$(".memenu").memenu();
	$("#slider").responsiveSlides({
		auto: true,
		nav: true,
		speed: 500,
		namespace: "callbacks",
		pager: true
    });
});
