function search_foods(callback) {
	$.ajax({
	    type: 'GET',
	    url: '/energy/food/?name=' + $('#txtName').val(),
	    dataType: 'json',
        contentType: 'application/json; charset=utf-8',
	    success: function(response) {
	        $('#lblData').html(JSON.stringify(response));
	    },
	    error: function(error) {
	        console.log(error);
	    }
	 });
}