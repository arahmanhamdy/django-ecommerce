jQuery(document).ready(function($){
	$(".memenu").memenu();

	function convertToSlug(Text)
	{
		return Text
			.toLowerCase()
			.replace(/ /g,'-')
			.replace(/[^\w-]+/g,'')
			;
	}

	function getCookie(name) {
		var cookieValue = null;
		if (document.cookie && document.cookie !== '') {
			var cookies = document.cookie.split(';');
			for (var i = 0; i < cookies.length; i++) {
				var cookie = jQuery.trim(cookies[i]);
				// Does this cookie string begin with the name we want?
				if (cookie.substring(0, name.length + 1) === (name + '=')) {
					cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
					break;
				}
			}
		}
		return cookieValue;
	}


	simpleCart({
    	cartStyle: "table",
    	cartColumns: [
			{ attr: "id" , label: false} ,
    		{ view: 'image' , attr:'image', label: false},
    		{ attr: "name" , label: "Name", view: function(item, column){
    				console.log(item);
    				return "<a href='/product/"+item.get("id")+"/"+convertToSlug(item.get("name"))+"'>"+
    				item.get("name")+"</a>"
    			}
    		},
            { attr: "price" , label: "Price", view: 'currency' } ,
            { view: "decrement" , label: false , text: "-" } ,
            { attr: "quantity" , label: "Qty" } ,
            { view: "increment" , label: false , text: "+" } ,
            { attr: "total" , label: "SubTotal", view: 'currency' } ,
            { view: "remove" , text: "Remove" , label: false }
        ],
        checkout: {
			type: "SendForm",
			url: "/orders/order",
			success: "/orders/order/complete",
			cancel: "cancel.html",
			extra_data: {
				csrfmiddlewaretoken: getCookie("csrftoken")
			}
		},
		excludeFromCheckout: [],
  	});
  	simpleCart.bind("afterCreate", function(){
   		$cart_table = $(".simpleCart_items table")
   		$(".simpleCart_items").find("img").attr("width", "50px")
   		$cart_table.addClass("table").addClass("table-hover")
	});
});
