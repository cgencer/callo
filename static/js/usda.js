
function search_food(name) {
    $.ajax({
        type: 'GET',
        url: '/energy/food/?name=' + name,
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

function get_nutrients(ndbno, callback) {
    $.ajax({
        type: 'GET',
        url: '/energy/food/?ndbno=' + ndbno,
        dataType: 'json',
        contentType: 'application/json; charset=utf-8',
        success: callback.success(response),
        error: callback.error(error)
    });
}