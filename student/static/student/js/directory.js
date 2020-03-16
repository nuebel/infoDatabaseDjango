function confirmDelete() {
	return confirm("Are you sure you want to delete this person from the database?");
}

$(document).ready(function() {

$(".sorter").click( function(event) {
	var sort_by;
	if ( $(this).attr('id') == "sorter_lastname") sort_by = "last_name";
	else if ($(this).attr('id') == "sorter_firstname") sort_by = "first_name";
	else if ($(this).attr('id') == "sorter_schoolyear") sort_by = "school_year";
	else if ($(this).attr('id') == "sorter_color") sort_by = "color";
	else if ($(this).attr('id') == "sorter_address") sort_by = "address";
	console.log(`Sorting results by ${sort_by}`);

	var search_field = "last_name";
	var search_text = "";

	$.ajax({
		context: this,
		type : 'GET',
		url : '/student/ajax_searchsort',
		data : "search_field=" + search_field + "&search_text=" +  search_text + "&sort_by=" + sort_by
	})
		.done(function( data ) {
			//Replace the directory div with the Ajax data
			$('#directory').html(data);

			//Make the current sort by link unclickable and activate the one that was inactive
			$(".current").removeClass("current");
			$(this).addClass("current");
	})
		.fail(function() {
			console.log('Ajax get failed');
	});
});

});

