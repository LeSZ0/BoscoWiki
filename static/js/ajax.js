$(function() {

	$('#search').keyup(function() {

		$.ajax({
			type: 'POST',
			url: '/post/search/',
			data: {
				'search_text': $('#search').val(),
				'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val()
			},
			success: searchSuccess,
			dataType: 'html'
		});
	});
});

function searchSuccess(data, textStatus, jqXHR) {
	$('#search_result').html(data);
}