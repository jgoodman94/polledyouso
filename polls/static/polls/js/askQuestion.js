$(function() {
	$('table#numAnsSelect td').click(function() {
		numAnswers = $(this).text(); // global
		$('#numAnsSelect').hide();
		$('#numberAnsSelect').val(numAnswers);
		$('#numberAnsSelect').show();
		for (var i = 1; i <= numAnswers; i++) {
			$('#ans' + i).show("slide", { direction: "left" }, 500);
		}
		$('#ans1').focus();
	});

	$('#numberAnsSelect').focusout(function() {
		// user enters new number of fields
		if ($('#numberAnsSelect').val() != numAnswers) {
			numAnswers = $('#numberAnsSelect').val();
			$('.answer.uploadField').hide();
			// user selects invalid number of answers
			if (numAnswers == 69) {
				alert('you dog, you');
				$(this).focus();
				return false;
			}
			else if (numAnswers > 5 || numAnswers < 1) {
				alert('Please select between 1 and 5 answers.');
				$(this).focus();
				return false;
			}
			// user selects valid number of answers
			// show appropriate number of fields
			for (var i = 1; i <= numAnswers; i++) {
				$('#ans' + i).show("drop", 500);
			}
			$('#ans1').focus();
		}
	});

	$('#clickToAsk').click(function() {
		$('#overlay').show();
		$('#uploadQuestion').show('drop',500);
	});

	$('#overlay').click(function() {
		closeModal();
	});

	Parse.User.logOut();
});

function submitQuestion() {
	console.log('hey');
	var question = $('#yourQ').val();
	var ans1 = $('#ans1').val();
	var ans2 = $('#ans2').val();
	var ans3 = $('#ans3').val();
	var ans4 = $('#ans4').val();
	var ans5 = $('#ans5').val();


	var UserQuestion = Parse.Object.extend('Questions');
	var userQuestion = new UserQuestion();
	userQuestion.save(
	{
		question: question,
		answer_one: ans1,
		answer_two: ans2,
		answer_three: ans3,
		answer_four: ans4,
		answer_five: ans5
	});
    // initialize array answers
    userQuestion.save({one_answers: []});
    userQuestion.save({two_answers: []});
    userQuestion.save({three_answers: []});
    userQuestion.save({four_answers: []});
    userQuestion.save({five_answers: []});

	closeModal();
	window.setTimeout(function() {
		resetUpload();
	},500);
}

// close modal question window and overlay
function closeModal() {
	$('#uploadQuestion').hide('drop',250);
	$('#overlay').hide('drop', 250);
}

// reset question upload fields
function resetUpload() {
	numAnswers = 0;
	$('.answer.uploadField').hide();
	$('.answer.uploadField').val('');
	$('#numAnsSelect').show();
}